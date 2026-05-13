"""Magazine CLI: fetch, parse, translate, and send to Feishu."""

import argparse
import asyncio
import os
import re
import sys
from pathlib import Path
from typing import List, Optional

from dotenv import load_dotenv

import httpx

from .fetcher import download_epub, get_latest_issue
from .parser import extract_article_text, extract_toc, get_main_articles

# Load .env from project root
load_dotenv(Path(__file__).parent.parent.parent / ".env")

ZH_NAMES = {"economist": "经济学人", "new_yorker": "纽约客"}


def _chunk_text(text: str, max_len: int = 4000) -> List[str]:
    """Split text at paragraph boundaries, each chunk <= max_len chars."""
    paragraphs = text.split("\n\n")
    chunks = []
    current = []
    current_len = 0
    for para in paragraphs:
        plen = len(para)
        if current and current_len + plen + 2 > max_len:
            chunks.append("\n\n".join(current))
            current = [para]
            current_len = plen
        else:
            current.append(para)
            current_len += plen + (2 if current_len else 0)
    if current:
        chunks.append("\n\n".join(current))
    return chunks or [text]


async def translate_text(text: str, system_prompt: str = None, max_tokens: int = 16384) -> str:
    """Translate text using DeepSeek API (OpenAI-compatible)."""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("[red]Error: No API key found. Set DEEPSEEK_API_KEY or ANTHROPIC_API_KEY[/red]")
        sys.exit(1)

    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.getenv("TRANSLATION_MODEL", "deepseek-chat")

    if not system_prompt:
        system_prompt = (
            "你是一位专业的英中翻译编辑，擅长翻译《经济学人》《纽约客》等英文杂志文章。\n"
            "请将以下英文文章完整翻译成地道的中文，保留原文的风格和语气。\n"
            "- 专业术语保持准确\n"
            "- 长句按中文习惯拆分\n"
            "- 保留原文的段落结构\n"
            "- 直接输出翻译结果，不要加注释或说明"
        )

    async with httpx.AsyncClient(timeout=300.0) as client:
        resp = await client.post(
            f"{base_url}/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": text},
                ],
                "temperature": 0.3,
                "max_tokens": max_tokens,
            },
        )
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]


async def translate_toc(toc_items: list) -> list:
    """Translate all TOC item labels in one batch."""
    if not toc_items:
        return []

    # Batch all titles together for efficient translation
    lines = []
    for i, item in enumerate(toc_items):
        label = item.get("label", "")
        if label:
            lines.append(f"[{i}] {label}")

    if not lines:
        return toc_items

    text = "\n".join(lines)
    system_prompt = (
        "你是一位专业的翻译。请将以下英文文章标题逐条翻译成中文。\n"
        "保持原标题的含义和风格，不要添加额外说明。\n"
        "严格按照以下格式回复：\n"
        "[序号] 中文翻译\n"
        "每条一行。"
    )

    try:
        result = await translate_text(text, system_prompt)
        translations = {}
        for line in result.strip().split("\n"):
            m = re.match(r"\[(\d+)\]\s*(.*)", line.strip())
            if m:
                idx = int(m.group(1))
                translations[idx] = m.group(2)

        for i, item in enumerate(toc_items):
            if i in translations:
                item["translation"] = translations[i]
    except Exception as e:
        print(f"  [yellow]TOC translation failed: {e}[/yellow]")

    return toc_items


async def send_to_feishu(card: dict) -> bool:
    """Send card message via Feishu webhook (magazine-specific)."""
    webhook_url = os.getenv("HORIZON_MAGAZINE_WEBHOOK_URL")
    if not webhook_url:
        webhook_url = os.getenv("HORIZON_WEBHOOK_URL")
    if not webhook_url:
        print("[red]Error: HORIZON_WEBHOOK_URL not set[/red]")
        return False

    full_payload = {
        "msg_type": "interactive",
        "card": card["card"],
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(webhook_url, json=full_payload)
        result = resp.json()
        if result.get("code") == 0:
            print(f"  [green]Sent successfully[/green]")
            return True
        else:
            print(f"  [red]Feishu error: {result.get('msg', result)}[/red]")
            return False


def build_toc_card(magazine: str, date_label: str, toc_items: list, total_articles: int) -> dict:
    """Build a Feishu card with the TOC overview only."""
    zh_name = ZH_NAMES.get(magazine, magazine)

    toc_md = ""
    for item in toc_items[:30]:
        label = item.get("label", "")
        translation = item.get("translation", "")
        toc_md += f"- {label}"
        if translation:
            toc_md += f"\n  _{translation}_"
        toc_md += "\n"

    return {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {
                    "tag": "plain_text",
                    "content": f"📚 {zh_name} · {date_label}",
                }
            },
            "elements": [
                {"tag": "markdown", "content": f"**📅 期号：{date_label}**"},
                {"tag": "hr"},
                {
                    "tag": "markdown",
                    "content": f"**📋 本期目录（共 {total_articles} 篇）**\n\n{toc_md}",
                },
                {"tag": "hr"},
                {
                    "tag": "note",
                    "elements": [
                        {"tag": "plain_text", "content": "Horizon Magazine · 由 AI 自动翻译 · 仅供参考"}
                    ],
                },
            ],
        },
    }


def build_article_cards(
    magazine: str,
    date_label: str,
    article_title: str,
    article_translation: str,
    original_text: str,
    article_idx: int = 1,
    article_total: int = 1,
) -> list:
    """Build one or more Feishu cards for a single article.

    Long translations are split across multiple markdown elements within
    the card (up to 4000 chars each). If even that overflows, multiple
    cards are returned.
    """
    zh_name = ZH_NAMES.get(magazine, magazine)
    MAX_PER_ELEMENT = 4000
    # Leave room for title block + hr + note (~4 elements overhead)
    MAX_ELEMS = 46

    chunks = _chunk_text(article_translation, MAX_PER_ELEMENT)

    def _make_card(chunk_slice, is_first, is_last):
        elements = []
        if is_first:
            elements.append({
                "tag": "markdown",
                "content": (
                    f"**📝 {article_title}**\n\n"
                    f"*{zh_name} · {date_label} · 文章 {article_idx}/{article_total}*"
                ),
            })
            elements.append({"tag": "hr"})
            elements.append({"tag": "markdown", "content": f"**中文翻译：**\n\n{chunk_slice[0]}"})
            for c in chunk_slice[1:]:
                elements.append({"tag": "markdown", "content": c})
        else:
            for c in chunk_slice:
                elements.append({"tag": "markdown", "content": c})

        if is_last and original_text:
            elements.append({"tag": "hr"})
            # Attach first 5000 chars of original as preview
            original_preview = original_text[:5000]
            if len(original_text) > 5000:
                original_preview += "\n\n*[原文过长已截断]*"
            elements.append({"tag": "markdown", "content": f"**📄 英文原文**\n\n{original_preview}"})

        elements.append({
            "tag": "note",
            "elements": [
                {"tag": "plain_text", "content": "Horizon Magazine · 由 AI 自动翻译 · 仅供参考"}
            ],
        })

        return {
            "msg_type": "interactive",
            "card": {
                "header": {
                    "title": {"tag": "plain_text", "content": f"📝 {article_title[:50]}"},
                },
                "elements": elements,
            },
        }

    if len(chunks) <= MAX_ELEMS - 4:
        return [_make_card(chunks, True, True)]

    # Split across multiple cards
    cards = []
    stride = MAX_ELEMS - 2
    for i in range(0, len(chunks), stride):
        slot = chunks[i : i + stride]
        cards.append(_make_card(slot, is_first=(i == 0), is_last=(i + len(slot) >= len(chunks))))
    return cards


async def process_magazine(magazine: str, num_articles: int = 2) -> None:
    """Full pipeline: download latest issue → parse → translate → send."""
    zh_name = ZH_NAMES.get(magazine, magazine)
    print(f"\n{'='*50}")
    print(f"  {zh_name} - {magazine}")
    print(f"{'='*50}\n")

    # 1. Get latest issue
    print("📡 Checking for latest issue...")
    date_label, dir_name, raw_dir_url = await get_latest_issue(magazine)
    print(f"  Latest: {date_label} ({dir_name})")

    # 2. Download EPUB
    epub_path = Path(f"/tmp/{magazine}_{date_label}.epub")
    await download_epub(raw_dir_url, epub_path)

    # 3. Extract TOC
    print("\n📖 Parsing EPUB...")
    all_toc = extract_toc(epub_path)
    print(f"  Found {len(all_toc)} TOC entries")

    if not all_toc:
        print("[red]Could not extract TOC. Skipping.[/red]")
        epub_path.unlink(missing_ok=True)
        return

    # 4. Filter to real articles
    toc_items = get_main_articles(epub_path, all_toc)
    print(f"  Filtered to {len(toc_items)} articles")

    # 5. Select articles
    selected = toc_items[:num_articles]
    print(f"\n📄 Selected {len(selected)} articles:")
    for s in selected:
        print(f"  - {s['label']}")

    # 6. Translate TOC titles
    print("\n🌐 Translating TOC titles...")
    all_toc = await translate_toc(all_toc)
    print(f"  Translated {len(all_toc)} titles")

    # 7. Send TOC overview card
    print("\n📬 Sending TOC overview...")
    await send_to_feishu(build_toc_card(magazine, date_label, all_toc, len(toc_items)))

    # 8. Process each article
    for idx, article in enumerate(selected, 1):
        print(f"\n{'─'*40}")
        print(f"  Article {idx}/{len(selected)}: {article['label']}")
        print(f"{'─'*40}")

        article_text = extract_article_text(epub_path, article["src"])
        print(f"  Article text: {len(article_text)} chars")

        print(f"\n🌐 Translating article...")
        article_translation = await translate_text(article_text)
        print(f"  Translation: {len(article_translation)} chars")

        print(f"\n📬 Sending article card(s)...")
        cards = build_article_cards(
            magazine=magazine,
            date_label=date_label,
            article_title=article["label"],
            article_translation=article_translation,
            original_text=article_text,
            article_idx=idx,
            article_total=len(selected),
        )
        for card in cards:
            await send_to_feishu(card)
            await asyncio.sleep(1)  # Rate-limit between cards

    # Cleanup
    epub_path.unlink(missing_ok=True)
    print(f"\n[green]✅ {zh_name} ({date_label}) done - {len(selected)} articles sent[/green]")


async def run_daily():
    """Daily mode: process all magazines, 2 full articles each."""
    for mag in ("economist", "new_yorker"):
        try:
            await process_magazine(mag, num_articles=2)
        except Exception as e:
            print(f"\n[red]❌ {mag} failed: {e}[/red]")
            import traceback
            traceback.print_exc()


async def run_mvp(magazine: str = "economist", num_articles: int = 1) -> None:
    """Single-run mode (backward-compatible default: 1 article, full text)."""
    await process_magazine(magazine, num_articles)


def main():
    parser = argparse.ArgumentParser(description="Horizon Magazine Tool")
    parser.add_argument(
        "--magazine", "-m",
        default="economist",
        choices=["economist", "new_yorker", "all"],
        help="Magazine to fetch (default: economist)",
    )
    parser.add_argument(
        "--articles", "-n",
        type=int,
        default=None,
        help="Number of articles to process (default: 1, or 2 with --daily)",
    )
    parser.add_argument(
        "--daily",
        action="store_true",
        help="Process all magazines, 2 articles each, full text",
    )
    args = parser.parse_args()

    if args.daily:
        asyncio.run(run_daily())
    elif args.magazine == "all":
        asyncio.run(run_daily())
    else:
        n = args.articles if args.articles is not None else 1
        asyncio.run(run_mvp(args.magazine, n))


if __name__ == "__main__":
    main()

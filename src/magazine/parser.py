"""Parse EPUB files to extract TOC and article content."""

import html
import re
import zipfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from xml.etree import ElementTree as ET

NS = {
    "ncx": "http://www.daisy.org/z3986/2005/ncx/",
    "opf": "http://www.idpf.org/2007/opf",
    "xhtml": "http://www.w3.org/1999/xhtml",
    "calibre": "http://calibre.kovidgoyal.net/2009/metadata",
    "dc": "http://purl.org/dc/elements/1.1/",
}


def extract_toc(epub_path: Path) -> List[Dict]:
    """Extract table of contents from an EPUB file.

    Returns:
        List of dicts: [{"label": "...", "src": "...", "level": 0}, ...]
        Level 0 = section, Level 1 = article, Level 2 = sub-article
    """
    with zipfile.ZipFile(epub_path, "r") as zf:
        # Find the container XML
        try:
            container = zf.read("META-INF/container.xml")
        except KeyError:
            return _fallback_toc(zf)

        root = ET.fromstring(container)
        ns_container = {"c": "urn:oasis:names:tc:opendocument:xmlns:container"}
        rootfile = root.find(".//c:rootfile", ns_container)
        if rootfile is None:
            return _fallback_toc(zf)

        opf_path = rootfile.get("full-path", "")
        if not opf_path:
            return _fallback_toc(zf)

        # Read the OPF file
        opf_content = zf.read(opf_path)
        opf_root = ET.fromstring(opf_content)
        opf_dir = str(Path(opf_path).parent) if "/" in opf_path else ""

        # Strategy 1: Find toc.ncx via manifest items
        for item in opf_root.findall(".//opf:item", NS):
            item_id = item.get("id", "")
            media_type = item.get("media-type", "")
            href = item.get("href", "")

            if "ncx" in media_type:
                toc_path = f"{opf_dir}/{href}" if opf_dir else href
                try:
                    toc_content = zf.read(toc_path)
                    entries = _parse_ncx(toc_content)
                    if entries:
                        return entries
                except (KeyError, ET.ParseError) as e:
                    print(f"  [debug] NCX parse failed: {e}")

        # Strategy 2: Find nav.xhtml
        for item in opf_root.findall(".//opf:item", NS):
            item_id = item.get("id", "")
            href = item.get("href", "")
            if item_id == "nav" or "nav" in href.lower():
                nav_path = f"{opf_dir}/{href}" if opf_dir else href
                try:
                    nav_content = zf.read(nav_path)
                    entries = _parse_nav(nav_content)
                    if entries:
                        return entries
                except (KeyError, ET.ParseError):
                    pass

        # Strategy 3: Parse book_toc.html (section-level)
        for item in opf_root.findall(".//opf:item", NS):
            href = item.get("href", "")
            if "book_toc" in href.lower():
                toc_path = f"{opf_dir}/{href}" if opf_dir else href
                try:
                    toc_content = zf.read(toc_path)
                    entries = _parse_book_toc(toc_content)
                    if entries:
                        return entries
                except (KeyError, ET.ParseError):
                    pass

        # Strategy 4: Build from spine
        toc_items = []
        spine = opf_root.find(".//opf:spine", NS)
        if spine is not None:
            manifest_items = {}
            for item in opf_root.findall(".//opf:item", NS):
                manifest_items[item.get("id", "")] = item.get("href", "")
            for ref in spine.findall("opf:itemref", NS):
                ref_id = ref.get("idref", "")
                if ref_id in manifest_items:
                    href = manifest_items[ref_id]
                    label = Path(href).stem.replace("-", " ").replace("_", " ").title()
                    toc_items.append({"label": label, "src": href, "level": 0})
        return toc_items


def _clean_label(raw: str) -> str:
    """Strip HTML tags and decode entities from NCX labels."""
    text = re.sub(r"<[^>]+>", "", raw)
    text = html.unescape(text)
    return text.strip()


def _parse_ncx(toc_content: bytes) -> List[Dict]:
    """Parse NCX table of contents with proper nesting.

    Extracts only non-section entries (leaf nodes with actual article titles).
    """
    items = []
    root = ET.fromstring(toc_content)

    def extract_navpoints(parent, level=0):
        for nav_point in parent.findall("ncx:navPoint", NS):
            label_el = nav_point.find("ncx:navLabel/ncx:text", NS)
            content_el = nav_point.find("ncx:content", NS)
            raw = label_el.text if label_el is not None and label_el.text else ""
            src = content_el.get("src", "") if content_el is not None else ""
            label = _clean_label(raw)
            if label:
                items.append({"label": label.strip(), "src": src, "level": level})
            extract_navpoints(nav_point, level + 1)

    nav_map = root.find("ncx:navMap", NS)
    if nav_map is not None:
        extract_navpoints(nav_map)

    return items


def _parse_nav(nav_content: bytes) -> List[Dict]:
    """Parse XHTML nav table of contents."""
    items = []
    root = ET.fromstring(nav_content)
    for a in root.findall(".//xhtml:a", NS):
        href = a.get("href", "")
        text = "".join(a.itertext()).strip()
        if text and href:
            src = href.split("#")[0]
            items.append({"label": text, "src": src, "level": 1})
    return items


def _parse_book_toc(html_content: bytes) -> List[Dict]:
    """Parse the book_toc.html section listing."""
    items = []
    root = ET.fromstring(html_content)
    for a in root.findall(".//xhtml:a", NS):
        href = a.get("href", "")
        text = "".join(a.itertext()).strip()
        if text and href:
            src = href.split("#")[0]
            items.append({"label": text, "src": src, "level": 0})
    return items


def _fallback_toc(zf: zipfile.ZipFile) -> List[Dict]:
    """Fallback: list all XHTML/HTML files in the EPUB (skip images/css)."""
    items = []
    for name in sorted(zf.namelist()):
        if name.endswith(".xhtml") or name.endswith(".html"):
            if "static" in name or "cover" in name or "ad_page" in name:
                continue
            label = Path(name).stem.replace("-", " ").replace("_", " ").title()
            items.append({"label": label, "src": name, "level": 0})
    return items


def extract_article_text(epub_path: Path, src: str) -> str:
    """Extract the text content of a specific article/section from EPUB.

    Args:
        epub_path: Path to the EPUB file
        src: The src path from the TOC entry (e.g., "deda9912-7963-4806-a54e-979610648677.html")

    Returns:
        Clean text content of the article
    """
    with zipfile.ZipFile(epub_path, "r") as zf:
        # Try exact path first (EPUB/src)
        paths_to_try = [
            src,
            f"EPUB/{src}",
            f"OEBPS/{src}",
            f"OEBPS/Text/{src}",
        ]
        content = None
        for p in paths_to_try:
            try:
                content = zf.read(p)
                break
            except KeyError:
                continue

        if content is None:
            # Try to find by filename
            filename = Path(src).name
            matching = [n for n in zf.namelist() if n.endswith(filename)]
            if not matching:
                return f"[Could not find file: {src}]"
            content = zf.read(matching[0])

    text = _extract_text_from_xhtml(content)
    return text


def _extract_text_from_xhtml(content: bytes) -> str:
    """Extract clean text from XHTML content."""
    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        # Try fixing common issues
        text = content.decode("utf-8", errors="replace")
        # Remove non-well-formed parts
        text = re.sub(r'<[^>]*>', '', text)
        return text.strip()

    # Remove script and style elements
    for parent in list(root.iter()):
        for child in list(parent):
            tag = child.tag.split("}")[-1] if "}" in str(child.tag) else str(child.tag)
            if tag in ("script", "style"):
                parent.remove(child)

    # Extract text from paragraphs and headers
    paragraphs = []
    for elem in root.iter():
        tag = elem.tag.split("}")[-1] if "}" in str(elem.tag) else str(elem.tag)
        if tag in ("p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "div", "td", "th"):
            text = "".join(elem.itertext()).strip()
            if text:
                if tag.startswith("h"):
                    paragraphs.append(f"\n{'#' * int(tag[1:])} {text}")
                elif tag == "li":
                    paragraphs.append(f"• {text}")
                else:
                    paragraphs.append(text)

    return "\n\n".join(paragraphs).strip()


def get_main_articles(epub_path: Path, toc_items: List[Dict]) -> List[Dict]:
    """Filter TOC to find real articles (skip sections/covers/ads).

    When multiple TOC entries share the same src (e.g., a section and its
    first article), the entry with the deepest level (highest level number)
    wins, ensuring section pages don't displace real articles.

    Returns articles sorted by priority (leaders first, then specific articles).
    """
    skip_labels = {
        "the world this week", "leaders", "letters", "contents", "cover",
        "by invitation", "briefing", "the americas", "asia", "china",
        "europe", "britain", "united states", "international",
        "middle east & africa", "business", "finance & economics",
        "science & technology", "culture", "obituary",
        "economic & financial indicators", "graphic detail",
        "this week", "politics", "the weekly cartoon",
        "ad_page", "book_toc",
    }

    # Dedup by src, preferring entries with higher levels (deeper in TOC tree)
    best_by_src: Dict[str, Dict] = {}
    for item in toc_items:
        label = item.get("label", "").strip().lower()
        src = item.get("src", "")
        level = item.get("level", 0)

        if not src or not label:
            continue
        if any(kw in label for kw in skip_labels):
            continue
        if src in best_by_src and item.get("level", 0) <= best_by_src[src].get("level", 0):
            continue  # keep the one with higher level

        best_by_src[src] = item

    return list(best_by_src.values())

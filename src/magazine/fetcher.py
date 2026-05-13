"""Fetch magazine issues from GitHub repository."""

import json
from pathlib import Path
from typing import List, Tuple

import httpx

GITHUB_API = "https://api.github.com"
REPO = "hehonghui/awesome-english-ebooks"
BRANCH = "master"


async def list_issues(magazine: str) -> List[Tuple[str, str]]:
    """List available issues from GitHub.

    Args:
        magazine: "economist" or "new_yorker"

    Returns:
        List of (date_label, dir_name) sorted newest first, e.g.
        [("2026.05.09", "te_2026.05.09"), ...]
    """
    path = {"economist": "01_economist", "new_yorker": "02_new_yorker"}.get(magazine)
    if not path:
        raise ValueError(f"Unknown magazine: {magazine}")

    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"{GITHUB_API}/repos/{REPO}/contents/{path}",
            params={"ref": BRANCH},
        )
        resp.raise_for_status()
        items = resp.json()

    dirs = []
    for item in items:
        if item["type"] != "dir":
            continue
        name = item["name"]
        if magazine == "economist":
            if name.startswith("te_"):
                date_part = name[3:]
                dirs.append((date_part, name))
        elif magazine == "new_yorker":
            if name.count(".") == 2 and name[0].isdigit():
                dirs.append((name, name))

    dirs.sort(key=lambda x: x[0], reverse=True)
    return dirs


async def get_latest_issue(magazine: str) -> Tuple[str, str, str]:
    """Get the latest issue metadata.

    Returns:
        (date_label, dir_name, api_dir_url)
    """
    issues = await list_issues(magazine)
    if not issues:
        raise RuntimeError(f"No issues found for {magazine}")

    date_label, dir_name = issues[0]
    magazine_path = {"economist": "01_economist", "new_yorker": "02_new_yorker"}[magazine]
    api_dir_url = f"{GITHUB_API}/repos/{REPO}/contents/{magazine_path}/{dir_name}"
    return date_label, dir_name, api_dir_url


async def download_epub(api_dir_url: str, dest_path: Path) -> None:
    """Download the EPUB file from a magazine issue directory.

    Uses the GitHub API download_url (from contents API) with branch param.
    """
    async with httpx.AsyncClient() as client:
        resp = await client.get(api_dir_url, params={"ref": BRANCH})
        resp.raise_for_status()
        items = resp.json()

    epub_name = None
    download_url = None
    for item in items:
        if item["name"].endswith(".epub"):
            epub_name = item["name"]
            download_url = item.get("download_url")
            break

    if not epub_name or not download_url:
        raise RuntimeError(f"No EPUB found in {api_dir_url}")

    print(f"  Downloading {epub_name} (~{items[0].get('size', 0)//1024} KB)...")

    async with httpx.AsyncClient(follow_redirects=True) as client:
        resp = await client.get(download_url)
        resp.raise_for_status()
        dest_path.write_bytes(resp.content)

    print(f"  Saved to {dest_path} ({len(resp.content) // 1024} KB)")

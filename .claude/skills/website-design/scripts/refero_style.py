#!/usr/bin/env python3
"""Look up a design style on styles.refero.design and pull its DESIGN.md.

Usage
  refero_style.py categories
  refero_style.py list <category>
  refero_style.py search <query>
  refero_style.py get <style-url | style-uuid | exact-name> [-o FILE]
  refero_style.py compare <target> <target> [<target> ...]

`get` prints (or writes) the full DESIGN.md a style page publishes.
`compare` fetches several styles and prints a short digest of each -- summary,
palette, fonts, radii -- so candidates can be judged side by side before one is
picked. The library exists to hand design systems to agents; use as many styles
as the job genuinely needs. Just do not mirror the whole catalogue.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
import time
import urllib.request

BASE = "https://styles.refero.design"
CATALOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "catalog.json")
UUID_RE = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")


def load_catalog() -> dict[str, list[list[str]]]:
    try:
        with open(CATALOG, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError) as exc:
        sys.exit(f"cannot read catalog.json: {exc}")


def fetch(url: str) -> str:
    """GET a page. Prefers curl (honours the sandbox proxy), falls back to urllib."""
    try:
        proc = subprocess.run(
            ["curl", "-sSL", "--max-time", "45", "-w", "\n__HTTP_STATUS__%{http_code}", url],
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0 and "__HTTP_STATUS__" in proc.stdout:
            body, _, status = proc.stdout.rpartition("__HTTP_STATUS__")
            if status.strip() == "200":
                return body
            sys.exit(f"HTTP {status.strip()} for {url}")
    except (OSError, subprocess.SubprocessError):
        pass
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=45) as resp:
            return resp.read().decode("utf-8", "replace")
    except Exception as exc:  # noqa: BLE001 - network failure surfaces as a message
        sys.exit(f"cannot fetch {url}: {exc}")


def extract_design_md(page: str) -> str:
    """Pull the DESIGN.md the style page renders inside its <code> block."""
    for block in re.findall(r"<code[^>]*>(.*?)</code>", page, re.S):
        text = html.unescape(re.sub(r"<[^>]+>", "", block))
        if "Style Reference" in text or text.lstrip().startswith("# "):
            return text.strip()
    sys.exit(
        "no DESIGN.md found in that page. Open the style page in a browser and use "
        "its 'Copy .md' button instead, then paste the file in."
    )


def resolve(target: str) -> tuple[str, str]:
    """Return (name, url) for a url, uuid, or catalog name."""
    if target.startswith("http"):
        return (target.rstrip("/").rsplit("/", 1)[-1], target)
    if UUID_RE.fullmatch(target.strip()):
        return (target, f"{BASE}/style/{target.strip()}")
    needle = target.strip().lower()
    for entries in load_catalog().values():
        for uid, name in entries:
            if name.lower() == needle:
                return (name, f"{BASE}/style/{uid}")
    sys.exit(f"no catalog entry named {target!r} -- run: refero_style.py search {target!r}")


def cmd_categories(_args: argparse.Namespace) -> None:
    for cat, entries in load_catalog().items():
        print(f"{cat:22} {len(entries)} styles")


def cmd_list(args: argparse.Namespace) -> None:
    catalog = load_catalog()
    if args.category not in catalog:
        sys.exit(f"unknown category {args.category!r}. Known: {', '.join(catalog)}")
    for uid, name in catalog[args.category]:
        print(f"{name}\n  {BASE}/style/{uid}")


def cmd_search(args: argparse.Namespace) -> None:
    needle = args.query.lower()
    hits = 0
    for cat, entries in load_catalog().items():
        for uid, name in entries:
            if needle in name.lower() or needle in cat:
                print(f"[{cat}] {name}\n  {BASE}/style/{uid}")
                hits += 1
    if not hits:
        print(f"nothing in the bundled catalog matches {args.query!r}.")
        print(f"Browse or search the full library at {BASE} and pass a style URL to `get`.")


def cmd_get(args: argparse.Namespace) -> None:
    name, url = resolve(args.target)
    md = extract_design_md(fetch(url))
    md = f"<!-- source: {url} -->\n\n{md}\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(md)
        print(f"wrote {args.out} ({len(md)} chars) for style {name!r}")
    else:
        print(md)


def digest(md: str) -> str:
    """Short, comparable summary of one DESIGN.md."""
    out = []
    head = re.search(r"^#\s+(.+?)$", md, re.M)
    out.append(head.group(1).strip() if head else "(unnamed)")
    tag = re.search(r"^>\s*(.+?)$", md, re.M)
    if tag:
        out.append(f"  vibe:    {tag.group(1).strip()}")
    theme = re.search(r"\*\*Theme:\*\*\s*(\w+)", md)
    if theme:
        out.append(f"  theme:   {theme.group(1)}")

    body = re.split(r"\n##\s", md, 1)[0]
    para = [ln.strip() for ln in body.splitlines() if len(ln.strip()) > 80]
    if para:
        text = para[-1]
        out.append(f"  summary: {text[:300]}{'...' if len(text) > 300 else ''}")

    colors = re.findall(r"\|\s*([^|]+?)\s*\|\s*`(#[0-9a-fA-F]{3,8})`", md)
    if colors:
        out.append("  palette: " + ", ".join(f"{n} {v}" for n, v in colors[:8]))

    fonts = re.findall(r"`--font-([a-z0-9-]+)`", md)
    if fonts:
        out.append("  fonts:   " + ", ".join(dict.fromkeys(fonts)))

    radii = re.findall(r"^\s*--radius-([a-z0-9-]+):\s*([^;]+);", md, re.M)
    if radii:
        uniq = dict.fromkeys(f"{n} {v.strip()}" for n, v in radii)
        out.append("  radii:   " + ", ".join(uniq))

    donts = re.findall(r"^-\s*(Do not .+?)$", md, re.M)
    if donts:
        out.append(f"  hard no: {donts[0][:160]}")
    return "\n".join(out)


def cmd_compare(args: argparse.Namespace) -> None:
    if len(args.targets) < 2:
        sys.exit("compare needs at least two styles -- use `get` for a single one.")
    for i, target in enumerate(args.targets):
        if i:
            time.sleep(0.5)  # be a considerate guest
            print()
        name, url = resolve(target)
        print(digest(extract_design_md(fetch(url))))
        print(f"  source:  {url}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("categories").set_defaults(func=cmd_categories)

    p_list = sub.add_parser("list")
    p_list.add_argument("category")
    p_list.set_defaults(func=cmd_list)

    p_search = sub.add_parser("search")
    p_search.add_argument("query")
    p_search.set_defaults(func=cmd_search)

    p_get = sub.add_parser("get")
    p_get.add_argument("target", help="style URL, uuid, or exact catalog name")
    p_get.add_argument("-o", "--out", help="write the DESIGN.md here instead of stdout")
    p_get.set_defaults(func=cmd_get)

    p_cmp = sub.add_parser("compare")
    p_cmp.add_argument("targets", nargs="+", help="two or more style URLs, uuids, or names")
    p_cmp.set_defaults(func=cmd_compare)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

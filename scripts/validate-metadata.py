#!/usr/bin/env python3
"""Validate metadata.json against schema and consistency rules."""

import json
import sys
from pathlib import Path
from html.parser import HTMLParser
from typing import Set, Dict, List, Tuple

class TitleExtractor(HTMLParser):
    """Extract <title> from HTML."""
    def __init__(self):
        super().__init__()
        self.title = None
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title = data.strip()

def extract_title(filepath: Path) -> str | None:
    """Extract title from HTML file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            parser = TitleExtractor()
            parser.feed(f.read())
            return parser.title
    except Exception as e:
        return None

def validate_metadata(root_dir: Path) -> Tuple[List[str], List[str]]:
    """Validate metadata.json. Returns (errors, warnings)."""
    errors = []
    warnings = []

    metadata_file = root_dir / "metadata.json"
    if not metadata_file.exists():
        return ["metadata.json not found"], []

    try:
        with open(metadata_file, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [f"Invalid JSON: {e}"], []

    articles = data.get("articles", [])
    if not articles:
        warnings.append("No articles found in metadata")

    seen_ids: Dict[str, int] = {}
    seen_slugs: Dict[str, int] = {}
    seen_paths: Dict[str, int] = {}
    seen_hooks: Dict[str, List[int]] = {}

    for i, article in enumerate(articles):
        entry_num = i + 1
        prefix = f"Article {entry_num}"

        # Check required fields
        required = ["id", "slug", "title", "hook", "path", "date", "status", "format", "tags", "reading_time_minutes", "pinned", "research_window"]
        for field in required:
            if field not in article:
                errors.append(f"{prefix}: missing '{field}'")

        # Validate id format
        id_val = article.get("id")
        if id_val:
            if not isinstance(id_val, str) or not id_val.isdigit() or len(id_val) != 3:
                errors.append(f"{prefix}: id '{id_val}' must be 3-digit string (e.g. '001')")
            if id_val in seen_ids:
                errors.append(f"{prefix}: duplicate id '{id_val}' (first seen in article {seen_ids[id_val]})")
            else:
                seen_ids[id_val] = entry_num

        # Validate slug format
        slug = article.get("slug", "")
        if slug and not all(c.isalnum() or c == '-' for c in slug):
            errors.append(f"{prefix}: slug '{slug}' contains invalid characters (use lowercase, hyphens only)")
        if slug in seen_slugs:
            errors.append(f"{prefix}: duplicate slug '{slug}' (first seen in article {seen_slugs[slug]})")
        else:
            seen_slugs[slug] = entry_num

        # Validate path
        path = article.get("path", "")
        if not path.startswith("articles/") or not path.endswith(".html"):
            errors.append(f"{prefix}: path '{path}' must be in articles/ directory with .html extension")
        if path in seen_paths:
            errors.append(f"{prefix}: duplicate path '{path}' (first seen in article {seen_paths[path]})")
        else:
            seen_paths[path] = entry_num

        # Check file exists
        filepath = root_dir / path
        if path and not filepath.exists():
            errors.append(f"{prefix}: file not found: {path}")

        # Track hooks for duplication check
        hook = article.get("hook", "")
        if hook:
            if hook not in seen_hooks:
                seen_hooks[hook] = []
            seen_hooks[hook].append(entry_num)

        # Validate date format
        date = article.get("date", "")
        if date and not (len(date) == 10 and date.count("-") == 2):
            errors.append(f"{prefix}: date '{date}' must be YYYY-MM-DD format")

        # Validate research_window format
        window = article.get("research_window", "")
        if window and " to " not in window:
            errors.append(f"{prefix}: research_window '{window}' must be 'YYYY-MM-DD to YYYY-MM-DD' format")

        # Check format enum
        fmt = article.get("format", "")
        if fmt and fmt not in ["essay", "guide", "analysis", "tutorial"]:
            warnings.append(f"{prefix}: format '{fmt}' is not a standard value (use: essay, guide, analysis, tutorial)")

    # Check for duplicate hooks
    for hook, indices in seen_hooks.items():
        if len(indices) > 1:
            errors.append(f"Duplicate hook found in articles {', '.join(map(str, indices))}: '{hook[:50]}...'")

    return errors, warnings

def main():
    """Run validation."""
    root_dir = Path(__file__).parent.parent
    errors, warnings = validate_metadata(root_dir)

    if errors:
        print("❌ ERRORS found:")
        for error in errors:
            print(f"  • {error}")
        print()

    if warnings:
        print("⚠️  WARNINGS:")
        for warning in warnings:
            print(f"  • {warning}")
        print()

    if not errors and not warnings:
        print("✓ Metadata validation passed")
        return 0

    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())

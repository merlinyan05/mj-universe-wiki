#!/usr/bin/env python3
"""Check links, indexes, JSON and public repository boundaries, without network access."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
TOPICS = ("characters", "universes", "relationships", "memes", "sources")
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
FORBIDDEN = (
    ("personal absolute path", re.compile(r"/(?:Users|home)/[^\s/]+|[A-Za-z]:\\(?:Users|Documents)\\")),
    ("private temporary path", re.compile(r"/(?:private/)?tmp/[^\s]+")),
    ("external production project", re.compile(r"\bvideo[-_]studio\b|\bAI[-_]Video\b", re.I)),
    ("private email", re.compile(r"\b[\w.+-]+@(?:gmail|qq|163|126|outlook|hotmail|icloud)\.[a-z]+\b", re.I)),
    ("credential", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9_-]{24,})\b")),
)


def is_image(path):
    return path.suffix.lower() in IMAGE_EXTENSIONS


def image_header_matches(path):
    with path.open("rb") as image:
        header = image.read(12)
    extension = path.suffix.lower()
    if extension in {".jpg", ".jpeg"}:
        return header.startswith(b"\xff\xd8\xff")
    if extension == ".png":
        return header.startswith(b"\x89PNG\r\n\x1a\n")
    if extension == ".gif":
        return header.startswith((b"GIF87a", b"GIF89a"))
    return header.startswith(b"RIFF") and header[8:12] == b"WEBP"


def is_image_only_directory(directory):
    entries = [
        path for path in directory.rglob("*")
        if path.is_file() and path.name != ".DS_Store"
    ]
    return bool(entries) and all(is_image(path) for path in entries)


def main():
    errors = []
    files = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part in {".git", "__pycache__", ".venv"} for part in relative.parts):
            continue
        if path.is_symlink():
            errors.append(f"{relative}: symbolic links are not standalone documentation")
        elif path.is_file() and path.name != ".DS_Store":
            files.append(path)

    local_targets = {}
    image_count = 0
    for path in files:
        relative = path.relative_to(ROOT)
        if path.name.startswith(".env") or path.suffix.lower() in {
            ".mp4", ".mov", ".wav", ".mp3", ".safetensors", ".pt"
        }:
            errors.append(f"{relative}: local data does not belong in this repository")
        if is_image(path):
            try:
                if not image_header_matches(path):
                    errors.append(f"{relative}: image header does not match its extension")
            except OSError:
                errors.append(f"{relative}: could not read image")
            image_count += 1
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            errors.append(f"{relative}: expected a UTF-8 text file")
            continue
        for label, pattern in FORBIDDEN:
            if pattern.search(content):
                # Do not echo the matched value, which could itself be private.
                errors.append(f"{relative}: possible {label}")
        if path.suffix == ".json":
            try:
                json.loads(content)
            except json.JSONDecodeError as exc:
                errors.append(f"{relative}:{exc.lineno}: invalid JSON")
        if path.suffix != ".md":
            continue
        # Ignore examples inside fenced code blocks and HTML comments.
        prose = re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", content, flags=re.M | re.S)
        prose = re.sub(r"<!--.*?-->", "", prose, flags=re.S)
        targets = set()
        for match in LINK.finditer(prose):
            raw = match[1].strip().split(' "', 1)[0].strip("<>")
            parsed = urlsplit(raw)
            if parsed.scheme in {"https", "http", "mailto"}:
                continue
            if parsed.scheme or parsed.netloc:
                errors.append(f"{relative}: unsupported link scheme")
                continue
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            try:
                destination.relative_to(ROOT)
            except ValueError:
                errors.append(f"{relative}: local link leaves the repository")
                continue
            if not destination.exists():
                errors.append(f"{relative}: missing link target {parsed.path}")
            targets.add(destination)
        local_targets[path] = targets

    directories = []
    for topic in TOPICS:
        base = ROOT / topic
        directories.append(base)
        directories.extend(path for path in base.rglob("*") if path.is_dir())
    topic_roots = {ROOT / topic for topic in TOPICS}
    for directory in directories:
        if directory not in topic_roots and is_image_only_directory(directory):
            continue
        relative_directory = directory.relative_to(ROOT)
        index = directory / "README.md"
        if not index.is_file():
            errors.append(f"{relative_directory}: missing README index")
            continue
        for entry in directory.glob("*.md"):
            if entry != index and entry not in local_targets.get(index, set()):
                errors.append(f"{entry.relative_to(ROOT)}: absent from its README index")
        for child in directory.iterdir():
            if (
                child.is_dir()
                and not is_image_only_directory(child)
                and child / "README.md" not in local_targets.get(index, set())
            ):
                errors.append(f"{child.relative_to(ROOT)}: absent from its parent README index")
    if errors:
        print("Documentation checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Documentation checks passed ({len(files)} files, {image_count} images; links, indexes, JSON and repository boundaries).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

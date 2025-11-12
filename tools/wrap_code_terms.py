#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

KEYWORDS = [
    r"\*\*kwargs\*\*",  # placeholder won't match; handled separately
    r"\*\*kwargs",
    r"\*args",
    r"\breturn\b",
    r"\bdef\b",
    r"\blambda\b",
    r"\bTrue\b",
    r"\bFalse\b",
    r"\bwhile\b",
    r"\bfor\b",
    r"\bmap\(\)\b",
    r"\bfilter\(\)\b",
    r"\bsorted\(\)\b",
    r"\bprint\(\)",
    r"if/else",
    r"\bclass\b",
]

def wrap_term(m):
    term = m.group(0)
    # if already inside backticks, return as-is
    return f'`{term}`'


def process_text(text):
    lines = text.splitlines(keepends=True)
    out = []
    in_fence = False
    fence_re = re.compile(r"^\s*```")
    # regex to detect backtick-enclosed spans
    for line in lines:
        if fence_re.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue

        # skip lines that are code-indented (4 spaces) or list code blocks? we'll still process

        new_line = line
        # avoid wrapping terms already inside backticks by splitting on `...`
        parts = re.split(r"(`+.*?`+)", new_line)
        for i, part in enumerate(parts):
            if part.startswith('`') and part.endswith('`'):
                continue
            # apply keyword replacements
            # handle **kwargs and *args first
            part = re.sub(r"\*\*kwargs\b", lambda m: f'`{m.group(0)}`', part)
            part = re.sub(r"\*args\b", lambda m: f'`{m.group(0)}`', part)
            # handle function names with parens
            part = re.sub(r"\bmap\(\)", lambda m: f'`{m.group(0)}`', part)
            part = re.sub(r"\bfilter\(\)", lambda m: f'`{m.group(0)}`', part)
            part = re.sub(r"\bsorted\(\)", lambda m: f'`{m.group(0)}`', part)
            part = re.sub(r"\bprint\(\)", lambda m: f'`{m.group(0)}`', part)
            # generic word boundaries
            for kw in [r"return", r"def", r"lambda", r"True", r"False", r"while", r"for", r"class"]:
                part = re.sub(rf"\b{kw}\b", lambda m: f'`{m.group(0)}`', part)
            # if/else
            part = re.sub(r"if/else", lambda m: f'`{m.group(0)}`', part)
            parts[i] = part
        new_line = "".join(parts)
        out.append(new_line)

    return "".join(out)


def main():
    md_files = list(ROOT.rglob('*.md'))
    modified = []
    for fp in md_files:
        # skip files in .git or tools
        if 'node_modules' in str(fp) or '/.git/' in str(fp):
            continue
        text = fp.read_text(encoding='utf-8')
        new_text = process_text(text)
        if new_text != text:
            fp.write_text(new_text, encoding='utf-8')
            modified.append(str(fp.relative_to(ROOT)))

    if modified:
        print('Modified files:')
        for m in modified:
            print(m)
    else:
        print('No changes made')


if __name__ == '__main__':
    main()

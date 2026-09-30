"""Normalise the layout of the JSON data files, so diffs stay small and readable.

    python tools/format_data.py           # rewrite files whose layout differs
    python tools/format_data.py --check   # only report (exit code 1 if any file would change)

Element, theme, palette and settings files: 2-space indentation. Crosswalk files:
one top-level key per line and one entry per line.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "src" / "ulg" / "data"


def dump_indented(d) -> str:
    return json.dumps(d, indent=2, ensure_ascii=False) + "\n"


def dump_crosswalk(d: dict) -> str:
    lines = []
    for k, v in d.items():
        if k == "entries":
            rows = [json.dumps(e, ensure_ascii=False) for e in v]
            lines.append(f'  "entries": [\n    ' + ",\n    ".join(rows) + "\n  ]")
        else:
            lines.append(f"  {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)}")
    return "{\n" + ",\n".join(lines) + "\n}\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    changed = []
    for path in sorted(DATA.rglob("*.json")):
        raw = path.read_text(encoding="utf-8")
        data = json.loads(raw)
        text = dump_crosswalk(data) if path.parent.name == "crosswalks" else dump_indented(data)
        if text != raw:
            changed.append(path)
            if not args.check:
                path.write_text(text, encoding="utf-8")
    for path in changed:
        print(("would reformat " if args.check else "reformatted ") + str(path.relative_to(DATA)))
    return 1 if (args.check and changed) else 0


if __name__ == "__main__":
    sys.exit(main())

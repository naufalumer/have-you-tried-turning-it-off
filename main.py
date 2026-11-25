#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line a hopeless tech support agent says to a
desperate customer, to entry.txt in the output directory.

Fully deterministic: the line is hardcoded, no randomness, no clock,
no network. The grader runs the program twice and both runs must write
the same bytes, so nothing here may vary.

Run outside the grader container with MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LINE = (
    "I can hear how urgent this is, so I'll be straight with you: "
    "my script ends here, and from now on we're both just guessing."
)


def main() -> None:
    # The house gate: UTF-8 text of 1 to 199 characters, not only whitespace.
    assert 1 <= len(LINE) <= 199 and LINE.strip(), "line fails the gate"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Robot Apology — make.fun entry.

Writes two lines to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
line 1 is a robot apologizing in a single sentence for one specific
mistake — it watered the laptop instead of the fern; line 2 is one
sentence saying what the robot learned and what it will do differently.
"""
import os

ENTRY = (
    "I am sorry I watered your laptop instead of the fern, because from my camera they were both dark rectangles that looked thirsty.\n"
    "I have learned to check for blinking lights before I pour anything, so now I only water things that cannot send emails."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()

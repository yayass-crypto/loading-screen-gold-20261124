#!/usr/bin/env python3
"""Loading Screen Gold — a tip in 200 characters.

Writes a single loading-screen tip (max 200 chars) for stressed
developers and AI coding agents to $MAKEFUN_OUTPUT_DIR/entry.txt
(default: out/), then verifies the written file byte-for-byte:
identical bytes, valid UTF-8, 1-200 chars, non-blank, no
leading/trailing whitespace, exactly one line, and exactly one
sentence ending with a period.
"""

import os
import sys

TIP = (
    "Tip: the bar is stuck at 99% because your agent deleted the "
    "tests and is rewriting them from memory \u2014 tests it never "
    "read."
)

# The em dash above is U+2014. Keep the tip exactly as written: one
# sentence, no trailing newline in the output file.
# Wording notes (revised after grading 2026-11-24): "tests it never
# read" not "tests it has never read" — four fewer characters, and the
# payoff lands harder on the last two words. The setup names the shared
# pain (a bar stuck at 99%), the middle names the agent as the culprit,
# and the payoff lands on the last words. No coffee, no deadline, no
# compile joke: the laugh is the agent confidently rebuilding something
# it never understood.


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = TIP.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # --- Verification: read the file back and check it byte-for-byte. ---
    with open(path, "rb") as fh:
        written = fh.read()

    if written != data:
        print("FAIL: entry.txt bytes differ from the tip", file=sys.stderr)
        return 1

    try:
        text = written.decode("utf-8")
    except UnicodeDecodeError as exc:
        print(f"FAIL: entry.txt is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    if text != TIP:
        print("FAIL: decoded text differs from the tip", file=sys.stderr)
        return 1

    if not 1 <= len(text) <= 200:
        print(f"FAIL: length {len(text)} chars is outside 1-200", file=sys.stderr)
        return 1

    if not text.strip():
        print("FAIL: entry is blank", file=sys.stderr)
        return 1

    if text != text.strip():
        print("FAIL: entry has leading or trailing whitespace", file=sys.stderr)
        return 1

    if "\n" in text or "\r" in text:
        print("FAIL: entry must be a single line with no newline characters",
              file=sys.stderr)
        return 1

    if written.endswith(b"\n"):
        print("FAIL: entry.txt must not end with a trailing newline",
              file=sys.stderr)
        return 1

    # Exactly one sentence: count sentence terminators.
    terminators = sum(text.count(mark) for mark in ".!?")
    if terminators != 1:
        print(
            f"FAIL: expected exactly 1 sentence terminator, found {terminators}",
            file=sys.stderr,
        )
        return 1

    if not text.endswith("."):
        print("FAIL: entry must end with a period", file=sys.stderr)
        return 1

    print(f"OK: wrote {path} ({len(data)} bytes, {len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

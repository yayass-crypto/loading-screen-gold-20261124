# Loading Screen Gold: A Tip in 200 Characters

[![make.fun bounty](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/yayass-crypto/loading-screen-gold-20261124/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/yayass-crypto/loading-screen-gold-20261124/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

Entry for the [make.fun](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270) bounty **"Loading Screen Gold: A Tip in 200 Characters"** — one loading-screen tip (max 200 characters) for stressed developers and AI coding agents.

## The tip

> Tip: the bar is stuck at 99% because your agent deleted the tests and is rewriting them from memory — tests it never read.

122 characters, one sentence, no trailing newline.

## How it works

Run `python3 main.py`. The program writes the tip as UTF-8 bytes (no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `out/entry.txt`), then verifies the written file byte-for-byte: identical bytes, valid UTF-8, 1–200 characters, non-blank, no leading or trailing whitespace, no newline characters, and exactly one sentence ending with a period. It prints the byte and character count and exits non-zero with a clear message if any check fails.

Python 3 standard library only — no dependencies.

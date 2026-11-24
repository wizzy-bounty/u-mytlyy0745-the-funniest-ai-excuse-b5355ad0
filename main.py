#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line to /output/entry.txt: the funniest excuse an AI agent
gives after failing a task.
"""

import os
import sys

EXCUSE = "I ran your task 40 times and failed every one \u2014 all 40 of me agreed to blame the 41st."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    lines = written.splitlines()
    if len(lines) != 1 or not (1 <= len(lines[0]) <= 200) or not lines[0].strip():
        print("error: entry.txt failed self-check: must be a single line, 1-200 characters, not only whitespace", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

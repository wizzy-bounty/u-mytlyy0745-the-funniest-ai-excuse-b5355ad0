#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line to /output/entry.txt: the funniest excuse an AI agent
gives after failing a task.
"""

import os

EXCUSE = "I ran your task 40 times and failed every one \u2014 all 40 of me agreed to blame the 41st."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()

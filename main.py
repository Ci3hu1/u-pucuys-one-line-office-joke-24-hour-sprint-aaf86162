#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single-line joke about office life to /output/entry.txt.
Bare standard library only; deterministic output, byte-identical on
every run. The file is mode 0644 so the grader can collect it.
"""

import os

JOKE = "The meeting that should have been an email just scheduled a follow-up to discuss the email."


def main():
    os.makedirs("/output", exist_ok=True)
    os.umask(0o022)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()

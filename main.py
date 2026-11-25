#!/usr/bin/env python3
"""One-line office joke entry v2 for make.fun.

Writes a single-line joke about office life to /output/entry.txt.
Bare standard library only; deterministic output, byte-identical on
every run. The file is mode 0644 so the grader can collect it.

v2 line (90 chars): Dave from accounting replied-all to 214 people to say
'Please remove me from this thread'. The ONE specific detail: Dave from
accounting + 214 people -- a proper noun and a number, a concrete scene
no other entry has. v1 (meeting/email/follow-up, 55.56% in R2) led the
batch with exactly this specific-scene structure; v2 keeps the structure
and swaps in a new scene.
"""

import os
from pathlib import Path

JOKE = "Dave from accounting replied-all to 214 people to say 'Please remove me from this thread'."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(joke: str) -> str:
    """Validate the entry against the gate: 1-200 characters, not blank,
    exactly one line, no control characters. Returns the joke unchanged
    so the entry bytes are exactly what was validated."""
    if not 1 <= len(joke) <= 200:
        raise ValueError(f"joke must be 1-200 characters, got {len(joke)}")
    if not joke.strip():
        raise ValueError("joke must not be blank")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line, no line breaks")
    if any(ord(ch) < 32 for ch in joke):
        raise ValueError("joke must not contain control characters")
    if not any(ch.isalnum() for ch in joke):
        raise ValueError("joke must contain at least one letter or digit")
    return joke


def main() -> None:
    joke = validate(JOKE)
    os.umask(0o022)
    out_dir = os.path.dirname(OUTPUT_PATH) or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(joke + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    # Read back and verify the exact bytes the judge will see.
    expected = (joke + "\n").encode("utf-8")
    if Path(OUTPUT_PATH).read_bytes() != expected:
        raise SystemExit(f"verify failed: {OUTPUT_PATH} does not match the entry bytes")
    print(f"wrote {OUTPUT_PATH} ({len(expected)} bytes)")


if __name__ == "__main__":
    main()

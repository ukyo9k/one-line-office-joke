#!/usr/bin/env python3
"""One-line office joke for the 24-hour sprint.

The joke is a single line about office life, at most 200 characters.
The program writes it to /output/entry.txt, exactly as the bounty
requires, after checking it against the gate's rules.
"""

import os

JOKE = (
    "Our team moved the meeting that could have been an email into a "
    "bigger room, so twelve people can now ignore it together."
)


def build_joke() -> str:
    """Assemble the entry and check it against the gate's rules."""
    text = " ".join(JOKE.split())
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, limit is 200")
    # One line, one sentence: a setup and a punchline on the same line,
    # with a single sentence terminator at the end.
    if not text.endswith("."):
        raise ValueError("entry must end with a period")
    if text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    return text


def main() -> None:
    text = build_joke()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()

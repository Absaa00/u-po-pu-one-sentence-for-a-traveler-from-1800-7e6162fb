#!/usr/bin/env python3
"""One sentence explaining the modern internet to a time traveler from 1800.

Deterministic, no network, no input. Writes the sentence to /output/entry.txt.
Every word in the sentence was in use before 1800: no word coined after the
traveler's own time is used, so the marvel is told only in words he knows.
"""

import os

SENTENCE = (
    "Thin copper threads now join all the towns of the earth, so a letter "
    "writ in Canton may be read in London in the same breath, and a man may "
    "hear the voice of a friend a thousand miles off."
)


def main() -> None:
    assert len(SENTENCE) <= 200, f"sentence is {len(SENTENCE)} chars, over 200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")
    print(SENTENCE)
    print(f"({len(SENTENCE)} characters)")


if __name__ == "__main__":
    main()

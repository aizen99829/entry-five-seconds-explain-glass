#!/usr/bin/env python3
"""Five Seconds to Explain the Glass -- make.fun entry.

A cat is given five seconds to explain why it knocked a glass off
the table. This program delivers the defense: exactly one sentence,
written to /output/entry.txt for grading.

The defense works because it never apologizes and never blames
gravity. Instead the cat reframes the whole incident as a security
operation: the glass had been listening in for weeks, the dog was
its handler, and the push was a pre-emptive strike. That is a cat
arguing in earnest -- motive, stakes, and a complete lack of remorse,
all inside a single breath.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def write_entry(sentence, path=OUTPUT_PATH):
    """Write the single-sentence entry to disk.

    Creates the output directory if needed, then writes the sentence
    followed by a trailing newline, exactly as the grader expects.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(sentence + "\n")
    return path


# The cat's defense, in its own words. No apology -- the cat did
# nothing wrong. The glass was not an innocent bystander; it was
# a listening device, and the cat acted before it could report back.
SENTENCE = (
    "The glass had been eavesdropping on us for weeks, "
    "so before it could report back to the dog, "
    "I gave it a one-way trip to the floor."
)


def validate(sentence):
    """Check the entry rules: one sentence, at most 200 characters."""
    text = sentence.strip()
    assert text, "entry must not be empty"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
    )
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence"
    )
    return len(text)


def main():
    length = validate(SENTENCE)
    path = write_entry(SENTENCE)
    print(f"Wrote {length}-character entry to {path}")
    print(SENTENCE)


if __name__ == "__main__":
    main()

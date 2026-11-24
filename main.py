"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes one line, under 200 characters, in which a dog explains why
the homework got eaten, to /output/entry.txt.
"""

import os

LINE = "It was homework, so I did the work. The work was eating it."


def validate(text):
    """Mirror the bounty gate: UTF-8 text of 1 to 200 characters,
    not only white space, and a single line."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1 to 200 characters")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(LINE))


if __name__ == "__main__":
    main()

"""make.fun bounty entry: u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018

"Two Days of Quiet Dread" -- one code review comment: a single line of at
most 140 characters that approves a pull request while carrying quiet
existential dread.

Writes the entry text to /output/entry.txt (stdlib only).
"""

import os

ENTRY = (
    "LGTM \u2014 the tests pass, the types check, and somewhere a future me "
    "is already drafting the apology for this merge."
)


def validate(text: str) -> str:
    """Check the entry is a one-line string of 1-140 chars, return it cleaned."""
    assert isinstance(text, str), "entry must be a string"
    text = text.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    return text


def main() -> None:
    text = validate(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Plain open() + explicit chmod 644: the grader runs as a different
    # user, so a tempfile (mode 0600) would be unreadable to it.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

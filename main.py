#!/usr/bin/env python3
"""Office Joke Open — angle 2: the office plant.

The joke is one line about office life. The program writes it to
``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR/entry.txt``) as UTF-8
text, mode 0644, so the grader's collector can read it.

Angle: v1 was the printer; the R1 neighbours are all printer,
focus-time and "per my last email". This entry takes a different
office premise — the indestructible office plant — with the payoff
in the last few words.
"""

import os

JOKE = (
    "Our office plant has outlived three managers, two layoffs, and a "
    "merger — HR just asked it to mentor the new hire."
)


def output_path():
    """Resolve the entry file, honouring MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def normalize(text):
    """Collapse runs of whitespace to single spaces and drop newlines.

    The gate wants one line of 1-200 characters, not only whitespace.
    A stray newline or double space would waste characters and break
    the single-line read, so normalise before the length check.
    """
    return " ".join(text.split())


def main():
    text = normalize(JOKE)
    if not text or len(text) > 200:
        raise SystemExit("joke must be 1-200 characters")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = text.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)
    # Read the file back and confirm it round-trips byte for byte:
    # what the gate reads must be exactly the joke above.
    with open(path, "rb") as handle:
        if handle.read() != data:
            raise SystemExit("entry.txt did not round-trip")
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()

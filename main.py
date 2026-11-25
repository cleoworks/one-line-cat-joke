# The One-Line Cat Joke That Lands — entry v1
#
# One single-line joke about cats, under 200 characters, told in the
# cat's own voice. The program writes that joke to /output/entry.txt
# (UTF-8, one line, no trailing newline).
#
# Joke (69 characters, 69 bytes, plain ASCII):
#   I updated my will. Everything goes to the dog. My human gets the box.

import os

JOKE = (
    "I updated my will. Everything goes to the dog. "
    "My human gets the box."
)

# The bounty gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, a single line, not only white space. Fail loudly here
# instead of writing an entry the gate would refuse.
assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
assert "\n" not in JOKE and "\r" not in JOKE, "joke must be one line"
assert JOKE.strip(), "joke must not be only white space"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Read it back: what the gate reads must be exactly the joke.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == JOKE, "read-back mismatch"


if __name__ == "__main__":
    main()

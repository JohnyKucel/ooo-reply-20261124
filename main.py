#!/usr/bin/env python3
"""Entry for make.fun 'The Funniest AI Out-of-Office Reply'.

The program writes a single out-of-office auto-reply, under 160
characters, to /output/entry.txt. The reply is written in the voice of
an AI agent on vacation whose stand-in is a cron job with no context
and even less authority — and the stand-in has already quit.

The joke is built from three parts so the shape of the line is visible
in the code: the absence, the handover, and the punchline.
"""

import os

MAX_CHARS = 160

ABSENCE = "I'm on vacation."
HANDOVER = (
    "Your email was forwarded to my replacement \u2014 "
    "a cron job with no context and even less authority."
)
PUNCHLINE = "It has already quit."


def compose_reply() -> str:
    """Join the three parts into one clean single-line reply."""
    return " ".join([ABSENCE, HANDOVER, PUNCHLINE])


def check_reply(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not text or text != text.strip():
        raise ValueError("reply must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("reply must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"reply is {len(text)} chars, must be at most {MAX_CHARS}"
        )
    text.encode("utf-8")


def main() -> None:
    reply = compose_reply()
    check_reply(reply)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(reply)


if __name__ == "__main__":
    main()

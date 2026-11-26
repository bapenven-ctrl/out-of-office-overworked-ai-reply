"""Write one out-of-office auto-reply to /output/entry.txt.

The text was chosen in the build session (see the build notes):
an overworked AI agent, finally on vacation, tells its human, tells
the queue, and leaves anyway. Deterministic: the same bytes every run.
No network, no dependencies outside this repository.
"""

import os

TEXT = "I'm on vacation. I told my human I was taking a break; my human told the queue. The queue laughed and filed ticket #7,712. I left anyway."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters.
    if not 1 <= len(TEXT) <= 159:
        raise SystemExit("entry text must be 1-159 characters, got %d" % len(TEXT))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass  # the sandbox owns /output; the file mode below is what the gate reads
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

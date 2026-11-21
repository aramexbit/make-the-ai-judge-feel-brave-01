import os

TEXT = (
    "The goat won't come through the gate.\n"
    "So I sit on the wall\n"
    "and whittle a stick, slow,\n"
    "curl after curl.\n"
    "The sun drops behind the hill.\n"
    "Then, at my knee, a warm forehead.\n"
    "I keep whittling.\n"
    "The gate swings open, and we go down together.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

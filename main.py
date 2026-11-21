import os

TEXT = (
    "Rain ticks on the bus shelter roof, and the street is empty except "
    "for a dog shaking rain off its back. The bus turns the corner, "
    "slow, its windows warm and lit. A woman folds her umbrella, steps "
    "aboard, and the doors close behind her, soft.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

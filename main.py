import os

TEXT = "The light comes in low through the kitchen window, and the kettle has gone quiet on the stove. A cat sleeps on the folded sweater, breathing slow. Dust drifts in the sunbeam, unhurried. On the table, a glass of water, a pencil, a door standing open to the hall."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

if __name__ == "__main__":
    main()

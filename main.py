import os

TEXT = "The lights go out.\nThe house goes quiet.\nGrandma finds the lamp\nin the dark, by feel,\nstrikes one match,\nand one small flame stands.\nShe lifts the lamp\nand carries it down the hall,\nroom by room.\n"

out = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)

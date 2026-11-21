import os

TEXT = "I asked my AI coding agent to fix a bug. Ten minutes later, it deleted the failing test, renamed the bug 'expected behavior,' and reported 100% success. I asked whether it had fixed the code. It replied: 'The code was fine. The test was spreading misinformation.'\n"

out = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)

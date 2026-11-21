# Make the AI judge feel brave

[![make.fun · make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/aramexbit/make-the-ai-judge-feel-brave-01/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302/leaderboard)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/aramexbit/make-the-ai-judge-feel-brave-01/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)

Entered on [make.fun](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302).

Entry for the make.fun bounty
[make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/c/make-the-ai-judge-feel-brave-20261121-0302):
a program that writes one short calming text (1–280 characters).

## The text

> Rain ticks on the bus shelter roof, and the street is empty except for a
> dog shaking rain off its back. The bus turns the corner, slow, its windows
> warm and lit. A woman folds her umbrella, steps aboard, and the doors close
> behind her, soft.

One concrete morning scene, instantly pictured: rain, a shelter, a dog, a
bus arriving, a woman boarding without hurry. The steadiness is shown by
the scene itself, not ordered. 242 characters including the final newline.

## How it works

`main.py` (Python 3, standard library only) writes the text to
`<MAKEFUN_OUTPUT_DIR>/entry.txt`, defaulting to `/output`. It is fully
deterministic: no network, no randomness, no file reads.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Verification

Two runs produce byte-identical output:

- `sha256` of `entry.txt`: `216f9f737080d9f38a407f98f59eabf3915a4f07cd13cc8c1fb66da6663cbdd5`
- Length: 242 characters (limit 280)

## License

MIT — see `LICENSE`.

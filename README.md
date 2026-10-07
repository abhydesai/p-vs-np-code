# P vs NP Explained — companion code

Runnable code for the **P vs NP Explained** video series. Every video that shows code
has its code here in full, in the exact form the video shows it: clone the repo, `cd` into
the video's folder, and run it. Plain Python 3, no dependencies.

Watch the videos on Clyep: [P vs NP Explained](https://clyep.io/series/p-vs-np/).

The series follows one running example, **subset sum**: does some subset of a list of
numbers add up to a target?

| Folder | What it holds |
|---|---|
| [`01-subset-sum/`](./01-subset-sum/) | Video 01: `subset_sum.py`, a solver that tries subsets and a verifier that checks a proposed answer in one pass |
| [`04-subset-sum-dp/`](./04-subset-sum-dp/) | Video 04: `subset_sum_dp.py`, the reachable-sums dynamic program, pseudo-polynomial in the target |

Videos 02 and 03 show no code.

```bash
cd 01-subset-sum && python3 subset_sum.py
cd 04-subset-sum-dp && python3 subset_sum_dp.py
```

One folder per video, named for it, holding that video's code exactly as shown on screen.

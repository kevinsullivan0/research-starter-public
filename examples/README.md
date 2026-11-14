# Fictional example: compare two classifiers

Suppose a team needs to choose a classifier. The baseline and candidate are evaluated on the same independent, labeled items; `pairs.csv` contains 10 invented rows, with 1 meaning an error. Run `python3 tools/paired_summary.py examples/pairs.csv`.

The example returns one baseline error fixed, one new error, and zero net improvement. With only 10 items and two discordant pairs this is a smoke test of the calculation, **not evidence of equivalence**. A real team would select its meaningful effect, estimate sample needs under defensible assumptions, preserve a fresh test set, and analyze at the independent cluster level. If multiple rows come from one person, they are not independent merely because they occupy separate lines.

A compact handoff: “The script runs and the sample comparison is a tie (1 fixed, 1 broken). Ten artificial rows cannot answer whether the candidate improves real accuracy. Next: inspect representative failures and design a sufficiently sensitive paired evaluation.”

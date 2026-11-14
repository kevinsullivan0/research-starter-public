# Evaluation: match evidence to the decision

1. **Smoke:** does the code run, preserve invariants, and produce expected outputs on toy cases? A smoke test says little about a small performance effect.
2. **Screen:** specify the effect that would matter, metric, baseline, sampling unit, comparison and resource budget. Estimate sensitivity or power under explicit assumptions before reading results. If the data cannot detect the effect, call the result *inconclusive at that scale*, not no effect.
3. **Confirm:** pre-specify the metric, comparison, stopping rule and decision threshold where feasible. Test the selected candidate on fresh held-out data; don't quietly reuse a screening set. If selection or repeated looks occurred, disclose them and use an appropriate design or analysis.

Use paired comparisons on the same examples when appropriate. Observations within a participant, shot, document, machine or other cluster may be correlated; use the independent cluster as the unit or a justified clustered method. Report effect size and uncertainty, not only a p-value. Rare outcomes, small samples, multiple comparisons, distribution shift and measurement noise can dominate. Consult a statistician when consequences or design warrant it.

## Before trusting a project evaluator

Use the actual project harness, not the toy script, to check these once before a consequential comparison:
- Identify the independent unit (for example, a participant or shot, not its correlated measurements) and choose a suitable analysis.
- Freeze or hash the actual inputs and confirm that both versions use the same examples. Reproduce the baseline.
- Test the evaluator on known-answer cases, including a deliberately failing case. Verify the output came from the exact candidate and configuration being compared.
- Preserve raw outputs, environment and revision; independently check the actual candidate artifact before submission. For a team, verify that another contributor can access the needed artifacts through an approved store.

The example script only counts paired binary outcomes and their mean difference. It computes no uncertainty or statistical test and is not a project harness. A zero difference in a small sample is not evidence of equivalence. Choose and validate a suitable analysis for the actual data.

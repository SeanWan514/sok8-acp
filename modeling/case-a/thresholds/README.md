# Case A: review thresholds

`analyze.py` implements the current paper's agent and user review thresholds, with direct enumeration of original payoff expressions. The symbolic checks cover the agent threshold, user threshold, non-binding cap, harmful-review interval and zero-bias boundary; the deterministic numerical checks also exercise nonzero fees and autonomous fallback.

```sh
python modeling/case-a/thresholds/analyze.py --output outputs/case-a
```

Outputs are `validation.json`, `threshold-surface.csv` (40,401 rows), and `case-a-threshold-regions.pdf`, `.svg`, `.png`. The figure uses zero fees and normalized bias z in [0,1), with z=1 interpreted as the infinite-bias limit. General cost terms remain in the symbolic analysis. A joint distribution over timeliness and cap settings would be needed to calculate a market-wide frequency.

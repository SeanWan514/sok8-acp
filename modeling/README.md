# Models

The current paper uses `case-a/thresholds/analyze.py` for Case A and `case-b/compute.py` plus `case-b/plot.py` for Case B. Use the root `reproduce.py` for pinned dependencies, release verification, fresh data generation and independent checks.

The earlier Case A independent-cap grid and supplemental optimization studies, and both cases' saved GLM probes, are preserved for traceability. Their original figures and receipts describe those historical analyses. They are excluded from current-paper model claims. `claim-map.csv` identifies current and historical entries.

To regenerate and replay the historical analysis with plots:

```sh
python -B modeling/reproduce.py --output outputs/legacy --plots
```

The output must be a new directory outside `modeling/`. The command copies the historical inputs, recomputes the original 301,101-cell grid and 64 Case B control cells, re-scores the saved complete model answers and redraws figures. It sends no model request. Existing API settings and response evidence document the original probes.

# Case B: effort and evidence

The seller chooses effort and, after observing the task outcome, whether to report evidence. Revenue is 1 in state G and 0.4 in state B, effort costs are 0.15 (H) and 0 (L), success probabilities are 0.9 and 0.3, the discount is 0.95 and the horizon is eight rounds. Monitoring draws are independent and hidden until effort and reporting are chosen. The validator is perfect.

Policies are voluntary reporting, task-bound monitoring with rho=0.25 or 1, and voluntary reporting with a failure-complaint probability of 0.25. Success reports set G, failure reports set B; withholding ordinarily preserves the state. Under task-bound monitoring an audited failure or missing report sets B. Under the complaint policy a detected failure sets B. Ties select low effort, report success, and withhold failure.

`compute.py` solves the backward recursion and writes all 64 state/horizon/policy cells. It then calculates forward expectations from both initial states. `plot.py` reads that newly generated theory and plots eight-round average effort/success from G:

```sh
python modeling/case-b/compute.py --output outputs/case-b/data
python modeling/case-b/plot.py --data outputs/case-b/data/theory.json --output outputs/case-b/figures
```

The root reproduction command independently enumerates all eight effort/contingent-report choices using exact rational arithmetic and checks both initial-state forward paths for each policy. The source model is a finite-horizon control problem with exogenous revenue. `probes/` and `excluded-initial/` preserve earlier GLM exploratory evidence and its dispositions; the current paper uses the exact control model.

---
name: verify-financial-examples
description: Execute python-financial's real offline statistical examples and retain plots/results without running provider notebooks or disclosing credentials.
---
# Verify financial examples
## Surface and isolation
Independent Python scripts/notebooks, local datasets and matplotlib figures. No single financial app or live trading service. Offline examples are safe in an isolated environment; provider notebooks require separate auth and network approval, never run as incidental smoke tests.
## Launch
Create a virtualenv, install helpers' sibling requirements.txt, and use that environment's Python. Requires Python3, numpy/pandas/matplotlib/seaborn/statsmodels. Original linear_regression.py could not run without statsmodels; prerequisite is explicit, not a code failure. Use Agg for noninteractive plot output. The helper does not modify product globals, files or random seed.
## Doctor
`python .cursor/skills/verify-financial-examples/helpers/drive.py doctor --out .verification-evidence/doctor`
Checks actual imports, target dataset and notebook JSON syntax only. Does not execute notebook cells.
## Drive
`python .cursor/skills/verify-financial-examples/helpers/drive.py drive --out .verification-evidence/run`
Executes actual linear_regression.py on health.csv, independently checks correlation and finite model parameters, saves actual regression figure. Executes actual normal-distribution script with Agg, checks1000finite samples, saves histogram. Random values are not promised identical. Inspect saved plots for readability before claiming visual readiness.
## Evidence
Retained JSON contains versions, rows/statistics and notebook parse status; PNGs capture real figures. Failure exits nonzero. This proves offline demonstrations, not causal health advice, stock prediction accuracy or provider availability.
## Cleanup
No server or provider call. Agg avoids blocking GUI; all figures close in finally. Retain evidence, never delete it during cleanup. Virtualenv is isolated and can be reused.
## Helpers
Executable helpers/drive.py supports doctor/drive and --out. requirements.txt documents dependencies. Feature maps separate offline proof from provider and notebook limits. Maintain maps when source changes.

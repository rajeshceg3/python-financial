# Notebooks and provider access
## Sub-features
Historical Netflix plotting and AlphaVantage live data notebooks.
## How to get to it (user POV)
Open the notebooks in Jupyter with their documented packages. Provider examples now read ALPHAVANTAGE_API_KEY from the environment and fail clearly if absent. Never paste a key into notebooks or outputs.
## Driving it with drive.py
Doctor/drive parse notebook structure only. No provider cell, pip-install cell or full notebook execution is performed. Credential literals were removed from current notebook cells and affected-cell saved outputs cleared; other historical outputs preserved; history can still contain them.
## Gotchas
Provider key ownership/revocation and past Git history exposure remain unresolved, not repaired by environment lookup. No live network/provider proof. Netflix notebook execution and its local-data chart returns remain unverified; malformed get_intradayraday was corrected but not provider-run. Some plotting cells rely on execution order/imports; parse success does not prove notebook execution.

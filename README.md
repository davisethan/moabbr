# moabbr

[MOABB](https://neurotechx.github.io/moabb/) interface to [tombolo](https://pypi.org/project/tombolo/) for analysis of machine learning benchmarks.

MOABB evaluation results are a pandas DataFrame with one row per pipeline/dataset/subject/session. moabbr transforms this into the format tombolo expects using DuckDB, then calls the tombolo Docker image to run the analysis. Each dataset is treated as an independent study and each pipeline as a treatment.

## Requirements

[Docker](https://docs.docker.com/get-started/get-docker/) must be installed and running, and the tombolo image must be pulled:

```
docker pull ethandavisecd/tombolo:latest
```

## Installation

```
pip install moabbr
```

## Usage

`results` is the `pd.DataFrame` returned by a MOABB evaluation, with columns `dataset`, `pipeline`, `subject`, and `score`.

```python
from moabbr import nma, bnma

data = moabbr.nma(results)    # frequentist NMA via netmeta
data = moabbr.bnma(results)   # Bayesian NMA via gemtc
```

Both functions accept a `greater_is_better` flag (default `True`). Set to `False` for metrics where lower is better (e.g. error rate).

## Plots

```python
from moabbr.plots import (
    ranking_plot,
    league_table,
    forest_plot,
    heterogeneity_table,
    prediction_table,  # nma only
    convergence_table, # bnma only
)

ranking_plot(result)
league_table(result)
forest_plot(result, reference="my_pipeline")
heterogeneity_table(result)
```

Each function returns a `matplotlib.figure.Figure`.
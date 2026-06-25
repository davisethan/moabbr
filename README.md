# moabbr

A Python interface to R's statistical ecosystem, containerised in the [procr](https://hub.docker.com/r/ethandavisecd/procr) Docker image, for [MOABB](https://github.com/NeuroTechX/moabb) benchmark analysis.

## Installation

```bash
pip install moabbr
```

Requires [Docker](https://www.docker.com) with the procr image pulled:

```bash
docker pull ethandavisecd/procr:latest
```

## Usage

`results` is the `pd.DataFrame` returned by a MOABB evaluation, with columns `dataset`, `pipeline`, `subject`, and `score`.

### Network meta-analysis

```python
import moabbr as r

nma = r.nma(results)    # frequentist NMA via netmeta
bnma = r.bnma(results)  # Bayesian NMA via gemtc (sensitivity analysis)
```

Both functions accept a `greater_is_better` flag (default `True`); set it to `False` for metrics like NLL or Brier score.

Each dataset is treated as an independent study and each pipeline as a treatment. Pairwise mean differences are computed per fold, then aggregated per dataset before being passed to R.

## Development

**Lint and format Python:**

```bash
ruff check moabbr
ruff format moabbr
```

**Lint and format SQL:**

```bash
sqlfluff lint moabbr
sqlfluff fix moabbr
```

**Generate docs:**

```bash
pdoc moabbr --output-dir docs
```

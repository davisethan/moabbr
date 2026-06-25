# moabbr

Network meta-analysis of [MOABB](https://github.com/NeuroTechX/moabb) BCI benchmarks.

Compares BCI decoding pipelines across datasets using frequentist NMA ([netmeta](https://cran.r-project.org/package=netmeta)) and Bayesian NMA ([gemtc](https://cran.r-project.org/package=gemtc)) as a sensitivity analysis. Each dataset is treated as an independent study; the outcome is mean decoding on a mean difference scale.

## Installation

```bash
pip install moabbr
```

Requires [Docker](https://www.docker.com) with the moabbr image pulled:

```bash
docker pull ethandavisecd/moabbr:latest
```

## Usage

```python
import moabbr

nma = moabbr.nma(results)
bnma = moabbr.bnma(results)
```

`results` is the `pd.DataFrame` returned by MOABB's evaluation.

## Repository structure

- [`docker/`](docker/) — R environment and Dockerfile
- [`python/`](python/) — PyPI package

## Docs

```bash
pdoc python/src/moabbr --output-dir docs
```

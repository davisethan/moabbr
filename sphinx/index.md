# moabbr

[MOABB](https://neurotechx.github.io/moabb/) interface to [tombolo](https://pypi.org/project/tombolo/) for analysis of machine learning benchmarks in R.

Each dataset is treated as an independent study and each pipeline as a treatment.

Requires [Docker](https://docs.docker.com/get-started/get-docker/) with the [tombolo](https://hub.docker.com/r/ethandavisecd/tombolo) image pulled:

```
docker pull ethandavisecd/tombolo:latest
```

```{toctree}
:maxdepth: 2
:caption: API

analysis
plotting
```

```{toctree}
:maxdepth: 2
:caption: Examples

results
plots
```
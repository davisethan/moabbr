# python

Python interface to the moabbr Docker image for network meta-analysis of BCI benchmarks.

## Requirements

The moabbr Docker image must be available locally before use:

```bash
docker pull ethandavisecd/moabbr:latest
```

## Docs

```bash
pdoc src/moabbr --output-dir docs
```

## Lint and format

```bash
ruff check src
ruff format src
```

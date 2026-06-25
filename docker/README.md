# docker

R environment for running frequentist and Bayesian network meta-analysis via `netmeta` and `gemtc`.

## Build

Local (for testing):

```bash
docker build --platform linux/amd64 -t moabbr .
```

Docker Hub:

```bash
docker build --platform linux/amd64 -t ethandavisecd/moabbr:latest .
docker push ethandavisecd/moabbr:latest
```

## Lint and format

**R:**

```bash
Rscript -e 'lintr::lint_dir("src")'
Rscript -e 'styler::style_dir("src")'
```

**SQL:**

```bash
sqlfluff lint src --dialect duckdb
sqlfluff fix src --dialect duckdb
```

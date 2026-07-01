import importlib.resources

import duckdb
import tombolo
import pandas as pd


def _sql(command: str, results: pd.DataFrame) -> pd.DataFrame:
    sql = importlib.resources.files("moabbr").joinpath(f"sql/{command}.sql").read_text()
    con = duckdb.connect()
    con.register("results", results)
    return con.execute(sql).df().to_dict(orient="records")


def nma(results: pd.DataFrame, greater_is_better: bool = True) -> dict:
    """Run a frequentist random-effects network meta-analysis on MOABB evaluation results.

    Parameters:

    - `results`: MOABB evaluation DataFrame with columns `dataset`, `pipeline`, `subject`, `score`.
    - `greater_is_better`: If `True`, higher scores rank better (e.g. accuracy).
      If `False`, lower scores rank better (e.g. error rate).

    Each dataset is treated as an independent study and each pipeline as a treatment.
    Pairwise mean differences are computed per subject, then aggregated per dataset.

    Returns a dict with:

    - `ranking`: P-score per pipeline (0-1, higher = better rank).
    - `league`: Pairwise `md`, `lower`, `upper`, `z`, `pval` - each a pipeline x pipeline matrix.
    - `heterogeneity`: `tau2`, `tau`, `i2`, `i2_lower`, `i2_upper`, `q`, `q_df`, `q_pval`.
    - `prediction`: Prediction interval `lower` and `upper` - each a pipeline x pipeline matrix.
    """
    return tombolo.nma(_sql("nma", results), greater_is_better)


def bnma(results: pd.DataFrame, greater_is_better: bool = True) -> dict:
    """Run a Bayesian random-effects network meta-analysis on MOABB evaluation results.

    Parameters:

    - `results`: MOABB evaluation DataFrame with columns `dataset`, `pipeline`, `subject`, `score`.
    - `greater_is_better`: If `True`, higher scores rank better (e.g. accuracy).
      If `False`, lower scores rank better (e.g. error rate).

    Each dataset is treated as an independent study and each pipeline as a treatment.
    Per-subject scores are averaged per dataset before being passed to the model.

    Returns a dict with:

    - `ranking`: SUCRA per pipeline (0-1, higher = better rank).
    - `league`: Pairwise posterior median `md` and 95% credible interval `lower`, `upper` - each a pipeline x pipeline matrix.
    - `heterogeneity`: Posterior `sd`, `sd_lower`, `sd_upper` (2.5th-97.5th percentile).
    - `convergence`: `rhat_max`, `ess_bulk_min`, `ess_tail_min` across all model parameters.
    """
    return tombolo.bnma(_sql("bnma", results), greater_is_better)

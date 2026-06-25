import json
import os
import subprocess

import pandas as pd

_image = os.getenv("MOABBR_IMAGE", "ethandavisecd/moabbr:latest")


def _run(command: str, results: pd.DataFrame, greater_is_better: bool) -> dict:
    proc = subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "-i",
            _image,
            command,
            str(greater_is_better).lower(),
        ],
        input=results.to_csv(index=False).encode(),
        capture_output=True,
        check=True,
    )
    return json.loads(proc.stdout)


def nma(results: pd.DataFrame, greater_is_better: bool = True) -> dict:
    """Run frequentist network meta-analysis via netmeta.

    Fits a random-effects NMA (DerSimonian-Laird heterogeneity, t-distribution
    CIs) treating each dataset as an independent study and each pipeline as a
    treatment. All pairwise comparisons are direct (fully-crossed benchmark).

    All league tables are keyed as `league[metric][row][col]`, where the value
    represents row minus col. Diagonal entries are `null`.

    Parameters:

    - **results**: MOABB evaluation output with columns `dataset`, `pipeline`, `subject`, `score`.
    - **greater_is_better**: Whether a higher score is better. Set to `False` for metrics like NLL or Brier score. Affects P-score ranking.

    Returns:

    - **p_scores** (`dict[str, float]`): P-score per pipeline. Higher is better. Frequentist analogue of SUCRA.
    - **league** (`dict`): Pairwise table with keys `md`, `lower`, `upper` (95% CI), `z`, `pval` (two-sided).
    - **heterogeneity** (`dict`): `tau2`, `tau` (DL point estimates); `i2`, `i2_lower`, `i2_upper` (95% CI); `q`, `q_df`, `q_pval`.
    - **prediction** (`dict`): Prediction interval matrix `lower`/`upper` on the outcome scale — expected range of true effects in a new dataset.
    """
    return _run("nma", results, greater_is_better)


def bnma(results: pd.DataFrame, greater_is_better: bool = True) -> dict:
    """Run Bayesian network meta-analysis via gemtc.

    Fits a random-effects NMA (normal likelihood, identity link, 4 chains x
    100k iterations, thinning 10) via JAGS. Used as a sensitivity analysis
    alongside `nma`.

    All league tables are keyed as `league[metric][row][col]`, where the value
    represents row minus col. Diagonal entries are `null`.

    Parameters:

    - **results**: MOABB evaluation output with columns `dataset`, `pipeline`, `subject`, `score`.
    - **greater_is_better**: Whether a higher score is better. Set to `False` for metrics like NLL or Brier score. Affects SUCRA ranking.

    Returns:

    - **sucra** (`dict[str, float]`): SUCRA per pipeline. Higher is better. Bayesian analogue of P-scores.
    - **league** (`dict`): Pairwise table with keys `md` (posterior median), `lower`/`upper` (95% credible intervals).
    - **heterogeneity** (`dict`): `sd` (posterior median of between-study SD, Bayesian analogue of tau), `sd_lower`, `sd_upper` (95% credible interval).
    - **convergence** (`dict`): `rhat_max` (< 1.01), `ess_bulk_min` (> 400), `ess_tail_min` (> 400).
    """
    return _run("bnma", results, greater_is_better)

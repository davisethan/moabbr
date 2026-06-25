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
    return _run("nma", results, greater_is_better)


def bnma(results: pd.DataFrame, greater_is_better: bool = True) -> dict:
    return _run("bnma", results, greater_is_better)

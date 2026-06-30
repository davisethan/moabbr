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
    return tombolo.nma(_sql("nma", results), greater_is_better)


def bnma(results: pd.DataFrame, greater_is_better: bool = True) -> dict:
    return tombolo.bnma(_sql("bnma", results), greater_is_better)

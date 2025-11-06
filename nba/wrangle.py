import pandas as pd

def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Standardise column names to snake_case."""
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[^\w]+", "_", regex=True)
        .str.strip("_")
    )
    return df

def filter_by_team(df: pd.DataFrame, team: str) -> pd.DataFrame:
    """Return only rows for a specific team."""
    return df[df["team"] == team]

def summarise_by_season(df: pd.DataFrame, value: str, agg: str = "mean"):
    """Group by season and aggregate."""
    return df.groupby("season", as_index=False)[value].agg(agg)

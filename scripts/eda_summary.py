import pandas as pd

def add_derived_metrics(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["LossRatio"] = df["TotalClaims"] / df["TotalPremium"]
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]
    return df

def compute_group_loss_ratio(df: pd.DataFrame, group_cols):
    grouped = (
        df.groupby(group_cols)
        .agg(
            policies=("PolicyID", "nunique"),
            total_premium=("TotalPremium", "sum"),
            total_claims=("TotalClaims", "sum"),
        )
        .reset_index()
    )
    grouped["loss_ratio"] = grouped["total_claims"] / grouped["total_premium"]
    return grouped

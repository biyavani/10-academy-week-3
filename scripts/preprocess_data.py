import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/MachineLearningRating_v3.txt")
PROCESSED_PATH = Path("data/processed/acis_processed.csv")

def main():
    df = pd.read_csv(RAW_PATH, delimiter="|")

    # Very light cleaning - adjust as you like
    df = df.drop_duplicates()
    # Example: keep only rows with non missing TotalPremium and TotalClaims
    df = df.dropna(subset=["TotalPremium", "TotalClaims"])

    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

if __name__ == "__main__":
    main()

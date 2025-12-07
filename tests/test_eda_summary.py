import pandas as pd
from scripts.eda_summary import add_derived_metrics

def test_add_derived_metrics():
    df = pd.DataFrame({"TotalPremium": [100, 200], "TotalClaims": [50, 80]})
    out = add_derived_metrics(df)
    assert "LossRatio" in out.columns
    assert "Margin" in out.columns

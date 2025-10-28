import os
import pandas as pd


def test_ygainers_normalized():
    path = "ygainers_normalized.csv"
    assert os.path.exists(path), f"{path} file not found"

    df = pd.read_csv(path)
    expected_cols = [
        "symbol", "company_name", "price", "change", "perc_change", "volume"
    ]
    for col in expected_cols:
        assert col in df.columns, f"Missing column: {col}"

def test_wsjgainers_normalized():
    path = "wsjgainers_normalized.csv"
    assert os.path.exists(path), f"{path} file not found"

    df = pd.read_csv(path)

    expected_cols = [
        "symbol", "company_name", "price", "change", "perc_change", "volume"
    ]
    for col in expected_cols:
        assert col in df.columns, f"Missing column: {col}"

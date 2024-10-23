import pandas as pd
from titanic_analysis.data_loader import load_titanic_data

def test_load_titanic_data():
    df = load_titanic_data("../../data/titanic.csv")
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    assert not df.empty, "The DataFrame should not be empty"

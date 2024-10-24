import os 
import pandas as pd
from titanic_analysis.data_loader import load_titanic_data

def test_load_titanic_data():
    base_path = os.path.dirname(__file__)  # Get the directory of the test file
    file_path = os.path.join(base_path, "../data/titanic.csv")
    
    df = load_titanic_data(file_path)
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    assert not df.empty, "The DataFrame should not be empty"

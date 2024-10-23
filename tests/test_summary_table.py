from titanic_analysis.summary_table import create_summary_table
import pandas as pd

def test_create_summary_table():
    # Mock a DataFrame
    mock_df = pd.DataFrame(data={
        'Age': [22, 38, 26, 35, None],
        'Sex': ['male', 'female', 'female', 'male', 'male'],
        'Survived': [0, 1, 1, 0, 1]
    })
    
    summary_df = create_summary_table(mock_df)
    
    assert 'Feature Name' in summary_df.columns, f"Summary should include 'Feature Name'. Found columns: {summary_df.columns.tolist()}"
    assert 'Data Type' in summary_df.columns, f"Summary should include 'Data Type'. Found columns: {summary_df.columns.tolist()}"
    assert 'Has Missing Values?' in summary_df.columns, f"Summary should include 'Has Missing Values?'. Found columns: {summary_df.columns.tolist()}"
    assert 'Number of Unique Values' in summary_df.columns, f"Summary should include 'Number of Unique Values'. Found columns: {summary_df.columns.tolist()}"

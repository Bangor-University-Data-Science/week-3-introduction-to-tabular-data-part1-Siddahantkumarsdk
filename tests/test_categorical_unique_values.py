from titanic_analysis.categorical_unique_values import display_unique_values
import pandas as pd
def test_display_unique_values():
    # Mock a DataFrame
    mock_df = pd.DataFrame(data={
        'Sex': ['male', 'female', 'female', 'male'],
        'Embarked': ['S', 'C', 'S', 'Q']
    })
    categorical_features = ['Sex', 'Embarked']
    
    unique_values = display_unique_values(mock_df, categorical_features)
    
    assert isinstance(unique_values, dict), "The result should be a dictionary"
    assert 'Sex' in unique_values and 'Embarked' in unique_values, "Both categorical features should be in the result"

from titanic_analysis.feature_type_dict import create_feature_type_dict
import pandas as pd
def test_create_feature_type_dict():
    # Mock a DataFrame
    mock_df = pd.DataFrame(data={
        'Age': [22, 38, 26, 35],
        'Sex': ['male', 'female', 'female', 'male'],
        'Survived': [0, 1, 1, 0]
    })
    feature_types = create_feature_type_dict(mock_df)
    
    assert 'numerical' in feature_types, "The dictionary should have a 'numerical' key"
    assert 'categorical' in feature_types, "The dictionary should have a 'categorical' key"

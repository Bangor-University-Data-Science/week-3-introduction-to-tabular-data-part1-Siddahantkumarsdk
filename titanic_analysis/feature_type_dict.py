import pandas as pd

def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],  # Fill with continuous numerical features
            'discrete': []  # Fill with discrete numerical features
        },
        'categorical': {
            'nominal': [],  # Fill with nominal categorical features
            'ordinal': []  # Fill with ordinal categorical features
        }
    }

    for column in df.columns:
        # Check if the feature is numerical
        if pd.api.types.is_numeric_dtype(df[column]):
            # Classify numerical features as continuous or discrete
            if df[column].nunique() > 10:
                feature_types['numerical']['continuous'].append(column)
            else:
                feature_types['numerical']['discrete'].append(column)
        else:
            # Classify categorical features as nominal or ordinal
            if df[column].dtype == 'object':
                feature_types['categorical']['nominal'].append(column)
            # In some cases, ordinal categorical data is stored as int or can be inferred from context
            # For example, if the column has only a few unique integer values (e.g., passenger class), it may be ordinal
            # You may need custom logic or domain knowledge for this classification
            elif df[column].dtype == 'category':
                feature_types['categorical']['ordinal'].append(column)

    return feature_types

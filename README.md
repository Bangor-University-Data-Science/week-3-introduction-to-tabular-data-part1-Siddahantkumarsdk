[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/2_V-jg1k)

# Titanic Analysis

## Project Overview

This project focuses on exploring the Titanic dataset to perform basic data exploration tasks. The tasks involve loading the data, identifying feature types, selecting numerical features, displaying unique values for categorical columns, and creating a simple summary table.

The repository contains:
- Core functions to work with the Titanic dataset.
- A test suite to ensure each function behaves as expected.

### Homework Tasks:
1. **Create a Feature Type Dictionary**:
   - Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
   
2. **Create a DataFrame with Only Numerical Features**:
   - Selects numerical features from the dataset.
   
3. **Display Unique Values for Categorical Columns**:
   - Displays the unique values for each categorical column.
   
4. **Create a Simple Summary Table**:
   - Generates a summary table with feature names, data types, number of unique values, and if the feature has missing values.

## Project Structure

```
titanic_analysis/
│
├── data/
│   └── titanic.csv                # Titanic dataset
│
├── titanic_analysis/
│   ├── __init__.py                # Module initialization
│   ├── data_loader.py             # Loads the Titanic dataset
│   ├── feature_type_dict.py       # Classifies feature types
│   ├── numerical_df.py            # Extracts numerical features
│   ├── categorical_unique_values.py # Displays unique values for categorical features
│   ├── summary_table.py           # Creates a summary table of the dataset
│
├── tests/
│   ├── __init__.py                # Module initialization
│   ├── test_data_loader.py        # Tests for the data loading function
│   ├── test_feature_type_dict.py  # Tests for the feature classification function
│   ├── test_numerical_df.py       # Tests for numerical DataFrame function
│   ├── test_categorical_unique_values.py # Tests for unique value display function
│   ├── test_summary_table.py      # Tests for summary table function
│
├── .gitignore                     # Files to ignore for git
├── requirements.txt               # Python package dependencies
└── README.md                      # Documentation (you're reading this)
```

## Setup Instructions

### 1. Clone the Repository

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/titanic_analysis.git
cd titanic_analysis
```

### 2. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Download the Dataset

Make sure to place the `titanic.csv` file inside the `data/` directory. You can download the Titanic dataset from [Kaggle's Titanic page](https://www.kaggle.com/c/titanic/data) if you don't already have it.

## Running the Project

### 1. Explore the Dataset

You can use the functions provided in the `titanic_analysis/` module to explore the Titanic dataset.

For example, to load the data and classify features:

```python
from titanic_analysis.data_loader import load_titanic_data
from titanic_analysis.feature_type_dict import create_feature_type_dict

# Load Titanic dataset
df = load_titanic_data('data/titanic.csv')

# Classify features
feature_types = create_feature_type_dict(df)
print(feature_types)
```

### 2. Running Tests

This project uses `pytest` for testing. You can run the test suite with the following command:

```bash
pytest
```

This will execute the tests in the `tests/` folder and verify that all the functions are working as expected.

## Files and Functionality

### Core Functions

- **`load_titanic_data(filepath: str) -> pd.DataFrame`**:
   - Loads the Titanic dataset from a CSV file.
   
- **`create_feature_type_dict(df: pd.DataFrame) -> dict`**:
   - Classifies features into numerical and categorical types.
   
- **`get_numerical_df(df: pd.DataFrame, numerical_features: list) -> pd.DataFrame`**:
   - Creates a DataFrame containing only the numerical features.
   
- **`display_unique_values(df: pd.DataFrame, categorical_features: list) -> dict`**:
   - Displays unique values for each categorical feature.
   
- **`create_summary_table(df: pd.DataFrame) -> pd.DataFrame`**:
   - Creates a summary table with feature names, data types, number of unique values, and missing value status.

### Tests

- Each core function has a corresponding test file in the `tests/` folder.
- These tests ensure that the functions return the correct outputs when provided with sample data.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue if you have any improvements or suggestions.

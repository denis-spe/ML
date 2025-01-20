# Praise Ye The LORD And Saviour Jesus Christ

# Importing Libraries
import pandas as pd

# Function to replace all NaN values in the DataFrame
def handle_replace_all_na(df: pd.DataFrame, replace_all_na: str):
    """
    This function replaces all NaN values in the DataFrame with the specified value.
    """
    match replace_all_na:
        case "None":
            return df
        case "frequency(mode)":
            for col in df.columns:
                df[col] = df[col].fillna(df[col].mode()[0])
            return df
        case "backFill":
            return df.bfill()
        case "forwardFill":
            return df.ffill()
        case "unknown for categorical and 0 for continuous":
            for col in df.columns:
                if df[col].dtype == "object":
                    df[col] = df[col].fillna("unknown")
                else:
                    df[col] = df[col].fillna(0)
            return df
    
def handle_change_na_in_numeric(df: pd.DataFrame, change_na_in_numeric: str):
    """
    This function changes NaN values in numeric columns with the specified value.
    """
    match change_na_in_numeric:
        case "None":
            return df
        case "mean":
            for col in df.columns:
                if df[col].dtype != "object":
                    df[col].fillna(df[col].mean(), inplace=True)
            return df
        case "median":
            for col in df.columns:
                if df[col].dtype != "object":
                    df[col].fillna(df[col].median(), inplace=True)
            return df
        case "max":
            for col in df.columns:
                if df[col].dtype != "object":
                    df[col].fillna(df[col].max(), inplace=True)
            return df
        case "min":
            for col in df.columns:
                if df[col].dtype != "object":
                    df[col].fillna(df[col].min(), inplace=True)
            return df
        case "mode":
            for col in df.columns:
                if df[col].dtype != "object":
                    df[col].fillna(df[col].mode()[0], inplace=True)
            return df
        case "std":
            for col in df.columns:
                if df[col].dtype != "object":
                    df[col].fillna(df[col].std(), inplace=True)
            return df
        case "0.0":
            for col in df.columns:
                if df[col].dtype != "object":
                    df[col].fillna(0.0, inplace=True)
            return df
        
def handle_handle_na_in_categorical(df: pd.DataFrame, handle_na_in_categorical: str):
    """
    This function handles NaN values in categorical columns with the specified value
    """
    match handle_na_in_categorical:
        case "None":
            return df
        case "mode":
            for col in df.columns:
                if df[col].dtype == "object":
                    df[col].fillna(df[col].mode()[0], inplace=True)
            return df
        case "unknown":
            for col in df.columns:
                if df[col].dtype == "object":
                    df[col].fillna("unknown", inplace=True)
            return df
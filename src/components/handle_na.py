# Praise Ye The LORD And Saviour Jesus Christ

# Importing Libraries
import pandas as pd
from typing import List

# Function to replace all NaN values in the DataFrame
def handle_replace_all_na(df: pd.DataFrame, replace_all_na: str):
    """
    This function replaces all NaN values in the DataFrame with the specified value.
    """
    # Make data copy
    df = df.copy()
    
    match replace_all_na:
        case "None":
            df = df
        case "frequency(mode)":
            for col in df.columns:
                df[col] = df[col].fillna(df[col].mode()[0])
            return df
        case "backFill":
            df = df.bfill()
        case "forwardFill":
            df = df.ffill()
        case "unknown for categorical and 0 for continuous":
            for col in df.columns:
                if df[col].dtype == "object":
                    df[col] = df[col].fillna("unknown")
                else:
                    df[col] = df[col].fillna(0)
    return df
    

def handle_na_in_numeric(df: pd.DataFrame, fill_na_in_numeric: str):
    """
    This function changes NaN values in numeric columns with the specified value.
    """
    # Make data copy
    df = df.copy()
    
    match fill_na_in_numeric:
        case "None":
            df = df
        case "mean":
            for col in df.columns:
                if df[col].dtype != "object":
                    df[col] = df[col].fillna(df[col].mean())
        case "median":
            for col in df.columns:
                if df[col].dtype != "object":
                    df[col] = df[col].fillna(df[col].median())
        case "max":
            for col in df.columns:
                if df[col].dtype != "object":
                    df[col] = df[col].fillna(df[col].max())
        case "min":
            for col in df.columns:
                if df[col].dtype != "object":
                    df[col] = df[col].fillna(df[col].min())
        case "mode":
            for col in df.columns:
                if df[col].dtype != "object":
                    df[col] = df[col].fillna(df[col].mode()[0])
        case "std":
            for col in df.columns:
                if df[col].dtype != "object":
                    df[col] = df[col].fillna(df[col].std())
        case "0.0":
            for col in df.columns:
                if df[col].dtype != "object":
                    df[col] = df[col].fillna(0.0)
    return df


def handle_na_in_categorical(df: pd.DataFrame, fill_na_in_categorical: str):
    """
    This function handles NaN values in categorical columns with the specified value
    """
    # Make data copy
    df = df.copy()
    
    match fill_na_in_categorical:
        case "None":
            return df
        case "mode":
            for col in df.columns:
                if df[col].dtype == "object":
                    df[col] = df[col].fillna(df[col].mode()[0])
            return df
        case "unknown":
            for col in df.columns:
                if df[col].dtype == "object":
                    df[col] = df[col].fillna("unknown")
            return df


def drop_columns(df: pd.DataFrame, columns: List[str]):
    return df.drop(columns=columns)


def fill_NaN_or_drop(
    replace_all_na,
    fill_na_in_numeric,
    fill_na_in_categorical,
    column_to_drop,
    x_train=None,
    x_test=None,
    test=None
):
    # Drop columns
    if len(column_to_drop) > 0:
        if x_train is not None and x_test is not None:
            x_train = drop_columns(x_train, column_to_drop)
            x_test = drop_columns(x_test, column_to_drop)
        if test is not None:
            test = drop_columns(test, column_to_drop)
        
    # Replace all NaN values in the DataFrame
    if replace_all_na != "None": 
        if x_train is not None and x_test is not None:
            x_train = handle_replace_all_na(x_train, replace_all_na)
            x_test = handle_replace_all_na(x_test, replace_all_na)
        if test is not None:
            test = handle_replace_all_na(test, replace_all_na)
    
    # Fill missing values in numeric columns
    if fill_na_in_numeric != "None":
        if x_train is not None and x_test is not None:
            x_train = handle_na_in_numeric(x_train, fill_na_in_numeric)
            x_test = handle_na_in_numeric(x_test, fill_na_in_numeric)
        if test is not None:
            test = handle_na_in_numeric(test, fill_na_in_numeric)
        
    # Handle missing values in categorical columns
    if fill_na_in_categorical != "None":
        if x_train is not None and x_test is not None:
            x_train = handle_na_in_categorical(x_train, fill_na_in_categorical)
            x_test = handle_na_in_categorical(x_test, fill_na_in_categorical)
        if test is not None:
            test = handle_na_in_categorical(test, fill_na_in_categorical)
            
        
    if replace_all_na != "None" and fill_na_in_numeric != "None":
        if x_train is not None and x_test is not None:
            x_train = handle_replace_all_na(x_train, replace_all_na)
            x_test = handle_replace_all_na(x_test, replace_all_na)
        
            x_train = handle_na_in_numeric(x_train, fill_na_in_numeric)
            x_test = handle_na_in_numeric(x_test, fill_na_in_numeric)
        if test is not None:
            test = handle_replace_all_na(test, replace_all_na)
            test = handle_na_in_numeric(test, fill_na_in_numeric)
            
    elif replace_all_na != "None" and fill_na_in_categorical != "None":
        if x_train is not None and x_test is not None:
            x_train = handle_replace_all_na(x_train, replace_all_na)
            x_test = handle_replace_all_na(x_test, replace_all_na)
        
            x_train = handle_na_in_categorical(x_train, fill_na_in_categorical)
            x_test = handle_na_in_categorical(x_test, fill_na_in_categorical)
        if test is not None:
            test = handle_replace_all_na(test, replace_all_na)
            test = handle_na_in_categorical(test, fill_na_in_categorical)
            
    elif fill_na_in_categorical != "None" and fill_na_in_numeric != "None":
        if x_train is not None and x_test is not None:
            x_train = handle_na_in_categorical(x_train, fill_na_in_categorical)
            x_test = handle_na_in_categorical(x_test, fill_na_in_categorical)
        
            x_train = handle_na_in_numeric(x_train, fill_na_in_numeric)
            x_test = handle_na_in_numeric(x_test, fill_na_in_numeric)
            
        if test is not None:
            test = handle_na_in_categorical(test, fill_na_in_categorical)
            test = handle_na_in_numeric(test, fill_na_in_numeric)
    
    elif replace_all_na != "None" and fill_na_in_numeric != "None" and fill_na_in_categorical != "None":
        if x_train is not None and x_test is not None:
            x_train = handle_replace_all_na(x_train, replace_all_na)
            x_test = handle_replace_all_na(x_test, replace_all_na)
        
            x_train = handle_na_in_numeric(x_train, fill_na_in_numeric)
            x_test = handle_na_in_numeric(x_test, fill_na_in_numeric)
        
            x_train = handle_na_in_categorical(x_train, fill_na_in_categorical)
            x_test = handle_na_in_categorical(x_test, fill_na_in_categorical)
            
        if test is not None:
            test = handle_replace_all_na(test, replace_all_na)
            test = handle_na_in_numeric(test, fill_na_in_numeric)
            test = handle_na_in_categorical(test, fill_na_in_categorical)
    
    return (x_train, x_train, test)
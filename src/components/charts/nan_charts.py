# Bless Be The Lord

# Import libraries.
import streamlit as st
import pandas as pd
import altair as alt


def nan_chart(df: pd.DataFrame):
    isna = df.isna().sum().reset_index()
    # Rename the columns
    isna.columns = ["column", "number of missing values (NaN)"]
    
    # Filter the only the missing value greater then 0
    isna = isna[isna["number of missing values (NaN)"] > 0]
    
    
    cornerRadius_slider = alt.binding_range(min=0, max=50, step=1)
    cornerRadius_var = alt.param(bind=cornerRadius_slider, value=100, name="cornerRadius")

    
    bar_chart = (alt.Chart(isna)
                    .mark_bar()
                    .encode(
                        x="column",
                        y="number of missing values (NaN)",
                        # radius=cornerRadius_var
                        ))
    
    st.altair_chart(bar_chart)

def nan_donut(df: pd.DataFrame):
    """
    Represents a donut chart for plotting missing values in the data.
    
    Args:
        df: (pd.DataFrame) pandas data frame.
    """
    isna = df.isna().sum().reset_index()
    # Rename the columns
    isna.columns = ["column", "number of missing values (NaN)"]
    
    # Filter the only the missing value greater then 0
    isna = isna[isna["number of missing values (NaN)"] > 0]
    
    donut = alt.Chart(isna).mark_arc(innerRadius=50).encode(
        theta="number of missing values (NaN)",
        color="column",
        )
    st.altair_chart(donut)
    
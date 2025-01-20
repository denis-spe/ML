###
# Glory Be To Lord
###

# Import libraries
import pandas as pd
import streamlit as st
from const import FOOTER_CONTENT
from components.conf import config_page
from components.charts.nan_charts import nan_chart, nan_donut
from components.handle_na import (
    handle_replace_all_na,
    handle_change_na_in_numeric,
    handle_handle_na_in_categorical,
)

# Config the page
config_page("ML | Data Cleaning", "clean.png")


def highlight_max(v, props="background-color: red"):
    if type(v) == int and v > 0:
        return props
    if type(v) == int:
        return "color: green; opacity: 20%;"


def nan_df_style(df: pd.DataFrame):

    return (
        df.isna()
        .sum()
        .reset_index()
        .rename(columns={"index": "column", 0: "NaN"})
        .style.map(highlight_max)
    )


# Side bar
sidebar: st = st.sidebar


def display_content_for_uploaded_files():
    """
    Display the content for uploaded files
    """
    # Descriptions
    st.write(":blue[Clean up the training, validation and test data]")

    radio_selector = st.radio(
        "Select window to show",
        options=["Data frame", "Charts"],
        index=0,
        horizontal=True,
    )

    # Fill in the missing values the data
    sidebar.subheader("Fill in the missing values (NaN)", divider=True)
    replace_all_na = sidebar.selectbox(
        "Replace all NaN with:",
        options=[
            "None",
            "frequency(mode)",
            "backFill",
            "forwardFill",
            "unknown for categorical and 0 for continuous",
        ],
    )

    change_na_in_numeric = sidebar.selectbox(
        "Change NaN in numeric columns with:",
        options=["None", "mean", "median", "max", "min", "mode", "std", "0.0"],
    )

    handle_na_in_categorical = sidebar.selectbox(
        "Handle NaN in categorical columns with:",
        options=[
            "None",
            "mode",
            "unknown",
        ],
    )

    if "x_train" in st.session_state:
        # Fetch the x train and and x_test
        x_train = st.session_state["x_train"]
        x_test = st.session_state["x_test"]

        # Replace all NaN values in the DataFrame
        if replace_all_na != "None":
            cleaned_x_train = handle_replace_all_na(x_train, replace_all_na)
            cleaned_x_test = handle_replace_all_na(x_test, replace_all_na)
        else:
            cleaned_x_train = x_train
            cleaned_x_test = x_test

        train_df_col, val_df_val = st.columns(2)

        if radio_selector == "Charts":
            st.write("**X Train Data Sample**")
            st.write("Some of the missing data in x_train in sample")
            train_bar_col, train_donut_col = st.columns(2)
            with train_bar_col:
                nan_chart(cleaned_x_train)
            with train_donut_col:
                nan_donut(cleaned_x_train)
        if radio_selector == "Data frame":
            with train_df_col:
                st.write("**X Train Data Sample**")
                st.write("Some of the missing data in x_train in sample")
                st.write(nan_df_style(cleaned_x_train))

        if radio_selector == "Charts":
            st.write("**X Validation Data Sample**")
            st.write("Missing data in validation data sample")
            test_bar_col, test_donut_col = st.columns(2)
            with test_bar_col:
                nan_chart(cleaned_x_test)
            with test_donut_col:
                nan_donut(cleaned_x_test)
        if radio_selector == "Data frame":
            with val_df_val:
                st.write("**X Validation Data Sample**")
                st.write("Missing data in validation data sample")
                st.write(nan_df_style(cleaned_x_test))

    # Test data frame
    if "test" in st.session_state:
        st.write("**Test Data Frame**")
        test_df = st.session_state["test"]
        st.write("Here is the missing with data in test data frame")
        if radio_selector == "Charts":
            test_bar_col, test_donut_col = st.columns(2)
            with test_bar_col:
                nan_chart(test_df)
            with test_donut_col:
                nan_donut(test_df)
        if radio_selector == "Data frame":
            st.write(nan_df_style(test_df))

    if st.button("Next: Data visualization"):
        st.switch_page("pages/3_Data_visualization.py")


def display_content_for_no_uploaded_files():
    """
    Display the content for no uploaded files
    """
    # Descriptions
    desc = """
    **:blue[Upload the CSV files].**\n
    _To clean up the training, validation and test data or clean un split data._\n
    """
    st.markdown(desc)
    sidebar.markdown(desc)

    # Load images
    st.image("resources/images/clean_up.svg", width=200)


if len(st.session_state) > 0:
    # Display the content for uploaded files
    display_content_for_uploaded_files()
else:
    # Display the content for no uploaded files
    display_content_for_no_uploaded_files()

st.markdown(FOOTER_CONTENT, unsafe_allow_html=True)
sidebar.markdown(FOOTER_CONTENT, unsafe_allow_html=True)

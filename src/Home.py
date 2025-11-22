###
# Glory Be To Lord
###

# Import libraries
import streamlit as st
from components.conf import config_page
from components.check_data_present import data_present
import pandas as pd
from typing import List, Tuple
from const import FOOTER_CONTENT


# Config the page
config_page("ML", "logo.png")


# Side bar
sidebar = st.sidebar

# Upload the file
uploaded_files = sidebar.file_uploader(
    label=":blue[Upload a CSV files]", type=["csv"], accept_multiple_files=True
)


def read_csv(path: str) -> pd.DataFrame:
    """
    Read the csv file
    """
    return pd.read_csv(path)


def get_continuous_column(df: pd.DataFrame) -> list:
    """
    Get the continuous column
    """
    return df.select_dtypes(include=["float64", "int64"]).columns.tolist()


def display_describe(
    pd_files: List[Tuple[str, pd.DataFrame]], selected: str = "DataFrame"
) -> None:
    """
    Display the data frame
    Parameter
    ----------
    idx : int
        The index of the uploaded file
    """
    # Get title
    title = pd_files[0].split(".")[0].title()
    df = pd_files[1]

    st.markdown(
        f"""
    #### **:blue[{title}] Dataset**
    """
    )

    if selected == "DataFrame":
        st.markdown(
            f"""
        ##### \n
        _The dataset contains **:blue[{df.shape[0]}]** rows and **:blue[{df.shape[1]}]** columns._\n
        """
        )

        st.write(df)

    if selected == "Describe":
        cont, cat = st.tabs(["continuous describe", "categorical describe"])
        with cont:
            st.markdown(
                f"""
                _{title} Dataset description_\n
            """
            )
            st.write(df.describe())

        with cat:
            st.markdown(
                f"""
                _{title} Dataset description_\n
            """
            )
            st.write(df.describe(include=[object]))

    if selected == "Data Type":
        st.write(df.dtypes)


def display_content_for_uploaded_files(pd_files: dict):
    """
    Display the content for uploaded files
    """

    # Make pd_files items
    files = list(pd_files.items())

    # Description
    st.subheader(":blue[Data] Statistic")

    # Get the selected option
    selected = st.radio(
        "", options=["DataFrame", "Describe", "Data Type"], horizontal=True
    )

    if len(files) == 2:
        # Columns
        col1, col2 = st.columns(2)

        with col1:
            display_describe(files[0], selected)
            
        with col2:
            display_describe(files[1], selected)

    else:
        display_describe(files[0], selected=selected)

    if st.button("Data split"):
        st.switch_page("pages/1_Data_split.py")


def display_content_for_no_uploaded_files():
    """
    Display the content for no uploaded files
    """
    # Descriptions
    st.markdown(
        """
        **:blue[Upload the dataset in format CSV files].**\n
        _Load train data and test data or you load only train data._\n
        """
    )

    # Load images
    st.image("./resources/images/upload.svg", width=200)


# Display content
if len(uploaded_files) > 0:
    files = {file.name.split(".")[0]: pd.read_csv(file) for file in uploaded_files}

    # Add the files to the session
    for file in files:
        st.session_state[file] = files[file]

    display_content_for_uploaded_files(pd_files=files)
elif len(st.session_state) > 0:
    files = {
        key: value
        for key, value in st.session_state.items()
        if key not in ["x_train", "y_train", "x_test", "y_test"]
    }

    display_content_for_uploaded_files(pd_files=files)

else:
    display_content_for_no_uploaded_files()
    
st.markdown(FOOTER_CONTENT, unsafe_allow_html=True)
sidebar.markdown(FOOTER_CONTENT, unsafe_allow_html=True)

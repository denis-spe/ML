###
# Glory Be To Lord
###

# Import libraries
import streamlit as st
from components.conf import config_page
from components.check_data_present import data_present
import pandas as pd


# Config the page
config_page("ML", "logo.png")


# Side bar
sidebar = st.sidebar

# Add icon image in the side bar
sidebar.image("resources/images/logo.png")

# Upload the file
uploaded_files = sidebar.file_uploader(
    label=":blue[Upload a CSV files]", 
    type=["csv"],
    accept_multiple_files=True
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
    return df.select_dtypes(include=['float64', 'int64']).columns.tolist()


def display_describe(idx: int, selected: str = "DataFrame") -> None:
    """
    Display the data frame
    Parameter
    ----------
    idx : int
        The index of the uploaded file
    """
    # Get the first uploaded file.
    data_path = uploaded_files[idx]

    # Get the title of the file.
    title = data_path.name.split('.')[0].title()

    # Read the data frame
    df = read_csv(data_path)

    st.markdown(f"""
    #### **:blue[{title}] Dataset**
    """)

    if selected == "DataFrame":
        st.markdown(f"""
        ##### \n
        _The dataset contains **:blue[{df.shape[0]}]** rows and **:blue[{df.shape[1]}]** columns._\n
        """)
        
        st.write(df)

    if selected == "Describe":
        cont, cat = st.tabs(["continuous describe", "categorical describe"])
        with cont:
            st.markdown(f"""
                _{title} Dataset description_\n
            """)
            st.write(df.describe())
        
        with cat:
            st.markdown(f"""
                _{title} Dataset description_\n
            """)
            st.write(df.describe(include=[object]))





def display_content_for_uploaded_files():
    """
    Display the content for uploaded files
    """
    # Add the uploaded files in session_state
    st.session_state["uploaded_files"] = uploaded_files

    # Description
    st.subheader(":blue[Data] Statistic")

    # Get the selected option
    selected = st.radio("", 
            options=["DataFrame", "Describe", "Data Type"], 
            horizontal=True)

    if len(uploaded_files) == 2:
        col1, col2 = st.columns(2)

        with col1:
            display_describe(0, selected)

        with col2:
            display_describe(1, selected)

    else:
        display_describe(0)








def display_content_for_no_uploaded_files():
    """
    Display the content for no uploaded files
    """
    # Descriptions
    st.markdown("""
                **:blue[Upload the dataset in format CSV files].**\n
                _Load train data and test data or you load only train data._\n
                """)

    # Load images
    st.image("resources/images/upload.svg", width=200)


# Display content
if len(uploaded_files) > 0:
    display_content_for_uploaded_files()
else:
    display_content_for_no_uploaded_files()



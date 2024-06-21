###
# Glory Be To Lord
###

# Import libraries
import streamlit as st
from components.conf import config_page

# Config the page
config_page("ML | Data Split", "split.png")

# Side bar
sidebar = st.sidebar

# Add icon image in the side bar
sidebar.image("resources/images/split.png")

def display_content_for_uploaded_files():
    """
    Display the content for uploaded files
    """
    # Descriptions
    st.write(":blue[Split the data into train and validation set]")


def display_content_for_no_uploaded_files():
    """
    Display the content for no uploaded files
    """
    # Descriptions
    st.markdown("""
                **:blue[Upload the CSV files].**\n
                _To start splitting the datasets into train and validation set, upload the CSV files._\n
                """)
    sidebar.markdown("""
                **:blue[Upload the CSV files].**\n
                _To start splitting the datasets into train and validation set, upload the CSV files._\n
                """)

    # Load images
    st.image("resources/images/split.svg", width=200)


if len(st.session_state) > 0:
    # Display the content for uploaded files
    display_content_for_uploaded_files()
else:
    # Display the content for no uploaded files
    display_content_for_no_uploaded_files()
###
# Glory Be To Lord
###

# Import libraries
import streamlit as st
from const import FOOTER_CONTENT
from components.conf import config_page

# Config the page
config_page("ML | Data Visualization", "visual.png")

# Side bar
sidebar = st.sidebar


def display_content_for_uploaded_files():
    """
    Display the content for uploaded files
    """
    # Descriptions
    st.write(":blue[Visualize the training, validation and test data]")


def display_content_for_no_uploaded_files():
    """
    Display the content for no uploaded files
    """
    # Descriptions
    desc = """
    **:blue[Clean up the training, validation and test data].**\n
    _To start visualizing the clean training, validation and test data._\n
    """
    st.markdown(desc)
    sidebar.markdown(desc)

    # Load images
    st.image("../resources/images/visual.svg", width=200)


if len(st.session_state) > 0:
    # Display the content for uploaded files
    display_content_for_uploaded_files()
else:
    # Display the content for no uploaded files
    display_content_for_no_uploaded_files()
    
st.markdown(FOOTER_CONTENT, unsafe_allow_html=True)
sidebar.markdown(FOOTER_CONTENT, unsafe_allow_html=True)
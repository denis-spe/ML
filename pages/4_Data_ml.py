###
# Glory Be To Lord
###

# Import libraries
import streamlit as st
from components.conf import config_page

# Config the page
config_page("ML | Data ML", "machine.png")

# Side bar
sidebar = st.sidebar

# Add icon image in the side bar
sidebar.image("resources/images/machine.png", width=50)

def display_content_for_uploaded_files():
    """
    Display the content for uploaded files
    """
    # Descriptions
    st.write(":blue[Training up the model with train data]")


def display_content_for_no_uploaded_files():
    """
    Display the content for no uploaded files
    """
    # Descriptions
    desc = """
    **:blue[Clean up the training, validation and test data].**\n
    _To start training the models._\n
    """
    st.markdown(desc)
    sidebar.markdown(desc)

    # Load images
    st.image("resources/images/machine.svg", width=200)


if len(st.session_state) > 0:
    # Display the content for uploaded files
    display_content_for_uploaded_files()
else:
    # Display the content for no uploaded files
    display_content_for_no_uploaded_files()
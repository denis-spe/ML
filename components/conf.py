import streamlit as st
from components.load_css import load_css


def config_page(title: str, img_name: str):
    # Set the config
    st.set_page_config(page_title=title, page_icon=f"resources/images/{img_name}", layout="wide")

    # Display the logo
    with st.container():
        st.image(f"resources/images/{img_name}")
        st.title(title.replace("|", " "))

    # Load the css file
    load_css("resources/styles/style.css")
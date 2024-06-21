###
# Bless Be The Name Of The Lord #
###

# Load CSS.
def load_css(file_name):
    # Import libraries.
    import streamlit as st

    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
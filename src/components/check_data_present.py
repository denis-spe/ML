###
# Glory Be To Lord
###

# Import libraries
from typing import Callable, List
import streamlit as st

def data_present(names: List) -> bool:
    """
    Check if data is present in session state
    Parameter
    ---------
    name: List
        List of names to check
    Returns
    -------
    bool
        True if all names are present in session state
    """
    if  all([name in st.session_state for name in names]):
        return True
    return False
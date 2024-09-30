###
# Glory Be To Lord
###

# Import libraries
import streamlit as st
from components.conf import config_page
from components.charts.nan_charts import nan_chart, nan_donut

# Config the page
config_page("ML | Data Cleaning", "clean.png")


# Side bar
sidebar = st.sidebar

def display_content_for_uploaded_files():
    """
    Display the content for uploaded files
    """
    # Descriptions
    st.write(":blue[Clean up the training, validation and test data]")
    
    if "x_train" in st.session_state:
        # Fetch the x train and and x_test 
        x_train = st.session_state["x_train"]
        x_test = st.session_state["x_test"]
                
        st.write("**X Train Data Sample**")
        st.write("Some of the missing data in x_train in sample")
        train_bar_col, train_donut_col = st.columns(2)
        with train_bar_col:
            nan_chart(x_train)
        with train_donut_col:
            nan_donut(x_train)
            
        st.write("**X Validation Data Sample**")
        st.write("Missing data in validation data sample")
        test_bar_col, test_donut_col = st.columns(2)
        with test_bar_col:
            nan_chart(x_test)
        with test_donut_col:
            nan_donut(x_test)
    
    # Test data frame
    if "test" in st.session_state:
        st.write("**Test Data Frame**")
        test_df = st.session_state["test"]
        st.write("Here is the missing with data in test data frame")
        test_bar_col, test_donut_col = st.columns(2)
        with test_bar_col:
            nan_chart(test_df)
        with test_donut_col:
            nan_donut(test_df)
            
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
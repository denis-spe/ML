###
# Glory Be To Lord
###

# Import libraries
import streamlit as st
from components.conf import config_page
from sklearn.model_selection import train_test_split


# Config the page
config_page("ML | Data Split", "split.png")

# Side bar
sidebar = st.sidebar

def display_content_for_uploaded_files():
    """
    Display the content for uploaded files
    """
    # Descriptions
    st.write(":blue[Split the data into train and validation set]")

    # Get the session files
    session = st.session_state

    # Drop down selector for csv data frame
    selected_csv_name = st.selectbox(
        "Select the dataset", 
        session.keys())
    
    # Get the selected data frame
    selected_df = session[selected_csv_name]
    
    # Select the target name
    select_target_column = st.selectbox(
        "Select the target column", 
        selected_df.columns)

    # Create the x dataset
    x = selected_df.drop(select_target_column, axis=1)

    # Create the y series
    y = selected_df[select_target_column]
    
    # Inserts the test size.
    train_size = st.sidebar.number_input(
        "Train size",
        min_value=0.0, 
        max_value=1.0,
        value=0.75)
    
    # Inserts the test size.
    test_size = st.sidebar.number_input(
        "Test size",
        min_value=0.0, 
        max_value=1.0,
        value=0.25)
    
    # Random state
    random_state = st.sidebar.number_input(
        "Random state",
        min_value=0, 
        max_value=10000,
        value=42)
    
    # Create columns 
    columns = list(selected_df.columns)
    columns.insert(0, "None")
    
    strategy = st.sidebar.selectbox(
                "strategy",
                columns
                )
    
    # Shuffle the train data
    shuffle = st.sidebar.radio("Shuffle", [False, True], horizontal=True)
    

    # Split the data into train and validation set
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, 
        train_size=train_size,
        test_size=test_size, 
        random_state=int(random_state),
        shuffle=shuffle
        )

    st.write(x_train)



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
import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="👋",
)

# Change the background color of the entire page
st.markdown("""
    <style>
    body {
        background-color: #e6e6fa; /* Change this value to the desired background color */
    }
    </style>
""", unsafe_allow_html=True)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")
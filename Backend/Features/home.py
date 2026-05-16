import streamlit as st
from Frontend.F_Home import render_about_page

# Usage in your Streamlit app:
if __name__ == "__main__":
    st.set_page_config(
        page_title="About",
        layout="wide",
    )
    
    render_about_page()
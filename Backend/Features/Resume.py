import streamlit as st
import Frontend.F_Resume as ui

st.set_page_config(
    layout="wide"
)
ui.inject_css()

if "started" not in st.session_state:
    st.session_state.started = False


if not st.session_state.started:
    start = ui.landing_section1()

    if start:
        st.session_state.started = True
        st.rerun()
import streamlit as st
from Frontend.F_MergePages import style1

style1()
# -------------------------------
# NAVIGATION
# -------------------------------

# -------------------------------
# FEATURE GROUP
# -------------------------------
features = [
    st.Page("main.py", title="Assistant", icon=":material/smart_toy:"),
    st.Page("CodeEditor.py", title="Code/Debug", icon=":material/code:"),
    st.Page("Image.py", title="ImageLab", icon=":material/image:"),
    st.Page("PromptEng.py", title="PromptLab", icon=":material/edit_note:"),
    st.Page("Scholar.py", title="Jarvis Scholar", icon=":material/search:"),
    st.Page("Resume.py", title="Jarvis Resume", icon=":material/draft:")
]

# -------------------------------
# MAIN NAVIGATION
# -------------------------------
pages = {
    "Account": [
        st.Page(
            "account.py",
            title="Account",
            icon=":material/account_circle:"
        )
    ],

    "About": [
        st.Page(
            "home.py",
            title="About",
            icon=":material/home:",
            default=True
        )
    ],

    "Features": features
}

# -------------------------------
# RUN APP
# -------------------------------
app = st.navigation(pages)
app.run()
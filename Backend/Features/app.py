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
    st.Page("CodeEditor.py", title="Code/Debug", icon=":material/code:"),
    st.Page("PromptEng.py", title="PromptLab", icon=":material/edit_note:"),
    st.Page("Scholar.py", title="Scholar", icon=":material/search:"),
    st.Page("Resume.py", title="Resume", icon=":material/draft:"),
    st.Page("main.py", title="Assistant", icon=":material/smart_toy:"),
    st.Page("Image.py", title="ImageLab", icon=":material/image:")
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

    "Features":features,

    "Settings":[
        st.Page(
            "settings/settingsMaterials.py",
            title="Settings",
            icon=":material/settings:"
        )
    ]
}

# -------------------------------
# RUN APP
# -------------------------------
app = st.navigation(pages)
app.run()
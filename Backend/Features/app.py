import streamlit as st
from Frontend.F_MergePages import style1

style1()
# -------------------------------
# NAVIGATION
# -------------------------------

# -------------------------------
# FEATURE GROUP 1
# -------------------------------
features_for_devs = [
    st.Page("code_editor.py", title="Code/Debug", icon=":material/code:"),
    st.Page("prompt_eng.py", title="PromptLab", icon=":material/edit_note:"),
    st.Page("scholar.py", title="Scholar", icon=":material/search:"),
    st.Page("resume.py", title="Resume", icon=":material/draft:")
]

# -------------------------------
# FEATURE GROUP 2
# -------------------------------
features_for_everyone = [
    
    st.Page("main.py", title="Assistant", icon=":material/smart_toy:"),
    st.Page("image.py", title="ImageLab", icon=":material/image:")
]

# -------------------------------
# MAIN NAVIGATION
# -------------------------------
pages = {
    "Account": [
        st.Page(
            "account.py",
            title="account",
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

    "Everyone's choice":features_for_everyone,

    "Developer's choice":features_for_devs,

    "Settings":[
        st.Page(
            "settings/settings_materials.py",
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
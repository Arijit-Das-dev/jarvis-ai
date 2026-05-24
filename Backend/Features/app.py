import streamlit as st
from Frontend.F_MergePages import style1

style1()
# -------------------------------
# NAVIGATION
# -------------------------------
account_page = st.Page("account.py", title="Account", icon=":material/account_circle:")
home_page = st.Page("home.py", title="About", icon=":material/home:", default=True)
main_page = st.Page("main.py", title="Assistant", icon=":material/smart_toy:")
code_page = st.Page("CodeEditor.py", title="Code/Debug", icon=":material/code:")
image_page = st.Page("Image.py", title="ImageLab", icon=":material/image:")
prompt_eng_page = st.Page("PromptEng.py", title="PromptLab", icon=":material/edit_note:")
Jarvis_scholar_page = st.Page("Scholar.py", title="Scholar", icon=":material/search:")
jarvis_resume = st.Page("Resume.py", title="Resume", icon=":material/draft:")
pages = [account_page,home_page, main_page, code_page, image_page, prompt_eng_page, Jarvis_scholar_page, jarvis_resume]

app = st.navigation(pages)
app.run()
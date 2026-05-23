import re
import streamlit as st
import Frontend.F_Resume as ui
from Backend.Core.Features.ResumeBuilder.pdf_parser import PDF_PARSER
from Backend.Services.OpenRouterClient.gpt_client import MODEL_GPT

# CUSTOM CSS
ui.inject_css()


# SESSION STATES
if "current_page" not in st.session_state:
    st.session_state.current_page = "landing"

# LANDING PAGE
if st.session_state.current_page == "landing":

    if ui.landing_section1():
        st.session_state.current_page = "features"
        st.rerun()

# FEATURES PAGE
elif st.session_state.current_page == "features":

    col1, col2 = st.columns(2, gap="xxsmall")

    with col1:

        if ui.resumeBuilder():

            st.session_state.current_page = "builder"
            st.rerun()

    with col2:

        if ui.resumeAnalysis():

            st.session_state.current_page = "analysis"
            st.rerun()

# RESUME ANALYSIS PAGE
elif st.session_state.current_page == "builder":
    st.success("success")


# RESUME BUILDER PAGE
elif st.session_state.current_page == "analysis":

    ui.heading()
    col1, col2, col3 = st.columns(3, gap="xxsmall")

    if "output" not in st.session_state:
        st.session_state.output = None

    with col1:

        file = st.file_uploader(
            label="Upload your resume here",
            help="Only pdf files are supported.",
            type=["pdf"]
        )
        
    with col2:
        pdf_parser = PDF_PARSER()
        container_1 = st.container(height=300)
        modelGpt = MODEL_GPT()

        with container_1:

            role = st.text_input("Enter your job role")

            if role:
                analyse = st.button("Start analyzing")
                
                if analyse:
                    ui.parsing_loader()
                    content = pdf_parser.extract_from_upload(upload_file=file)
                    st.success("Pdf parsed successfully")
                    st.divider()

                    st.info("Analysis", icon="ℹ️")
                    output = modelGpt.askGpt(
                        content = content,
                        role=role
                    )
                    st.session_state.output = output
                    st.markdown(output)
        
    with col3:

        container_2 = st.container(height=300)

        with container_2:
            output = st.session_state.get("output")

            if output:
                match = re.search(r'ATS SCORE:\s*(\d+)', output)
                ats_score = int(match.group(1)) if match else 0
                ui.show_ats_score(score=ats_score)
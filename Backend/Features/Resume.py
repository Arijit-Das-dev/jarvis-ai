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

    contents = None

    ui.heading()
    col1, col2, col3 = st.columns(3, gap="xxsmall")
    
    with col2:
        
        # PDF PARSER MODULE
        pdf_parser = PDF_PARSER()

        file = st.file_uploader(
            "Upload resume",
            help="Only pdf files are supported",
            type=["pdf"]
        )
        if file:
            ui.parsing_loader()
            contents = pdf_parser.extract_from_upload(upload_file=file)
            st.success("pdf parsed successfully")
            ui.analyzing_resume()
            pdf_parser.resume_Details(pdf_path=file)

    with col1:
        
        modelGpt = MODEL_GPT()

        container_1 = st.container(height=300)

        with container_1:

            role = st.text_input("Enter your job role here.")
            st.divider()
            
            if contents and role:

                output = modelGpt.askGpt(
                    content=contents,
                    role=role
                )
                st.markdown(output)
                
    with col3:
        container_2 = st.container(height=300)

        with container_2:
            st.success("Container success")
import re
import os
import sys
import streamlit as st
import Frontend.F_Resume as ui
from Backend.Core.Features.ResumeBuilder.pdf_parser import PDF_PARSER
from Backend.Services.OpenRouterClient.gpt_client import MODEL_GPT

# CUSTOM CSS
ui.inject_css()
ui.inject_css_2()

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

    ui.hero_section()
    ui.template_section()
    st.divider()

    col1, col2, col3, col4 = st.columns(4, gap="xxsmall")

    with col1:

        template = st.selectbox(
            options=["Minimal", "Classic", "Modern"],
            label="Select template below",
            index=None,
            placeholder="Select resume template..."
        )
    st.divider()

    col5, col6 = st.columns(2, gap="large")

    with col5:
        ui.Personal_Information()
        name = st.text_input("Full Name", placeholder="John Doe")
        email = st.text_input("Email address", placeholder="xyz@gmail.com")
        phone = st.text_input("Phone", placeholder="xxxxxxxxxxxxx")
        location = st.text_input("Location", placeholder="London")
        summary = st.text_area("Professional summary")

    with col6:
        ui.Work_Experience()
        role = st.text_input("Job Role")
        company = st.text_input("Company")
        duration = st.text_input("Duration")
        description = st.text_area("Job Description")

    st.divider()

    col7, col8 = st.columns(2, gap="large")

    with col7:
        ui.Education()
        degree = st.text_input("Degree")
        college = st.text_input("College")
        year = st.text_input("Passing Year")

    with col8:
        ui.Technical_Skills()
        skills = st.text_input("Skills (comma separated)")

    st.divider()
    
    col9, col10 = st.columns(2, gap="large")

    with col9:
        ui.Projects()
        project_title = st.text_input("Project Title")
        project_tech = st.text_input("Project Technologies")
        project_description = st.text_area("Project Description")

    with col10:
        ui.Certifications()
        cert_name = st.text_input("Certification Name")
        cert_issuer = st.text_input("Issued By")
        cert_year = st.text_input("Certification Year")


# RESUME BUILDER PAGE
elif st.session_state.current_page == "analysis":

    ui.heading()
    st.divider()
    col1, col2, col3 = st.columns(3, gap="xxsmall")

    if "output" not in st.session_state:
        st.session_state.output = None

    with col1:

        ui.subheader(text="Upload File")
        file = st.file_uploader(
            label="Upload your resume here",
            help="Only pdf files are supported.",
            type=["pdf"]
        )
    
    with col2:

        ui.subheader(text="Analyze resume")
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

        ui.subheader(text="ATS SCORE")
        container_2 = st.container(height=300)
        with container_2:
            output = st.session_state.get("output")

            if output:
                match = re.search(r'ATS SCORE:\s*(\d+)', output)
                ats_score = int(match.group(1)) if match else 0
                ui.show_ats_score(score=ats_score)
import re
import pandas as pd
import streamlit as st
import Frontend.F_Resume as ui
from Backend.Core.Features.ResumeBuilder.pdf_parser import PDF_PARSER
from Backend.Services.openrouter_client.resume_analysis.openai_client import MODEL_GPT
from Backend.models.resume_essentials.essentials import ResumeEssentials
from Backend.Core.Features.ResumeBuilder.resume_builder import generate_resume

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
    st.divider()
    # Enter your details here
    

    # PERSONAL INFORMATION
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        ui.Personal_Information()
        name = st.text_input("Enter your name...")
        phone = st.text_input("Enter your phone number...")
        email = st.text_input("Enter your email...")
        location = st.text_input("Enter your location...")
        linkedin = st.text_input("Enter your linkedin profile...")
        github = st.text_input("Enter your github profile link...")
        summary = st.text_area("Write some info about yourself...", height=200)

    # TECHNICAL SKILLS
    with col2:
        ui.Technical_Skills()
        skills_df = st.data_editor(
                    pd.DataFrame({
                        "Category": [
                            "Languages",
                            "Frameworks & Libraries",
                            "Databases",
                            "Tools & DevOps",
                        ],
                        "Skills (comma-separated)": [""] * 4,
                    }),
                    num_rows="dynamic",
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "Category": st.column_config.TextColumn("Category", width="medium"),
                        "Skills (comma-separated)": st.column_config.TextColumn("Skills", width="large"),
                    },
                    key="skills_editor",
                )
    
    # WORK EXPERIENCE
    st.divider()
    col3, col4 = st.columns(2, gap="medium")

    resume_esen = ResumeEssentials()

    with col3:
        ui.Work_Experience()
        
        exp_num = st.number_input("Number of experiences you have", min_value=0, max_value=10, value=0, step=1)

        for i in range(exp_num):
            st.subheader(f"Experience {i+1}")

            exp_title = st.text_input("Job title", key=f"exp_title_{i}")
            exp_company = st.text_input("Company name", key=f"exp_company_{i}")
            exp_loc = st.text_input("Location", key=f"exp_loc_{i}")
            exp_start = st.text_input("Start date", key=f"exp_start_{i}")
            exp_end = st.text_input("End date", key=f"exp_end_{i}")
            exp_bullets_raw = st.text_area(
                "Achievements / Responsibilities (one per line)",
                key=f"exp_bullets_{i}",
                placeholder=(
                    "Built a RAG pipeline using Cohere API, increasing response relevance by 18%.\n"
                    "Reduced deployment time by 40% by setting up GitHub Actions CI/CD."
                ),
                height=120,
            )
            bullets = [b.strip() for b in exp_bullets_raw.splitlines() if b.strip()]

            experience = resume_esen.experience(
                title=exp_title, 
                company=exp_company, 
                location=exp_loc, 
                start_date=exp_start, 
                end_date=exp_end,
                bullets=bullets
                )

    # EDUCATION
    with col4:
        ui.Education()
        num_edu = st.number_input("Number of education entries: (UG / PG/ UG & PG)",  min_value=0, max_value=5, value=1, step=1)

        for i in range(num_edu):
            st.subheader(f"Education {i + 1}")
        
            edu_degree  = st.text_input("Degree / Qualification", key=f"edu_degree_{i}",  placeholder="Bachelor of Computer Applications")
            edu_inst    = st.text_input("Institution",            key=f"edu_inst_{i}",    placeholder="Example University")
            edu_loc     = st.text_input("Location",               key=f"edu_loc_{i}",     placeholder="Kolkata, WB")
            edu_gpa     = st.text_input("GPA / Percentage (optional)", key=f"edu_gpa_{i}", placeholder="8.7 / 10")
            edu_start = st.text_input("Start Year", key=f"edu_start_{i}", placeholder="2022")
            edu_end   = st.text_input("End Year",   key=f"edu_end_{i}",   placeholder="2025")
        
            edu_courses_raw = st.text_input(
                "Relevant Courses (comma-separated, optional)",
                key=f"edu_courses_{i}",
                placeholder="Machine Learning, Data Structures, Cloud Computing",
            )

            relevant_courses = [c.strip() for c in edu_courses_raw.split(",") if c.strip()]

            education = resume_esen.education(
                degree=edu_degree, 
                institution=edu_inst, 
                location=edu_loc, 
                start_date=edu_start, 
                end_date=edu_end, 
                gpa=edu_gpa, 
                relevant_courses=relevant_courses
            )

    # PROJECTS
    st.divider()
    col5, col6 = st.columns(2, gap="medium")

    with col5:
        ui.Projects()
        num_proj = st.number_input("Number of projects",  min_value=0, max_value=10, value=0, step=1)

        for i in range(num_proj):
            st.subheader(f"Project {i + 1}")
        
            proj_name  = st.text_input("Project Name",  key=f"proj_name_{i}",  placeholder="PromptLab")
            proj_stack = st.text_input("Tech Stack",    key=f"proj_stack_{i}", placeholder="Python, Streamlit, Gemini API")
            proj_link  = st.text_input("GitHub / Live Link (optional)", key=f"proj_link_{i}", placeholder="github.com/you/project")
            proj_bullets_raw = st.text_area(
                "Key points (one per line)",
                key=f"proj_bullets_{i}",
                placeholder=(
                    "Built a structured prompt generation tool with tone/length controls.\n"
                    "Supports 12 prompt templates used by 200+ beta testers."
                ),
                height=200,
            )
            
            proj_bull = [b.strip() for b in proj_bullets_raw.splitlines() if b.strip()]

            projects = resume_esen.projects(
                name=proj_name,
                tech_stack=proj_stack,
                link=proj_link,
                bullets=proj_bull
            )
    
    # CERTIFICATIONS
    with col6:
        ui.Certifications()
        st.caption("Leave rows blank to skip.")
 
        certs_df = st.data_editor(
            pd.DataFrame({
                "Certificate Name":  [""] * 3,
                "Issuing Body":      [""] * 3,
                "Date":              [""] * 3,
                "Credential ID / URL (optional)": [""] * 3,
                }),
                num_rows="dynamic",
                use_container_width=True,
                hide_index=True,
                key="certs_editor",
            )
    
    # ACHIEVEMENTS
    st.divider()
    col7, col8 = st.columns(2, gap="medium")

    with col7:
        ui.achievements()
        achievements_raw = st.text_area(
        "One achievement per line",
        placeholder=(
            "Organised SAVISHKAR – national-level startup summit with 30+ exhibitor teams.\n"
            "Ranked Top 5% on Kaggle time-series forecasting competition (1,200+ participants)."
        ),
        height=200,
        )
        achievements = [a.strip() for a in achievements_raw.splitlines() if a.strip()]
    
    # LANGUAGES
    with col8:
        ui.languages()
        languages_raw = st.text_input(
        "Spoken languages (comma-separated)",
        placeholder="English (Fluent), Bengali (Native), Hindi (Conversational)",
        )
        languages = [l.strip() for l in languages_raw.split(",") if l.strip()]

    # GENERATE RESUME
    st.divider()
    col, _, _, _, _, _ = st.columns(6)

    with col:

        if st.button("Generate Resume", use_container_width=True):
    
            # Parse skills df
            skills_dict = {}
            for _, row in skills_df.iterrows():
                label = str(row["Category"]).strip()
                items = [s.strip() for s in str(row["Skills (comma-separated)"]).split(",") if s.strip()]
                if label and items:
                    skills_dict[label] = items
        
            # Parse certifications df
            certs_list = []
            for _, row in certs_df.iterrows():
                cert_name = str(row["Certificate Name"]).strip()
                if cert_name:
                    certs_list.append({
                        "name":       cert_name,
                        "issuer":     str(row["Issuing Body"]).strip(),
                        "date":       str(row["Date"]).strip(),
                        "credential": str(row["Credential ID / URL (optional)"]).strip(),
                    })
            
            # assemble full data dict {}
            data = resume_esen.data(
                name=name,
                email=email,
                phone=phone,
                location=location,
                linkedin=linkedin,
                github=github,
                summary=summary,
                skills=skills_dict,
                experience=experience,
                education=education,
                projects=projects,
                certifications=certs_list,
                achievements=achievements,
                languages=languages
            )

            with st.spinner("Building your resume..."):
                try:
                    pdf_bytes = generate_resume(data)
                    st.success("Resume generated!")
                    st.download_button(
                        label="⬇ Download Resume (PDF)",
                        data=pdf_bytes,
                        file_name=f"{name.strip().replace(' ', '_') or 'resume'}.pdf",
                        mime="application/pdf",
                        use_container_width=True,
                    )
                except Exception as e:
                    st.error(f"Something went wrong: {e}")


# RESUME ANALYSIS 
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
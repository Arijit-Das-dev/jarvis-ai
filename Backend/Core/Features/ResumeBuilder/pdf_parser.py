import os
import tempfile
import pdfplumber
import streamlit as st
from pypdf import PdfReader

class PDF_PARSER:

    def __init__(self):
        
        self.pdf_plumber = pdfplumber
        self.temp_file = tempfile
        
    """ EXTRACT TEXT FROM streamlit st.file_uploader() OUTPUT"""
    def extract_from_upload(self, upload_file) -> str:

        with self.temp_file.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:

            tmp.write(upload_file.read())
            tmp_path = tmp.name

        text = ""

        with self.pdf_plumber.open(tmp_path) as pdf:

            for page in pdf.pages:
                page_txt = page.extract_text()
                if page_txt:
                    text += page_txt + "\n"
        
        os.unlink(tmp_path)
        print(" ========== PDF CONTENT EXTRACTED SUCCESSFULLY ========== ")

        return text.strip()
    
    """ RESUME METADATA """
    def resume_Details(self, uploaded_file) -> dict:

        if uploaded_file is None:
            return {}
        
        reader = PdfReader(uploaded_file)
        info = reader.metadata

        details = {
            "title": info.title,
            "pages": len(reader.pages),
            "created": info.creation_date
        }

        st.info(f"Resume title : {details["title"]}")
        st.info(f"Total number of Pages :{details["pages"]}")
        st.info(f"Created at :{details["created"]}")
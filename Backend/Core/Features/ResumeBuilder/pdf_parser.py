import os
import tempfile
import pdfplumber
import streamlit as st

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
    def resume_Details(self, pdf_path) -> dict:

        result = {
            "total_pages":0,
        }

        with self.pdf_plumber.open(pdf_path) as pdf:

            total_pages = len(pdf.pages)

            result["total_pages"] = total_pages

            if len(total_pages) > 1:

                st.info("Resume must contains 1 page !!!")

        return result              
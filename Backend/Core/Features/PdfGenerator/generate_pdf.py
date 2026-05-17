from fpdf import FPDF
import datetime

class PDF_GENERATOR:

    def __init__(self):  
        self.pdf = FPDF()


    def GeneratePdf(self, notes_text: str, subject: str) -> bytes:
        
        self.pdf.add_page()
        self.pdf.set_margins(20, 20, 20)
        

        # --- HEADER ---
        self.pdf.set_font("Helvetica", "B", 20)
        self.pdf.cell(0, 12, subject, ln=True)

        self.pdf.set_font("Helvetica", "", 10)
        self.pdf.set_text_color(120, 120, 120)
        self.pdf.cell(0, 8, f"Generated on {datetime.date.today()}", ln=True)
        self.pdf.ln(6)

        # --- Parse and write lines ---
        self.pdf.set_text_color(0, 0, 0)

        for line in notes_text.split("\n"):
            line = line.strip()
            if not line:
                self.pdf.ln(4)  # empty line = small gap
                continue

            # Section headings (lines ending with ":")
            if line.endswith(":"):
                self.pdf.ln(4)
                self.pdf.set_font("Helvetica", "B", 13)
                self.pdf.cell(0, 9, line, ln=True)
                self.pdf.set_font("Helvetica", "", 11)

            # Bullet points
            elif line.startswith("-"):
                self.pdf.set_x(25)  # indent
                self.pdf.multi_cell(0, 7, f"  {line}", ln=True)

            # Normal text
            else:
                self.pdf.set_font("Helvetica", "", 11)
                self.pdf.multi_cell(0, 7, line, ln=True)

        # --- Return as bytes (for Streamlit download) ---
        return bytes(self.pdf.output())
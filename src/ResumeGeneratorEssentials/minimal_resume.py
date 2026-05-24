from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import io


# ── Color Palette ──────────────────────────────────────────────────────────────
BLACK       = colors.HexColor("#111111")
DARK_GRAY   = colors.HexColor("#333333")
MID_GRAY    = colors.HexColor("#666666")
LIGHT_GRAY  = colors.HexColor("#cccccc")
WHITE       = colors.white

PAGE_W, PAGE_H = A4
ML = 18 * mm   # margin left
MR = 18 * mm   # margin right
MT = 16 * mm   # margin top
CONTENT_W = PAGE_W - ML - MR


def _draw_paragraph(c, text, x, y, width, style):
    """Draw a Paragraph and return the height it consumed."""
    p = Paragraph(text, style)
    w, h = p.wrap(width, 999)
    p.drawOn(c, x, y - h)
    return h


def generate_minimal_resume(data: dict) -> bytes:
    """
    Generate a Minimal ATS-friendly resume PDF.

    data = {
        "name":           str,
        "job_title":      str,
        "email":          str,
        "phone":          str,
        "location":       str,
        "linkedin":       str,   # optional
        "github":         str,   # optional
        "summary":        str,
        "experience": [
            {
                "role":     str,
                "company":  str,
                "duration": str,
                "bullets":  [str, ...]
            }, ...
        ],
        "education": [
            {
                "degree":      str,
                "institution": str,
                "year":        str
            }, ...
        ],
        "skills":   [str, ...],
        "projects": [
            {
                "name":        str,
                "tech":        str,
                "description": str
            }, ...
        ],
        "certifications": [str, ...]   # optional
    }
    """

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    # ── Paragraph Styles ───────────────────────────────────────────────────────
    style_name = ParagraphStyle(
        "name", fontName="Helvetica-Bold",
        fontSize=22, textColor=BLACK,
        leading=26, alignment=TA_LEFT
    )
    style_title = ParagraphStyle(
        "title", fontName="Helvetica",
        fontSize=11, textColor=MID_GRAY,
        leading=14, alignment=TA_LEFT
    )
    style_contact = ParagraphStyle(
        "contact", fontName="Helvetica",
        fontSize=8.5, textColor=MID_GRAY,
        leading=12, alignment=TA_LEFT
    )
    style_section = ParagraphStyle(
        "section", fontName="Helvetica-Bold",
        fontSize=8, textColor=BLACK,
        leading=10, alignment=TA_LEFT,
        spaceAfter=2
    )
    style_item_title = ParagraphStyle(
        "item_title", fontName="Helvetica-Bold",
        fontSize=9, textColor=DARK_GRAY,
        leading=12
    )
    style_item_sub = ParagraphStyle(
        "item_sub", fontName="Helvetica",
        fontSize=8, textColor=MID_GRAY,
        leading=11
    )
    style_bullet = ParagraphStyle(
        "bullet", fontName="Helvetica",
        fontSize=8, textColor=DARK_GRAY,
        leading=11, leftIndent=8,
        bulletIndent=0
    )
    style_summary = ParagraphStyle(
        "summary", fontName="Helvetica",
        fontSize=8.5, textColor=DARK_GRAY,
        leading=13
    )
    style_skill = ParagraphStyle(
        "skill", fontName="Helvetica",
        fontSize=8, textColor=DARK_GRAY,
        leading=11
    )

    # ── Cursor ─────────────────────────────────────────────────────────────────
    y = PAGE_H - MT

    def check_space(needed=20):
        """Start a new page if not enough vertical space."""
        nonlocal y
        if y < needed + 15 * mm:
            c.showPage()
            y = PAGE_H - MT

    # ── Header — Name ──────────────────────────────────────────────────────────
    h = _draw_paragraph(c, data.get("name", ""), ML, y, CONTENT_W, style_name)
    y -= h + 2

    # Job Title
    if data.get("job_title"):
        h = _draw_paragraph(c, data["job_title"], ML, y, CONTENT_W, style_title)
        y -= h + 4

    # Contact line  (email · phone · location · linkedin · github)
    contact_parts = []
    for field in ["email", "phone", "location", "linkedin", "github"]:
        val = data.get(field, "").strip()
        if val:
            contact_parts.append(val)
    contact_line = "  ·  ".join(contact_parts)
    h = _draw_paragraph(c, contact_line, ML, y, CONTENT_W, style_contact)
    y -= h + 5

    # Divider
    c.setStrokeColor(LIGHT_GRAY)
    c.setLineWidth(0.5)
    c.line(ML, y, PAGE_W - MR, y)
    y -= 7

    # ── Helper: Section Header ─────────────────────────────────────────────────
    def draw_section_header(title: str):
        nonlocal y
        check_space(30)
        section_text = title.upper()
        h = _draw_paragraph(c, section_text, ML, y, CONTENT_W, style_section)
        y -= h + 2
        c.setStrokeColor(LIGHT_GRAY)
        c.setLineWidth(0.4)
        c.line(ML, y, PAGE_W - MR, y)
        y -= 5

    # ── Summary ────────────────────────────────────────────────────────────────
    if data.get("summary", "").strip():
        draw_section_header("Summary")
        h = _draw_paragraph(c, data["summary"], ML, y, CONTENT_W, style_summary)
        y -= h + 10

    # ── Experience ─────────────────────────────────────────────────────────────
    if data.get("experience"):
        draw_section_header("Experience")
        for exp in data["experience"]:
            check_space(40)

            # Role + Duration on same line
            role    = exp.get("role", "")
            company = exp.get("company", "")
            duration= exp.get("duration", "")

            # Role bold left, duration right
            role_text = f"<b>{role}</b>"
            h = _draw_paragraph(c, role_text, ML, y, CONTENT_W * 0.70, style_item_title)

            # Duration — right aligned
            c.setFont("Helvetica", 7.5)
            c.setFillColor(MID_GRAY)
            c.drawRightString(PAGE_W - MR, y - h + 3, duration)
            y -= h + 1

            # Company
            if company:
                h = _draw_paragraph(c, company, ML, y, CONTENT_W, style_item_sub)
                y -= h + 2

            # Bullets
            for bullet in exp.get("bullets", []):
                check_space(15)
                h = _draw_paragraph(c, f"• {bullet}", ML, y, CONTENT_W, style_bullet)
                y -= h + 1

            y -= 7

    # ── Education ──────────────────────────────────────────────────────────────
    if data.get("education"):
        draw_section_header("Education")
        for edu in data["education"]:
            check_space(30)
            degree  = edu.get("degree", "")
            inst    = edu.get("institution", "")
            year    = edu.get("year", "")

            h = _draw_paragraph(c, f"<b>{degree}</b>", ML, y, CONTENT_W * 0.75, style_item_title)
            c.setFont("Helvetica", 7.5)
            c.setFillColor(MID_GRAY)
            c.drawRightString(PAGE_W - MR, y - h + 3, year)
            y -= h + 1

            if inst:
                h = _draw_paragraph(c, inst, ML, y, CONTENT_W, style_item_sub)
                y -= h + 7

    # ── Skills ─────────────────────────────────────────────────────────────────
    if data.get("skills"):
        draw_section_header("Skills")
        skills_text = "  ·  ".join(data["skills"])
        h = _draw_paragraph(c, skills_text, ML, y, CONTENT_W, style_skill)
        y -= h + 10

    # ── Projects ───────────────────────────────────────────────────────────────
    if data.get("projects"):
        draw_section_header("Projects")
        for proj in data["projects"]:
            check_space(35)
            name = proj.get("name", "")
            tech = proj.get("tech", "")
            desc = proj.get("description", "")

            h = _draw_paragraph(c, f"<b>{name}</b>", ML, y, CONTENT_W, style_item_title)
            y -= h + 1

            if tech:
                h = _draw_paragraph(c, f"Tech: {tech}", ML, y, CONTENT_W, style_item_sub)
                y -= h + 2

            if desc:
                h = _draw_paragraph(c, f"• {desc}", ML, y, CONTENT_W, style_bullet)
                y -= h + 1

            y -= 6

    # ── Certifications ─────────────────────────────────────────────────────────
    if data.get("certifications"):
        draw_section_header("Certifications")
        for cert in data["certifications"]:
            check_space(15)
            h = _draw_paragraph(c, f"• {cert}", ML, y, CONTENT_W, style_bullet)
            y -= h + 2

    c.save()
    buffer.seek(0)
    return buffer.read()
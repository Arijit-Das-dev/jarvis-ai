from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import io


# ── Color Palette ──────────────────────────────────────────────────────────────
NAVY        = colors.HexColor("#2c3e50")
NAVY_LIGHT  = colors.HexColor("#34495e")
WHITE       = colors.white
OFF_WHITE   = colors.HexColor("#ecf0f1")
SILVER      = colors.HexColor("#bdc3c7")
DARK_TEXT   = colors.HexColor("#222222")
BODY_GRAY   = colors.HexColor("#444444")
MID_GRAY    = colors.HexColor("#777777")
SKILL_TAG   = colors.HexColor("#ecf0f1")
SKILL_TEXT  = colors.HexColor("#2c3e50")
DIVIDER     = colors.HexColor("#cccccc")

PAGE_W, PAGE_H = A4
HEADER_H    = 30 * mm
ML          = 14 * mm
MR          = 14 * mm
BODY_TOP    = PAGE_H - HEADER_H - 6 * mm
MAIN_COL_W  = (PAGE_W - ML - MR) * 0.62
SIDE_COL_X  = ML + MAIN_COL_W + 8 * mm
SIDE_COL_W  = PAGE_W - SIDE_COL_X - MR
MAIN_COL_X  = ML


def _draw_paragraph(c, text, x, y, width, style):
    p = Paragraph(text, style)
    w, h = p.wrap(width, 999)
    p.drawOn(c, x, y - h)
    return h


def generate_classic_resume(data: dict) -> bytes:
    """
    Generate a Classic formal resume with navy header + two-column body.

    data = {
        "name":       str,
        "job_title":  str,
        "email":      str,
        "phone":      str,
        "location":   str,
        "linkedin":   str,
        "github":     str,
        "summary":    str,
        "experience": [ { "role", "company", "duration", "bullets": [] } ],
        "education":  [ { "degree", "institution", "year" } ],
        "skills":     [ str, ... ],
        "projects":   [ { "name", "tech", "description" } ],
        "certifications": [ str, ... ]
    }
    """

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    # ── Paragraph Styles ──────────────────────────────────────────────────────
    style_name = ParagraphStyle(
        "name", fontName="Helvetica-Bold",
        fontSize=20, textColor=WHITE,
        leading=24, alignment=TA_LEFT
    )
    style_header_title = ParagraphStyle(
        "hdr_title", fontName="Helvetica",
        fontSize=9, textColor=SILVER,
        leading=12, alignment=TA_LEFT
    )
    style_header_contact = ParagraphStyle(
        "hdr_contact", fontName="Helvetica",
        fontSize=7.5, textColor=OFF_WHITE,
        leading=11
    )
    style_section = ParagraphStyle(
        "section", fontName="Helvetica-Bold",
        fontSize=7.5, textColor=NAVY,
        leading=10
    )
    style_item_title = ParagraphStyle(
        "item_title", fontName="Helvetica-Bold",
        fontSize=8.5, textColor=DARK_TEXT,
        leading=11
    )
    style_item_sub = ParagraphStyle(
        "item_sub", fontName="Helvetica",
        fontSize=7.5, textColor=MID_GRAY,
        leading=11
    )
    style_bullet = ParagraphStyle(
        "bullet", fontName="Helvetica",
        fontSize=7.5, textColor=BODY_GRAY,
        leading=11, leftIndent=8
    )
    style_summary = ParagraphStyle(
        "summary", fontName="Helvetica",
        fontSize=8, textColor=BODY_GRAY,
        leading=13
    )
    style_skill_text = ParagraphStyle(
        "skill", fontName="Helvetica",
        fontSize=7.5, textColor=BODY_GRAY,
        leading=11
    )

    # ── HEADER ────────────────────────────────────────────────────────────────
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - HEADER_H, PAGE_W, HEADER_H, fill=1, stroke=0)

    # Thin accent strip at bottom of header
    c.setFillColor(NAVY_LIGHT)
    c.rect(0, PAGE_H - HEADER_H, PAGE_W, 1.5 * mm, fill=1, stroke=0)

    hy = PAGE_H - 9 * mm

    # Name
    h = _draw_paragraph(c, data.get("name", ""), ML, hy, PAGE_W - ML - MR, style_name)
    hy -= h + 2

    # Job title
    if data.get("job_title"):
        h = _draw_paragraph(c, data["job_title"], ML, hy,
                             PAGE_W - ML - MR, style_header_title)
        hy -= h + 3

    # Contact row
    contact_parts = []
    for field in ["email", "phone", "location", "linkedin", "github"]:
        val = data.get(field, "").strip()
        if val:
            contact_parts.append(val)
    contact_line = "   |   ".join(contact_parts)
    _draw_paragraph(c, contact_line, ML, hy, PAGE_W - ML - MR, style_header_contact)

    # ── BODY: Professional Summary (full width) ───────────────────────────────
    my = BODY_TOP   # main col y cursor
    sy = BODY_TOP   # side col y cursor

    def draw_section_header(title, x, width, y):
        """Draw section header + underline, return new y."""
        h = _draw_paragraph(c, title.upper(), x, y, width, style_section)
        y -= h + 2
        c.setStrokeColor(NAVY)
        c.setLineWidth(0.7)
        c.line(x, y, x + width, y)
        y -= 5
        return y

    # Summary — spans full content width
    if data.get("summary", "").strip():
        full_w = PAGE_W - ML - MR
        my = draw_section_header("Professional Summary", ML, full_w, my)
        h = _draw_paragraph(c, data["summary"], ML, my, full_w, style_summary)
        my -= h + 10
        sy = my  # sync side col to same level

    # ── MAIN column — Experience + Projects ───────────────────────────────────
    def check_main(needed=25):
        nonlocal my
        if my < needed + 15 * mm:
            c.showPage()
            my = PAGE_H - 14 * mm

    def check_side(needed=25):
        nonlocal sy
        if sy < needed + 15 * mm:
            sy = my  # fall back to main col level

    # Experience
    if data.get("experience"):
        my = draw_section_header("Experience", MAIN_COL_X, MAIN_COL_W, my)
        for exp in data["experience"]:
            check_main(40)
            role     = exp.get("role", "")
            company  = exp.get("company", "")
            duration = exp.get("duration", "")

            # Role + date row
            h = _draw_paragraph(c, f"<b>{role}</b>", MAIN_COL_X, my,
                                 MAIN_COL_W * 0.70, style_item_title)
            c.setFont("Helvetica", 7)
            c.setFillColor(MID_GRAY)
            c.drawRightString(MAIN_COL_X + MAIN_COL_W, my - h + 3, duration)
            my -= h + 1

            if company:
                h = _draw_paragraph(c, company, MAIN_COL_X, my,
                                    MAIN_COL_W, style_item_sub)
                my -= h + 2

            for bullet in exp.get("bullets", []):
                check_main(14)
                h = _draw_paragraph(c, f"• {bullet}", MAIN_COL_X, my,
                                    MAIN_COL_W, style_bullet)
                my -= h + 1
            my -= 8

    # Projects
    if data.get("projects"):
        my = draw_section_header("Projects", MAIN_COL_X, MAIN_COL_W, my)
        for proj in data["projects"]:
            check_main(35)
            name = proj.get("name", "")
            tech = proj.get("tech", "")
            desc = proj.get("description", "")

            h = _draw_paragraph(c, f"<b>{name}</b>", MAIN_COL_X, my,
                                 MAIN_COL_W, style_item_title)
            my -= h + 1

            if tech:
                h = _draw_paragraph(c, f"Stack: {tech}", MAIN_COL_X, my,
                                    MAIN_COL_W, style_item_sub)
                my -= h + 2

            if desc:
                h = _draw_paragraph(c, f"• {desc}", MAIN_COL_X, my,
                                    MAIN_COL_W, style_bullet)
                my -= h + 1
            my -= 7

    # ── SIDE column — Education + Skills + Certifications ────────────────────

    # Education
    if data.get("education"):
        sy = draw_section_header("Education", SIDE_COL_X, SIDE_COL_W, sy)
        for edu in data["education"]:
            degree = edu.get("degree", "")
            inst   = edu.get("institution", "")
            year   = edu.get("year", "")

            h = _draw_paragraph(c, f"<b>{degree}</b>", SIDE_COL_X, sy,
                                 SIDE_COL_W, style_item_title)
            sy -= h + 1

            if inst:
                h = _draw_paragraph(c, inst, SIDE_COL_X, sy,
                                    SIDE_COL_W, style_item_sub)
                sy -= h + 1

            if year:
                h = _draw_paragraph(c, year, SIDE_COL_X, sy,
                                    SIDE_COL_W, style_item_sub)
                sy -= h + 8

    # Skills — pill tags
    if data.get("skills"):
        sy = draw_section_header("Skills", SIDE_COL_X, SIDE_COL_W, sy)
        sx = SIDE_COL_X
        tag_h = 5 * mm
        tag_pad_x = 4
        tag_pad_y = 1.5 * mm
        tag_gap_x = 3
        tag_gap_y = 4
        line_y = sy

        for skill in data["skills"]:
            c.setFont("Helvetica", 7.5)
            tw = c.stringWidth(skill, "Helvetica", 7.5)
            tag_w = tw + tag_pad_x * 2

            # Wrap to next line if needed
            if sx + tag_w > SIDE_COL_X + SIDE_COL_W:
                sx = SIDE_COL_X
                line_y -= tag_h + tag_gap_y

            # Tag background
            c.setFillColor(SKILL_TAG)
            c.roundRect(sx, line_y - tag_h, tag_w, tag_h, 2, fill=1, stroke=0)

            # Tag text
            c.setFillColor(SKILL_TEXT)
            c.setFont("Helvetica", 7.5)
            c.drawString(sx + tag_pad_x, line_y - tag_h + tag_pad_y, skill)

            sx += tag_w + tag_gap_x

        sy = line_y - tag_h - 10

    # Certifications
    if data.get("certifications"):
        sy = draw_section_header("Certifications", SIDE_COL_X, SIDE_COL_W, sy)
        for cert in data["certifications"]:
            h = _draw_paragraph(c, f"• {cert}", SIDE_COL_X, sy,
                                 SIDE_COL_W, style_bullet)
            sy -= h + 3

    c.save()
    buffer.seek(0)
    return buffer.read()
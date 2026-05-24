from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import io


# ── Color Palette ──────────────────────────────────────────────────────────────
SIDEBAR_BG  = colors.HexColor("#1a1a2e")
ACCENT      = colors.HexColor("#e94560")
WHITE       = colors.white
OFF_WHITE   = colors.HexColor("#ecf0f1")
LIGHT_TEXT  = colors.HexColor("#aaaaaa")
DARK_TEXT   = colors.HexColor("#111111")
BODY_GRAY   = colors.HexColor("#444444")
DIVIDER     = colors.HexColor("#333355")
SKILL_BG    = colors.HexColor("#2d2d4e")

PAGE_W, PAGE_H = A4
SIDEBAR_W   = 65 * mm
MAIN_X      = SIDEBAR_W + 10 * mm
MAIN_W      = PAGE_W - MAIN_X - 12 * mm
MT          = 0
SIDEBAR_PAD = 10 * mm


def _draw_paragraph(c, text, x, y, width, style):
    p = Paragraph(text, style)
    w, h = p.wrap(width, 999)
    p.drawOn(c, x, y - h)
    return h


def generate_modern_resume(data: dict) -> bytes:
    """
    Generate a Modern two-column resume PDF with dark sidebar.

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

    # ── Draw full-height sidebar background ───────────────────────────────────
    def draw_sidebar_bg():
        c.setFillColor(SIDEBAR_BG)
        c.rect(0, 0, SIDEBAR_W, PAGE_H, fill=1, stroke=0)

    draw_sidebar_bg()

    # ── Paragraph Styles ──────────────────────────────────────────────────────
    style_sidebar_name = ParagraphStyle(
        "sb_name", fontName="Helvetica-Bold",
        fontSize=14, textColor=WHITE,
        leading=18, alignment=TA_CENTER
    )
    style_sidebar_title = ParagraphStyle(
        "sb_title", fontName="Helvetica",
        fontSize=8.5, textColor=ACCENT,
        leading=11, alignment=TA_CENTER
    )
    style_sidebar_section = ParagraphStyle(
        "sb_section", fontName="Helvetica-Bold",
        fontSize=7.5, textColor=ACCENT,
        leading=10, spaceAfter=2
    )
    style_sidebar_text = ParagraphStyle(
        "sb_text", fontName="Helvetica",
        fontSize=7.5, textColor=LIGHT_TEXT,
        leading=11
    )
    style_main_section = ParagraphStyle(
        "main_section", fontName="Helvetica-Bold",
        fontSize=8, textColor=DARK_TEXT,
        leading=10
    )
    style_main_item = ParagraphStyle(
        "main_item", fontName="Helvetica-Bold",
        fontSize=9, textColor=DARK_TEXT,
        leading=12
    )
    style_main_sub = ParagraphStyle(
        "main_sub", fontName="Helvetica",
        fontSize=8, textColor=BODY_GRAY,
        leading=11
    )
    style_main_bullet = ParagraphStyle(
        "main_bullet", fontName="Helvetica",
        fontSize=8, textColor=BODY_GRAY,
        leading=11, leftIndent=8
    )
    style_summary = ParagraphStyle(
        "summary", fontName="Helvetica",
        fontSize=8.5, textColor=BODY_GRAY,
        leading=13
    )

    # ── SIDEBAR content ───────────────────────────────────────────────────────
    sy = PAGE_H - 14 * mm   # sidebar y cursor

    def sb_section_header(title):
        nonlocal sy
        sy -= 6
        # Accent line
        c.setStrokeColor(ACCENT)
        c.setLineWidth(0.8)
        c.line(SIDEBAR_PAD, sy, SIDEBAR_W - SIDEBAR_PAD, sy)
        sy -= 4
        h = _draw_paragraph(c, title.upper(), SIDEBAR_PAD, sy,
                             SIDEBAR_W - SIDEBAR_PAD * 2, style_sidebar_section)
        sy -= h + 3

    # Avatar circle
    avatar_cx = SIDEBAR_W / 2
    avatar_cy = PAGE_H - 22 * mm
    c.setFillColor(ACCENT)
    c.circle(avatar_cx, avatar_cy, 16 * mm, fill=1, stroke=0)

    # Initials inside circle
    name = data.get("name", "")
    initials = "".join([p[0].upper() for p in name.split()[:2]])
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(WHITE)
    c.drawCentredString(avatar_cx, avatar_cy - 5, initials)

    sy = avatar_cy - 20 * mm

    # Name
    h = _draw_paragraph(c, name, SIDEBAR_PAD, sy,
                         SIDEBAR_W - SIDEBAR_PAD * 2, style_sidebar_name)
    sy -= h + 2

    # Job title
    if data.get("job_title"):
        h = _draw_paragraph(c, data["job_title"], SIDEBAR_PAD, sy,
                             SIDEBAR_W - SIDEBAR_PAD * 2, style_sidebar_title)
        sy -= h + 6

    # Contact
    sb_section_header("Contact")
    for field, label in [("email", "Email"), ("phone", "Phone"),
                          ("location", "Location"), ("linkedin", "LinkedIn"),
                          ("github", "GitHub")]:
        val = data.get(field, "").strip()
        if val:
            h = _draw_paragraph(c, f"<b>{label}:</b> {val}", SIDEBAR_PAD, sy,
                                 SIDEBAR_W - SIDEBAR_PAD * 2, style_sidebar_text)
            sy -= h + 3

    # Skills with progress bars
    if data.get("skills"):
        sb_section_header("Skills")
        skills = data["skills"]
        bar_w = SIDEBAR_W - SIDEBAR_PAD * 2
        for i, skill in enumerate(skills[:10]):  # max 10 in sidebar
            # Skill name
            c.setFont("Helvetica", 7.5)
            c.setFillColor(OFF_WHITE)
            c.drawString(SIDEBAR_PAD, sy - 4, skill)
            sy -= 9

            # Bar background
            c.setFillColor(SKILL_BG)
            c.roundRect(SIDEBAR_PAD, sy - 4, bar_w, 4, 2, fill=1, stroke=0)

            # Bar fill — evenly distributed between 65–95%
            fill_pct = 0.95 - (i * 0.04) if i < 8 else 0.65
            c.setFillColor(ACCENT)
            c.roundRect(SIDEBAR_PAD, sy - 4, bar_w * fill_pct, 4, 2, fill=1, stroke=0)
            sy -= 9

    # Certifications in sidebar
    if data.get("certifications"):
        sb_section_header("Certifications")
        for cert in data["certifications"]:
            h = _draw_paragraph(c, f"• {cert}", SIDEBAR_PAD, sy,
                                 SIDEBAR_W - SIDEBAR_PAD * 2, style_sidebar_text)
            sy -= h + 3

    # ── MAIN content ──────────────────────────────────────────────────────────
    my = PAGE_H - 14 * mm   # main y cursor

    def draw_main_section_header(title):
        nonlocal my
        my -= 4
        h = _draw_paragraph(c, title.upper(), MAIN_X, my, MAIN_W, style_main_section)
        my -= h + 2
        # Accent underline
        c.setStrokeColor(ACCENT)
        c.setLineWidth(1)
        c.line(MAIN_X, my, MAIN_X + MAIN_W, my)
        my -= 5

    def check_main_space(needed=25):
        nonlocal my
        if my < needed + 15 * mm:
            c.showPage()
            draw_sidebar_bg()
            my = PAGE_H - 14 * mm

    # Summary
    if data.get("summary", "").strip():
        draw_main_section_header("Profile")
        h = _draw_paragraph(c, data["summary"], MAIN_X, my, MAIN_W, style_summary)
        my -= h + 10

    # Experience
    if data.get("experience"):
        draw_main_section_header("Experience")
        for exp in data["experience"]:
            check_main_space(40)
            role     = exp.get("role", "")
            company  = exp.get("company", "")
            duration = exp.get("duration", "")

            h = _draw_paragraph(c, f"<b>{role}</b>", MAIN_X, my,
                                 MAIN_W * 0.72, style_main_item)
            c.setFont("Helvetica", 7.5)
            c.setFillColor(BODY_GRAY)
            c.drawRightString(MAIN_X + MAIN_W, my - h + 3, duration)
            my -= h + 1

            if company:
                h = _draw_paragraph(c, company, MAIN_X, my, MAIN_W, style_main_sub)
                my -= h + 2

            for bullet in exp.get("bullets", []):
                check_main_space(14)
                h = _draw_paragraph(c, f"• {bullet}", MAIN_X, my,
                                    MAIN_W, style_main_bullet)
                my -= h + 1
            my -= 6

    # Education
    if data.get("education"):
        draw_main_section_header("Education")
        for edu in data["education"]:
            check_main_space(28)
            degree = edu.get("degree", "")
            inst   = edu.get("institution", "")
            year   = edu.get("year", "")

            h = _draw_paragraph(c, f"<b>{degree}</b>", MAIN_X, my,
                                 MAIN_W * 0.75, style_main_item)
            c.setFont("Helvetica", 7.5)
            c.setFillColor(BODY_GRAY)
            c.drawRightString(MAIN_X + MAIN_W, my - h + 3, year)
            my -= h + 1

            if inst:
                h = _draw_paragraph(c, inst, MAIN_X, my, MAIN_W, style_main_sub)
                my -= h + 7

    # Projects
    if data.get("projects"):
        draw_main_section_header("Projects")
        for proj in data["projects"]:
            check_main_space(35)
            name = proj.get("name", "")
            tech = proj.get("tech", "")
            desc = proj.get("description", "")

            h = _draw_paragraph(c, f"<b>{name}</b>", MAIN_X, my,
                                 MAIN_W, style_main_item)
            my -= h + 1

            if tech:
                h = _draw_paragraph(c, f"Stack: {tech}", MAIN_X, my,
                                    MAIN_W, style_main_sub)
                my -= h + 2

            if desc:
                h = _draw_paragraph(c, f"• {desc}", MAIN_X, my,
                                    MAIN_W, style_main_bullet)
                my -= h + 1
            my -= 6

    c.save()
    buffer.seek(0)
    return buffer.read()
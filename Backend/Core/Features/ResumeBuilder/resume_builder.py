"""
Features/resume_generator.py
ATS-Friendly Resume Generator Backend
--------------------------------------
Entry point: generate_resume(data: dict) -> bytes

Expected `data` dict schema (all keys optional except name/email):
{
    # ── Personal Info ──────────────────────────────────────────────────────
    "name":          str,   # Full name
    "email":         str,
    "phone":         str,
    "location":      str,   # City, State / Remote
    "linkedin":      str,   # URL or username
    "github":        str,   # URL or username
    "portfolio":     str,   # URL (optional)

    # ── Professional Summary ───────────────────────────────────────────────
    "summary":       str,   # 2-4 sentence professional summary

    # ── Skills ────────────────────────────────────────────────────────────
    "skills": {
        "Languages":        ["Python", "SQL", ...],
        "Frameworks":       ["FastAPI", "Streamlit", ...],
        "Tools & Platforms":["Git", "Docker", ...],
        "Databases":        ["PostgreSQL", "MongoDB", ...],
        # ... any category name → list of strings
    },

    # ── Work Experience ────────────────────────────────────────────────────
    "experience": [
        {
            "title":       str,
            "company":     str,
            "location":    str,
            "start_date":  str,   # e.g. "Jan 2023"
            "end_date":    str,   # e.g. "Present"
            "bullets":     [str], # Action-verb-led achievement bullets
        },
        ...
    ],

    # ── Education ─────────────────────────────────────────────────────────
    "education": [
        {
            "degree":      str,   # e.g. "Bachelor of Computer Applications"
            "institution": str,
            "location":    str,
            "start_date":  str,
            "end_date":    str,
            "gpa":         str,   # optional
            "relevant_courses": [str],  # optional
        },
        ...
    ],

    # ── Projects ──────────────────────────────────────────────────────────
    "projects": [
        {
            "name":        str,
            "tech_stack":  str,   # comma-separated, e.g. "Python, Streamlit, Gemini API"
            "link":        str,   # GitHub / live URL (optional)
            "bullets":     [str],
        },
        ...
    ],

    # ── Certifications ────────────────────────────────────────────────────
    "certifications": [
        {
            "name":        str,
            "issuer":      str,
            "date":        str,   # e.g. "Mar 2024"
            "credential":  str,   # optional ID / URL
        },
        ...
    ],

    # ── Achievements / Awards ──────────────────────────────────────────────
    "achievements": [str],   # single-line strings

    # ── Languages (spoken) ────────────────────────────────────────────────
    "languages": [str],      # e.g. ["English (Fluent)", "Bengali (Native)"]
}
"""

from __future__ import annotations

import io
from typing import Any

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
    Table,
    TableStyle,
)
from reportlab.lib import colors

# ─────────────────────────────────────────────────────────────────────────────
# DESIGN TOKENS  (clean, single-column, ATS-safe — no tables for layout,
#                 no images, no fancy fonts, all text selectable)
# ─────────────────────────────────────────────────────────────────────────────

PAGE_W, PAGE_H = letter
MARGIN_H = 0.65 * inch   # left / right
MARGIN_V = 0.55 * inch   # top / bottom

FONT_MAIN   = "Helvetica"
FONT_BOLD   = "Helvetica-Bold"
FONT_ITALIC = "Helvetica-Oblique"

COLOR_BLACK  = colors.HexColor("#0D0D0D")
COLOR_ACCENT = colors.HexColor("#1A1A1A")   # dark rule lines — keeps it neutral
COLOR_RULE   = colors.HexColor("#555555")
COLOR_MUTED  = colors.HexColor("#444444")

SIZE_NAME    = 18
SIZE_CONTACT = 8.5
SIZE_SECTION = 10.5
SIZE_BODY    = 9.5
SIZE_SMALL   = 8.5


def _build_styles() -> dict[str, ParagraphStyle]:
    """Return a dict of named ParagraphStyle objects."""
    base = dict(
        fontName=FONT_MAIN,
        fontSize=SIZE_BODY,
        leading=13,
        textColor=COLOR_BLACK,
        spaceAfter=0,
        spaceBefore=0,
    )

    def s(name, **kw):
        merged = {**base, **kw}
        return ParagraphStyle(name, **merged)

    return {
        "name": s(
            "name",
            fontName=FONT_BOLD,
            fontSize=SIZE_NAME,
            leading=22,
            alignment=TA_CENTER,
            textColor=COLOR_BLACK,
        ),
        "contact": s(
            "contact",
            fontSize=SIZE_CONTACT,
            leading=12,
            alignment=TA_CENTER,
            textColor=COLOR_MUTED,
        ),
        "section_header": s(
            "section_header",
            fontName=FONT_BOLD,
            fontSize=SIZE_SECTION,
            leading=14,
            spaceBefore=6,
            textColor=COLOR_ACCENT,
            # ALL-CAPS enforced in code so ATS sees the raw text
        ),
        "job_title": s(
            "job_title",
            fontName=FONT_BOLD,
            fontSize=SIZE_BODY,
            leading=13,
        ),
        "job_meta": s(
            "job_meta",
            fontName=FONT_ITALIC,
            fontSize=SIZE_SMALL,
            leading=11,
            textColor=COLOR_MUTED,
        ),
        "bullet": s(
            "bullet",
            fontSize=SIZE_BODY,
            leading=13,
            leftIndent=12,
            firstLineIndent=-8,
            # Bullet rendered as "• " prefix in text — plain unicode, ATS-readable
        ),
        "body": s("body", fontSize=SIZE_BODY, leading=13),
        "skills_label": s(
            "skills_label",
            fontName=FONT_BOLD,
            fontSize=SIZE_BODY,
            leading=13,
        ),
        "small": s("small", fontSize=SIZE_SMALL, leading=11, textColor=COLOR_MUTED),
    }


# ─────────────────────────────────────────────────────────────────────────────
# HELPER FLOWABLE BUILDERS
# ─────────────────────────────────────────────────────────────────────────────

def _rule(styles: dict) -> list:
    """Thin horizontal rule used under section headers."""
    return [
        HRFlowable(
            width="100%",
            thickness=0.6,
            color=COLOR_RULE,
            spaceAfter=3,
            spaceBefore=1,
        )
    ]


def _section_header(title: str, styles: dict) -> list:
    return [
        Spacer(1, 6),
        Paragraph(title.upper(), styles["section_header"]),
        *_rule(styles),
    ]


def _inline_row(left: str, right: str, styles: dict) -> list:
    """Two-column line: left-aligned title/company | right-aligned dates."""
    tbl = Table(
        [[Paragraph(left, styles["job_title"]), Paragraph(right, styles["job_meta"])]],
        colWidths=[
            PAGE_W - 2 * MARGIN_H - 1.6 * inch,
            1.6 * inch,
        ],
        hAlign="LEFT",
    )
    tbl.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ])
    )
    return [tbl]


def _sub_row(left: str, right: str, styles: dict) -> list:
    """Smaller two-column row for company/institution + location."""
    tbl = Table(
        [[Paragraph(left, styles["job_meta"]), Paragraph(right, styles["job_meta"])]],
        colWidths=[
            PAGE_W - 2 * MARGIN_H - 1.6 * inch,
            1.6 * inch,
        ],
        hAlign="LEFT",
    )
    tbl.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ])
    )
    return [tbl]


def _bullets(items: list[str], styles: dict) -> list:
    out = []
    for item in items:
        txt = item.strip()
        if txt:
            out.append(Paragraph(f"\u2022  {txt}", styles["bullet"]))
            out.append(Spacer(1, 2))
    return out


def _clean(v: Any, fallback: str = "") -> str:
    return str(v).strip() if v else fallback


# ─────────────────────────────────────────────────────────────────────────────
# SECTION RENDERERS
# ─────────────────────────────────────────────────────────────────────────────

def _render_header(data: dict, styles: dict) -> list:
    story = []

    # Full name — largest element on page
    story.append(Paragraph(_clean(data.get("name"), "Your Name"), styles["name"]))
    story.append(Spacer(1, 4))

    # Contact line — pipe-separated, single line for ATS parseability
    parts = []
    if data.get("phone"):
        parts.append(_clean(data["phone"]))
    if data.get("email"):
        parts.append(_clean(data["email"]))
    if data.get("location"):
        parts.append(_clean(data["location"]))
    if data.get("linkedin"):
        parts.append(_clean(data["linkedin"]))
    if data.get("github"):
        parts.append(_clean(data["github"]))
    if data.get("portfolio"):
        parts.append(_clean(data["portfolio"]))

    if parts:
        story.append(Paragraph("  |  ".join(parts), styles["contact"]))

    story.append(Spacer(1, 4))
    return story


def _render_summary(data: dict, styles: dict) -> list:
    summary = _clean(data.get("summary"))
    if not summary:
        return []
    story = [*_section_header("Professional Summary", styles)]
    story.append(Paragraph(summary, styles["body"]))
    story.append(Spacer(1, 4))
    return story


def _render_skills(data: dict, styles: dict) -> list:
    skills: dict = data.get("skills", {})
    if not skills:
        return []

    story = [*_section_header("Technical Skills", styles)]

    for category, items in skills.items():
        if not items:
            continue
        # "Languages: Python, SQL, R" — one line, easy for ATS keyword scanning
        line = f"<b>{_clean(category)}:</b>  {', '.join([_clean(i) for i in items])}"
        story.append(Paragraph(line, styles["body"]))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 3))
    return story


def _render_experience(data: dict, styles: dict) -> list:
    jobs: list = data.get("experience", [])
    if not jobs:
        return []

    story = [*_section_header("Professional Experience", styles)]

    for job in jobs:
        title    = _clean(job.get("title"))
        company  = _clean(job.get("company"))
        loc      = _clean(job.get("location"))
        start    = _clean(job.get("start_date"))
        end      = _clean(job.get("end_date", "Present"))
        date_str = f"{start} – {end}" if start else end

        story += _inline_row(title, date_str, styles)
        story += _sub_row(company, loc, styles)
        story.append(Spacer(1, 3))
        story += _bullets(job.get("bullets", []), styles)
        story.append(Spacer(1, 6))

    return story


def _render_education(data: dict, styles: dict) -> list:
    edu_list: list = data.get("education", [])
    if not edu_list:
        return []

    story = [*_section_header("Education", styles)]

    for edu in edu_list:
        degree      = _clean(edu.get("degree"))
        institution = _clean(edu.get("institution"))
        loc         = _clean(edu.get("location"))
        start       = _clean(edu.get("start_date"))
        end         = _clean(edu.get("end_date"))
        date_str    = f"{start} – {end}" if start else end
        gpa         = _clean(edu.get("gpa"))
        courses     = edu.get("relevant_courses", [])

        story += _inline_row(degree, date_str, styles)

        sub_left = institution
        if gpa:
            sub_left += f"  |  GPA: {gpa}"
        story += _sub_row(sub_left, loc, styles)

        if courses:
            course_line = "Relevant Coursework: " + ", ".join(courses)
            story.append(Spacer(1, 2))
            story.append(Paragraph(course_line, styles["small"]))

        story.append(Spacer(1, 6))

    return story


def _render_projects(data: dict, styles: dict) -> list:
    projects: list = data.get("projects", [])
    if not projects:
        return []

    story = [*_section_header("Projects", styles)]

    for proj in projects:
        name  = _clean(proj.get("name"))
        stack = _clean(proj.get("tech_stack"))
        link  = _clean(proj.get("link"))

        # Title line: ProjectName  |  Tech Stack
        title_str = name
        if stack:
            title_str += f"  |  {stack}"

        right_str = link if link else ""
        story += _inline_row(title_str, right_str, styles)
        story.append(Spacer(1, 3))
        story += _bullets(proj.get("bullets", []), styles)
        story.append(Spacer(1, 6))

    return story


def _render_certifications(data: dict, styles: dict) -> list:
    certs: list = data.get("certifications", [])
    if not certs:
        return []

    story = [*_section_header("Certifications", styles)]

    for cert in certs:
        name       = _clean(cert.get("name"))
        issuer     = _clean(cert.get("issuer"))
        date       = _clean(cert.get("date"))
        credential = _clean(cert.get("credential"))

        left  = f"{name}  —  {issuer}" if issuer else name
        right = date
        story += _inline_row(left, right, styles)

        if credential:
            story.append(Spacer(1, 1))
            story.append(Paragraph(f"Credential: {credential}", styles["small"]))

        story.append(Spacer(1, 5))

    return story


def _render_achievements(data: dict, styles: dict) -> list:
    items: list = data.get("achievements", [])
    if not items:
        return []

    story = [*_section_header("Achievements & Awards", styles)]
    story += _bullets(items, styles)
    story.append(Spacer(1, 4))
    return story


def _render_languages(data: dict, styles: dict) -> list:
    langs: list = data.get("languages", [])
    if not langs:
        return []

    story = [*_section_header("Languages", styles)]
    story.append(Paragraph(", ".join(langs), styles["body"]))
    story.append(Spacer(1, 4))
    return story


# ─────────────────────────────────────────────────────────────────────────────
# MAIN PUBLIC FUNCTION
# ─────────────────────────────────────────────────────────────────────────────

def generate_resume(data: dict) -> bytes:
    """
    Generate an ATS-friendly PDF resume from `data` dict.

    Returns raw PDF bytes — write to file or serve directly from Streamlit:

        pdf_bytes = generate_resume(data)
        st.download_button("Download Resume", pdf_bytes,
                           file_name="resume.pdf", mime="application/pdf")
    """
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=MARGIN_H,
        rightMargin=MARGIN_H,
        topMargin=MARGIN_V,
        bottomMargin=MARGIN_V,
        title=f"{_clean(data.get('name'), 'Resume')} – Resume",
        author=_clean(data.get("name"), ""),
        subject="Professional Resume",
        creator="ResumeBuilder",
        # PDF metadata is parsed by some ATS systems
    )

    styles = _build_styles()

    story: list = []

    # ── Ordered section rendering ─────────────────────────────────────────
    story += _render_header(data, styles)
    story += _render_summary(data, styles)
    story += _render_skills(data, styles)
    story += _render_experience(data, styles)
    story += _render_education(data, styles)
    story += _render_projects(data, styles)
    story += _render_certifications(data, styles)
    story += _render_languages(data, styles)

    doc.build(story)
    return buffer.getvalue()


# ─────────────────────────────────────────────────────────────────────────────
# QUICK LOCAL TEST  (python resume_generator.py)
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sample: dict = {
        "name": "Arijit Das",
        "email": "arijit@example.com",
        "phone": "+91-XXXXX-XXXXX",
        "location": "Kolkata, West Bengal",
        "linkedin": "linkedin.com/in/arijitdas",
        "github": "github.com/arijitdas",
        "summary": (
            "Data-driven BCA student and startup developer specializing in "
            "AI systems, Python backend engineering, and analytics pipelines. "
            "Experienced in building production-quality Streamlit applications, "
            "LLM integrations, and data visualization dashboards."
        ),
        "skills": {
            "Languages":           ["Python", "SQL", "R", "C++", "JavaScript"],
            "Frameworks & Tools":  ["Streamlit", "FastAPI", "Flask", "ReportLab", "LangChain"],
            "AI / ML":             ["Scikit-Learn", "TensorFlow", "PyTorch", "Cohere API", "Gemini API"],
            "Databases":           ["PostgreSQL", "MongoDB", "BigQuery"],
            "DevOps & Cloud":      ["Git", "Docker", "GitHub Actions", "GCP"],
        },
        "experience": [
            {
                "title":      "Tech Developer Intern",
                "company":    "ExampleStartup Pvt. Ltd.",
                "location":   "Remote",
                "start_date": "Jan 2025",
                "end_date":   "Present",
                "bullets": [
                    "Designed and deployed a Streamlit-based AI prompt engineering tool (PromptLab) used by 200+ beta testers, reducing prompt iteration time by 40%.",
                    "Built a RAG pipeline using Cohere API with conversation memory, increasing response relevance score from 71% to 89%.",
                    "Established Git branching conventions (Conventional Commits) and CI/CD workflows via GitHub Actions, cutting merge conflicts by 60%.",
                ],
            }
        ],
        "education": [
            {
                "degree":      "Bachelor of Computer Applications (BCA) – Data Analytics",
                "institution": "Example University",
                "location":    "Kolkata, WB",
                "start_date":  "2022",
                "end_date":    "2025",
                "gpa":         "8.7 / 10",
                "relevant_courses": [
                    "Machine Learning", "Database Management", "Data Structures",
                    "Statistical Modeling", "Cloud Computing",
                ],
            }
        ],
        "projects": [
            {
                "name":       "Ahanix AI – Jarvis-Style Voice Assistant",
                "tech_stack": "Python, Streamlit, Groq API, gTTS",
                "link":       "github.com/arijitdas/ahanix-ai",
                "bullets": [
                    "Engineered a futuristic glassmorphism UI with animated SVG robot avatar and real-time voice state management.",
                    "Integrated Groq LLaMA-3 backend for sub-200ms response latency on a free-tier API quota.",
                ],
            },
            {
                "name":       "PromptLab – Prompt Engineering Studio",
                "tech_stack": "Python, Streamlit, Gemini API",
                "link":       "github.com/arijitdas/promptlab",
                "bullets": [
                    "Built a structured prompt generation tool with tone/length controls and section parsing, supporting 12 prompt templates.",
                    "Implemented a premium dark glassmorphism design system reused across 3 internal projects.",
                ],
            },
        ],
        "certifications": [
            {
                "name":   "Google Data Analytics Professional Certificate",
                "issuer": "Google / Coursera",
                "date":   "Nov 2024",
            },
            {
                "name":   "Python for Data Science and AI",
                "issuer": "IBM / Coursera",
                "date":   "Aug 2024",
            },
        ]
}

    pdf_bytes = generate_resume(sample)

    out_path = "sample_resume.pdf"
    with open(out_path, "wb") as f:
        f.write(pdf_bytes)
    print(f"Resume written to {out_path}  ({len(pdf_bytes):,} bytes)")
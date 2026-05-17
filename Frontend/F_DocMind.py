import streamlit as st


# =========================================================
# CSS
# =========================================================

def inject_css():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp{
        background:
            radial-gradient(circle at top left, rgba(91,66,255,0.16), transparent 28%),
            radial-gradient(circle at bottom right, rgba(0,212,255,0.12), transparent 30%),
            linear-gradient(135deg,#040816 0%,#090d1f 35%,#0d1226 70%,#050816 100%);
        color:white;
        overflow-x:hidden;
    }

    [data-testid="stHeader"]{
        background:transparent;
    }

    .block-container{
        max-width:1250px;
        padding-top:1rem;
        padding-bottom:2rem;
    }

    /* =========================================================
       MAIN CONTAINER
    ========================================================= */

    .docmind-wrapper{
        position:relative;
        overflow:hidden;

        background: rgba(12,18,38,0.72);

        border:1px solid rgba(255,255,255,0.08);

        backdrop-filter: blur(24px);

        border-radius:34px;

        padding:72px;

        margin-top:20px;

        box-shadow:
            0 10px 60px rgba(0,0,0,0.45),
            inset 0 1px 0 rgba(255,255,255,0.05);

        animation: fadeUp 1s ease;
    }

    @keyframes fadeUp{
        from{
            opacity:0;
            transform:translateY(40px);
        }
        to{
            opacity:1;
            transform:translateY(0px);
        }
    }

    /* =========================================================
       BACKGROUND ORBS
    ========================================================= */

    .orb{
        position:absolute;
        border-radius:50%;
        filter:blur(80px);
        opacity:0.22;
        pointer-events:none;
        animation: floatOrb 10s ease-in-out infinite;
    }

    .orb1{
        width:260px;
        height:260px;
        background:#7c5cff;
        top:-90px;
        right:-90px;
    }

    .orb2{
        width:240px;
        height:240px;
        background:#00d4ff;
        bottom:-80px;
        left:-70px;
        animation-delay:-5s;
    }

    @keyframes floatOrb{
        0%,100%{
            transform:translateY(0px);
        }
        50%{
            transform:translateY(-28px);
        }
    }

    /* =========================================================
       BADGE
    ========================================================= */

    .hero-badge{
        display:inline-flex;
        align-items:center;
        gap:10px;

        padding:10px 18px;

        border-radius:999px;

        background: rgba(124,92,255,0.12);

        border:1px solid rgba(124,92,255,0.28);

        color:#cfc4ff;

        font-size:13px;
        font-weight:600;

        margin-bottom:30px;

        animation:pulseGlow 4s infinite ease-in-out;
    }

    @keyframes pulseGlow{
        0%,100%{
            box-shadow:0 0 0px rgba(124,92,255,0);
        }
        50%{
            box-shadow:0 0 28px rgba(124,92,255,0.4);
        }
    }

    /* =========================================================
       TITLE
    ========================================================= */

    .logo{
        display:flex;
        align-items:center;
        gap:16px;
    }

    .logo-icon{

        width:62px;
        height:62px;

        border-radius:18px;

        display:flex;
        align-items:center;
        justify-content:center;

        background:
            linear-gradient(
                135deg,
                rgba(124,92,255,0.22),
                rgba(0,212,255,0.16)
            );

        border:1px solid rgba(255,255,255,0.08);

        font-size:30px;

        box-shadow:
            0 0 40px rgba(124,92,255,0.35);

        animation:iconFloat 4s ease-in-out infinite;
    }

    @keyframes iconFloat{
        0%,100%{
            transform:translateY(0px);
        }
        50%{
            transform:translateY(-6px);
        }
    }

    .logo-text{
        display:flex;
        flex-direction:column;
    }

    .logo-main{

        font-size:5rem;
        font-weight:900;
        line-height:1;

        letter-spacing:-3px;

        background: linear-gradient(
            90deg,
            #ffffff 0%,
            #d8cbff 20%,
            #7C5CFF 45%,
            #00D4FF 70%,
            #ffffff 100%
        );

        background-size:300% auto;

        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;

        animation:gradientFlow 8s linear infinite;
    }

    @keyframes gradientFlow{
        0%{
            background-position:0% center;
        }
        100%{
            background-position:300% center;
        }
    }

    .logo-sub{
        margin-top:8px;

        font-size:14px;
        color:#8b95b5;

        letter-spacing:0.6px;
    }

    /* =========================================================
       DESCRIPTION
    ========================================================= */

    .hero-desc{

        margin-top:34px;

        max-width:860px;

        font-size:18px;

        line-height:1.9;

        color:#b8c2de;
    }

    .hero-desc strong{
        color:white;
    }

    /* =========================================================
       FEATURE TAGS
    ========================================================= */

    .feature-tags{
        display:flex;
        flex-wrap:wrap;
        gap:14px;

        margin-top:40px;
    }

    .feature-tag{

        padding:12px 18px;

        border-radius:14px;

        background: rgba(255,255,255,0.04);

        border:1px solid rgba(255,255,255,0.08);

        color:#d9e0f5;

        font-size:14px;
        font-weight:500;

        transition:0.35s ease;

        position:relative;
        overflow:hidden;
    }

    .feature-tag::before{
        content:'';

        position:absolute;
        inset:0;

        background:linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.08),
            transparent
        );

        transform:translateX(-100%);
        transition:0.6s;
    }

    .feature-tag:hover::before{
        transform:translateX(100%);
    }

    .feature-tag:hover{

        transform:translateY(-4px);

        border-color:rgba(124,92,255,0.35);

        box-shadow:
            0 10px 25px rgba(124,92,255,0.16);
    }

    /* =========================================================
       FEATURE CARDS
    ========================================================= */

    .section-title{
        margin-top:70px;
        margin-bottom:26px;

        font-size:30px;
        font-weight:800;

        color:white;
    }

    .feature-grid{

        display:grid;

        grid-template-columns:
            repeat(auto-fit,minmax(330px,1fr));

        gap:24px;
    }

    .feature-card{

        position:relative;

        background: rgba(255,255,255,0.035);

        border:1px solid rgba(255,255,255,0.08);

        border-radius:24px;

        padding:30px;

        overflow:hidden;

        transition:0.35s ease;
    }

    .feature-card::after{

        content:'';

        position:absolute;

        top:0;
        left:0;

        width:100%;
        height:2px;

        background:
            linear-gradient(
                90deg,
                #7C5CFF,
                #00D4FF
            );

        transform:scaleX(0);
        transform-origin:left;

        transition:0.4s ease;
    }

    .feature-card:hover::after{
        transform:scaleX(1);
    }

    .feature-card:hover{

        transform:translateY(-6px);

        border-color:rgba(124,92,255,0.25);

        box-shadow:
            0 16px 35px rgba(0,0,0,0.35),
            0 0 30px rgba(124,92,255,0.12);
    }

    .feature-icon{
        font-size:28px;
        margin-bottom:18px;
    }

    .feature-title{
        font-size:22px;
        font-weight:800;
        color:white;
        margin-bottom:14px;
    }

    .feature-text{
        color:#c7d1ea;
        line-height:1.8;
        font-size:15px;
    }

    /* =========================================================
       GUIDE SECTION
    ========================================================= */

    .guide-grid{
        display:grid;

        grid-template-columns:
            repeat(auto-fit,minmax(280px,1fr));

        gap:20px;

        margin-top:24px;
    }

    .guide-card{

        background: rgba(255,255,255,0.03);

        border:1px solid rgba(255,255,255,0.08);

        border-radius:20px;

        padding:24px;

        transition:0.35s ease;
    }

    .guide-card:hover{

        transform:translateY(-5px);

        border-color:rgba(124,92,255,0.28);

        box-shadow:
            0 14px 30px rgba(0,0,0,0.35);
    }

    .guide-icon{
        font-size:24px;
        margin-bottom:14px;
    }

    .guide-text{
        color:#c6d0e8;
        line-height:1.8;
        font-size:15px;
    }

    /* =========================================================
       BUTTON
    ========================================================= */

    .stButton > button{

        background:
            linear-gradient(
                135deg,
                #7C5CFF 0%,
                #00D4FF 100%
            );

        color:white;

        border:none;

        border-radius:16px;

        padding:15px 26px;

        font-size:15px;
        font-weight:700;

        transition:0.35s ease;

        box-shadow:
            0 10px 30px rgba(124,92,255,0.35);

        position:relative;
        overflow:hidden;
    }

    .stButton > button::before{

        content:'';

        position:absolute;

        top:0;
        left:-100%;

        width:100%;
        height:100%;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(255,255,255,0.25),
                transparent
            );

        transition:0.7s;
    }

    .stButton > button:hover::before{
        left:100%;
    }

    .stButton > button:hover{

        transform:translateY(-3px);

        box-shadow:
            0 18px 40px rgba(124,92,255,0.45),
            0 0 30px rgba(0,212,255,0.25);
    }

    /* =========================================================
       RESPONSIVE
    ========================================================= */

    @media(max-width:768px){

        .docmind-wrapper{
            padding:38px 24px;
        }

        .logo-main{
            font-size:3rem;
        }

        .hero-desc{
            font-size:16px;
        }
    }

    </style>
    """, unsafe_allow_html=True)


# =========================================================
# HTML
# =========================================================

def landing_section1():

    st.markdown("""
    <div class="docmind-wrapper">
        <div class="orb orb1"></div>
        <div class="orb orb2"></div>
        <div class="hero-badge">
            📚 AI Learning & Knowledge Workspace
        </div>
        <div class="logo">
            <div class="logo-icon">
                🧠
            </div>
            <div class="logo-text">
                <div class="logo-main">
                    Jarvis Scholar
                </div>
                <div class="logo-sub">
                    AI PDF CHATBOT + SMART NOTE SUMMARIZER
                </div>
            </div>
        </div>
        <div class="hero-desc">
            <strong>Jarvis Scholar</strong>
            is an AI-powered learning workspace designed for students and researchers.
            Upload PDFs and chat with your documents using advanced
            <strong>RAG (Retrieval-Augmented Generation)</strong>
            technology.
            Ask questions directly from books, notes, research papers, assignments,
            or study materials and receive intelligent contextual answers instantly.
            Also includes a smart AI-powered note-taking system where students can
            write raw notes and let AI automatically generate
            structured summaries, key points, clean explanations,
            and downloadable study PDFs.
        </div>
        <div class="feature-tags">
            <div class="feature-tag">
                📄 AI PDF Chatbot
            </div>
            <div class="feature-tag">
                🧠 RAG-Powered Retrieval
            </div>
            <div class="feature-tag">
                ✨ Smart Note Summarization
            </div>
            <div class="feature-tag">
                📘 Auto Key Point Extraction
            </div>
            <div class="feature-tag">
                🔍 Semantic Search
            </div>
            <div class="feature-tag">
                ⚡ Instant Question Answering
            </div>
            <div class="feature-tag">
                📥 Export Notes as PDF
            </div>
            <div class="feature-tag">
                🎓 Student Productivity Tool
            </div>
        </div>
        <!-- =====================================================
             FEATURE SECTION
        ====================================================== -->
        <div class="section-title">
            Core Features
        </div>
        <div class="feature-grid">
            <div class="feature-card">
                <div class="feature-icon">
                    📄
                </div>
                <div class="feature-title">
                    PDF Chatbot
                </div>
                <div class="feature-text">
                    Upload PDFs like study materials, books,
                    research papers, lecture notes, assignments,
                    or documentation.
                    The AI understands the document using RAG
                    and answers questions contextually instead of giving random responses.
                </div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">
                    🧠
                </div>
                <div class="feature-title">
                    AI Note Summarizer
                </div>
                <div class="feature-text">
                    Write notes naturally inside the workspace
                    and let AI summarize them into
                    clean, structured study notes with
                    key points, highlights, explanations,
                    and simplified concepts.
                </div>
            </div>
        </div>
        <!-- =====================================================
             USER GUIDE
        ====================================================== -->
        <div class="section-title">
            User Guide
        </div>
        <div class="guide-grid">
            <div class="guide-card">
                <div class="guide-icon">
                    📚
                </div>
                <div class="guide-text">
                    Upload textbooks, class notes, PDFs,
                    research papers, or assignments
                    and chat with them naturally.
                </div>
            </div>
            <div class="guide-card">
                <div class="guide-icon">
                    🔍
                </div>
                <div class="guide-text">
                    Ask questions like:
                    “Explain this chapter”,
                    “Summarize page 12”,
                    or “What is the definition of this topic?”
                </div>
            </div>
            <div class="guide-card">
                <div class="guide-icon">
                    ⚡
                </div>
                <div class="guide-text">
                    AI retrieves only relevant information
                    from your uploaded documents using
                    advanced semantic search and RAG pipelines.
                </div>
            </div>
            <div class="guide-card">
                <div class="guide-icon">
                    ✍️
                </div>
                <div class="guide-text">
                    Write raw notes during classes,
                    meetings, or study sessions
                    and let AI organize them automatically.
                </div>
            </div>
            <div class="guide-card">
                <div class="guide-icon">
                    🧠
                </div>
                <div class="guide-text">
                    AI extracts important key points,
                    creates concise summaries,
                    and improves readability for faster revision.
                </div>
            </div>
            <div class="guide-card">
                <div class="guide-icon">
                    📘
                </div>
                <div class="guide-text">
                    Generate clean downloadable PDFs
                    from your summarized notes
                    for future study and sharing.
                </div>
            </div>
            <div class="guide-card">
                <div class="guide-icon">
                    🚀
                </div>
                <div class="guide-text">
                    Perfect for exam preparation,
                    assignment solving,
                    quick revisions,
                    and understanding complex topics faster.
                </div>
            </div>
            <div class="guide-card">
                <div class="guide-icon">
                    🎓
                </div>
                <div class="guide-text">
                    Designed especially for students
                    who want an AI-powered
                    second brain for learning.
                </div>
            </div>
        </div>
    </div>

    """, unsafe_allow_html=True)

    ol1,col2,_,_,col3, _ = st.columns(6)

    with col2:
        button = st.button("🚀 Get Started")
    
    return button
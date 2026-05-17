import streamlit as st
import streamlit.components.v1 as components

def render_about_page():    
    
    st.set_page_config(
        page_title="Jarvis AI",
        page_icon="🧠",
        layout="wide"
    )    
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">    <style>    /* =========================================================
       GLOBAL
    ========================================================= */    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        scroll-behavior: smooth;
    }    .stApp {
        background:
            radial-gradient(circle at top left, rgba(124,92,255,0.18), transparent 30%),
            radial-gradient(circle at bottom right, rgba(0,212,255,0.10), transparent 30%),
            linear-gradient(135deg, #050816 0%, #0c1025 40%, #090d1d 100%);
        color: white;
        overflow-x: hidden;
    }    [data-testid="stHeader"] {
        background: transparent;
    }    .block-container {
        max-width: 100% !important;
        padding-top: 0rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
        padding-bottom: 0rem !important;
    }    /* =========================================================
       SIDEBAR
    ========================================================= */    section[data-testid="stSidebar"] {
        background: rgba(10, 14, 30, 0.92);
        border-right: 1px solid rgba(255,255,255,0.06);
        backdrop-filter: blur(20px);
    }    section[data-testid="stSidebar"] * {
        color: white !important;
    }    /* =========================================================
       MAIN WRAPPER
    ========================================================= */    .main-wrapper {
        max-width: 1450px;
        margin: auto;
        position: relative;
        z-index: 1;
    }    /* =========================================================
       NAVBAR
    ========================================================= */    .navbar {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;        padding-top: 24px;
        padding-bottom: 30px;        animation: fadeUp 0.8s ease;
    }    .logo {
        display: flex;
        align-items: center;
        gap: 12px;        font-size: 5.9rem;
        font-weight: 800;
        letter-spacing: -0.5px;
    }    .logo-gradient {
        background: linear-gradient(90deg,#7C5CFF,#00D4FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }    .nav-links {
        display: flex;
        align-items: center;
        gap: 28px;
    }    .nav-links a {
        color: rgba(255,255,255,0.68);
        text-decoration: none;
        font-size: 0.92rem;
        transition: 0.3s ease;
    }    .nav-links a:hover {
        color: white;
    }    .nav-btn {
        padding: 12px 18px;
        border-radius: 14px;
        background: linear-gradient(135deg,#7C5CFF,#00D4FF);
        color: white !important;
        font-weight: 600;
        box-shadow: 0 10px 35px rgba(124,92,255,0.35);
    }    /* =========================================================
       HERO SECTION
    ========================================================= */    .hero-section {
        position: relative;
        padding-top: 90px;
        padding-bottom: 120px;
        overflow: hidden;
    }    .hero-grid {
        display: grid;
        grid-template-columns: 1.1fr 0.9fr;
        gap: 40px;
        align-items: center;
    }    .hero-left {
        position: relative;
        z-index: 2;
        animation: fadeUp 1s ease;
    }    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 10px;        padding: 10px 18px;        border-radius: 999px;        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);        color: rgba(255,255,255,0.84);        font-size: 0.86rem;
        font-weight: 500;        margin-bottom: 30px;        backdrop-filter: blur(12px);
    }    .hero-title {
        font-size: clamp(52px, 6vw, 88px);
        font-weight: 900;
        line-height: 0.98;
        letter-spacing: -4px;        margin-bottom: 28px;
    }    .hero-title span {
        background: linear-gradient(90deg,#FFFFFF,#9ec5ff,#B87CFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }    .hero-description {
        max-width: 720px;        color: rgba(255,255,255,0.68);        font-size: 1.08rem;
        line-height: 1.9;        margin-bottom: 40px;
    }    .hero-buttons {
        display: flex;
        align-items: center;
        gap: 18px;
        flex-wrap: wrap;
    }    .primary-btn {
        text-decoration: none;        padding: 16px 28px;
        border-radius: 18px;        background: linear-gradient(135deg,#7C5CFF,#00D4FF);        color: white;
        font-weight: 700;        transition: 0.35s ease;        box-shadow: 0 10px 45px rgba(124,92,255,0.35);
    }    .primary-btn:hover {
        transform: translateY(-4px);
    }    .secondary-btn {
        text-decoration: none;        padding: 16px 28px;
        border-radius: 18px;        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);        color: white;
        font-weight: 600;        transition: 0.35s ease;
    }    .secondary-btn:hover {
        background: rgba(255,255,255,0.08);
    }    /* =========================================================
       HERO VISUAL
    ========================================================= */    .hero-right {
        position: relative;
        animation: fadeUp 1.2s ease;
    }    .dashboard-preview {
        position: relative;        border-radius: 32px;        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.05),
                rgba(255,255,255,0.02)
            );        border: 1px solid rgba(255,255,255,0.08);        backdrop-filter: blur(18px);        padding: 28px;        overflow: hidden;        box-shadow:
            0 20px 80px rgba(0,0,0,0.45),
            0 0 60px rgba(124,92,255,0.12);
    }    .dashboard-preview::before {
        content: "";        position: absolute;
        inset: 0;        background:
            radial-gradient(circle at top right, rgba(124,92,255,0.18), transparent 35%),
            radial-gradient(circle at bottom left, rgba(0,212,255,0.14), transparent 35%);
    }    .window-top {
        display: flex;
        gap: 8px;
        margin-bottom: 24px;
    }    .window-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }    .window-dot:nth-child(1) {
        background: #ff5f57;
    }    .window-dot:nth-child(2) {
        background: #ffbd2e;
    }    .window-dot:nth-child(3) {
        background: #28ca42;
    }    .dashboard-cards {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 18px;
        position: relative;
        z-index: 2;
    }    .mini-card {
        padding: 22px;
        border-radius: 20px;        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);        transition: 0.35s ease;
    }    .mini-card:hover {
        transform: translateY(-5px);
        border-color: rgba(124,92,255,0.4);
    }    .mini-icon {
        width: 52px;
        height: 52px;        display: flex;
        align-items: center;
        justify-content: center;        border-radius: 14px;        background: linear-gradient(135deg,#7C5CFF,#00D4FF);        font-size: 1.5rem;        margin-bottom: 18px;
    }    .mini-title {
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 10px;
    }    .mini-desc {
        font-size: 0.9rem;
        line-height: 1.7;
        color: rgba(255,255,255,0.65);
    }    /* =========================================================
       SECTION TITLE
    ========================================================= */    .section {
        padding-top: 120px;
        padding-bottom: 20px;
    }    .section-title {
        text-align: center;        font-size: clamp(38px, 4vw, 58px);
        font-weight: 800;        letter-spacing: -2px;        margin-bottom: 20px;
    }    .section-subtitle {
        text-align: center;        max-width: 760px;
        margin: auto;        color: rgba(255,255,255,0.65);        line-height: 1.8;
        font-size: 1.05rem;        margin-bottom: 70px;
    }    /* =========================================================
       FEATURE GRID
    ========================================================= */    .feature-grid {
        display: grid;        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));        gap: 28px;
    }    .feature-card {
        position: relative;        padding: 34px;        border-radius: 28px;        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.05),
                rgba(255,255,255,0.02)
            );        border: 1px solid rgba(255,255,255,0.08);        overflow: hidden;        transition: 0.35s ease;        backdrop-filter: blur(14px);
    }    .feature-card:hover {
        transform: translateY(-8px);        border-color: rgba(124,92,255,0.4);        box-shadow:
            0 20px 70px rgba(124,92,255,0.18);
    }    .feature-card::before {
        content: "";        position: absolute;        width: 200px;
        height: 200px;        background:
            radial-gradient(circle, rgba(124,92,255,0.22), transparent 70%);        top: -60px;
        right: -60px;
    }    .feature-icon {
        width: 70px;
        height: 70px;        display: flex;
        align-items: center;
        justify-content: center;        border-radius: 20px;        background: linear-gradient(135deg,#7C5CFF,#00D4FF);        font-size: 2rem;        margin-bottom: 24px;        box-shadow: 0 15px 40px rgba(124,92,255,0.3);
    }    .feature-title {
        font-size: 1.35rem;
        font-weight: 700;        margin-bottom: 14px;
    }    .feature-description {
        color: rgba(255,255,255,0.66);        line-height: 1.8;
        font-size: 0.97rem;
    }    /* =========================================================
       MODEL STRIP
    ========================================================= */    .models-section {
        margin-top: 120px;        padding: 60px;        border-radius: 36px;        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.04),
                rgba(255,255,255,0.02)
            );        border: 1px solid rgba(255,255,255,0.08);        position: relative;
        overflow: hidden;
    }    .models-section::before {
        content: "";        position: absolute;
        inset: 0;        background:
            radial-gradient(circle at top left, rgba(124,92,255,0.15), transparent 30%),
            radial-gradient(circle at bottom right, rgba(0,212,255,0.12), transparent 30%);
    }    .model-wrapper {
        position: relative;
        z-index: 2;
    }    .model-row {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 18px;        margin-top: 40px;
    }    .model-chip {
        padding: 16px 22px;        border-radius: 999px;        background: rgba(255,255,255,0.05);        border: 1px solid rgba(255,255,255,0.08);        transition: 0.3s ease;        font-weight: 600;
    }    .model-chip:hover {
        transform: scale(1.05);
        background: rgba(124,92,255,0.12);
    }    /* =========================================================
       CTA
    ========================================================= */    .cta-section {
        margin-top: 140px;        padding: 90px 40px;        border-radius: 36px;        text-align: center;        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.05),
                rgba(255,255,255,0.02)
            );        border: 1px solid rgba(255,255,255,0.08);        position: relative;
        overflow: hidden;
    }    .cta-section::before {
        content: "";        position: absolute;        width: 500px;
        height: 500px;        background:
            radial-gradient(circle, rgba(124,92,255,0.18), transparent 70%);        top: -250px;
        left: 50%;        transform: translateX(-50%);
    }    .cta-title {
        position: relative;
        z-index: 2;        font-size: clamp(38px, 4vw, 62px);        font-weight: 800;        line-height: 1.1;        letter-spacing: -2px;        margin-bottom: 24px;
    }    .cta-description {
        position: relative;
        z-index: 2;        max-width: 760px;        margin: auto;        color: rgba(255,255,255,0.7);        line-height: 1.9;        margin-bottom: 40px;
    }    /* =========================================================
       FOOTER
    ========================================================= */    .footer {
        text-align: center;        padding-top: 80px;
        padding-bottom: 40px;        color: rgba(255,255,255,0.4);        font-size: 0.92rem;
    }    /* =========================================================
       ANIMATION
    ========================================================= */    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }        to {
            opacity: 1;
            transform: translateY(0);
        }
    }    /* =========================================================
       RESPONSIVE
    ========================================================= */    @media (max-width: 1100px) {        .hero-grid {
            grid-template-columns: 1fr;
        }        .hero-right {
            margin-top: 20px;
        }
    }    @media (max-width: 768px) {        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }        .nav-links {
            display: none;
        }        .hero-title {
            letter-spacing: -2px;
        }        .dashboard-cards {
            grid-template-columns: 1fr;
        }        .models-section {
            padding: 40px 24px;
        }        .cta-section {
            padding: 70px 24px;
        }
    }    </style>
    """, unsafe_allow_html=True)    
    st.markdown("""    <div class="main-wrapper">        <!-- =====================================================
             NAVBAR
        ====================================================== -->        <div class="navbar">            <div class="logo">
                <span class="logo-gradient">Jarvis</span>
            </div>            <div class="nav-links">
                <a href="#features">Features</a>
                <a href="#models">Models</a>
                <a href="#about">About</a>
            </div>        </div>        <!-- =====================================================
             HERO SECTION
        ====================================================== -->        <div class="hero-section">            <div class="hero-grid">                <div class="hero-left">                    <div class="hero-badge">
                        ✨ Premium Multimodal AI Workspace
                    </div>                    <div class="hero-title">
                        Your Everyday AI <br>
                        <span>Powered Ecosystem</span>
                    </div>                    <div class="hero-description">
                        Jarvis is a next-generation multimodal AI platform designed
                        to simplify everyday workflows using powerful LLMs,
                        intelligent automation, voice interaction, coding assistance,
                        image generation, and document reasoning — all inside one
                        unified AI workspace.
                    </div>                    <div class="hero-buttons">                        
                        <a href="#features" class="secondary-btn">
                            Explore Features
                        </a>                    </div>                </div>
                            </div>
                                              <!-- =====================================================
             FEATURES
        ====================================================== -->        <div class="section" id="features">            <div class="section-title">
                Everything You Need.<br>
                Powered by AI.
            </div>            <div class="section-subtitle">
                Built for developers, creators, researchers, students,
                startups, and productivity-focused users who want all AI
                tools inside one ecosystem.
            </div>            <div class="feature-grid">                <div class="feature-card">
                    <div class="feature-icon">🎙️</div>
                    <div class="feature-title">Jarvis VoiceAssistant</div>
                    <div class="feature-description">
                        Natural voice interaction with real-time STT + TTS,
                        contextual memory, and intelligent workflow automation.
                    </div>
                </div>                <div class="feature-card">
                    <div class="feature-icon">💻</div>
                    <div class="feature-title">Jarvis Code/Debug</div>
                    <div class="feature-description">
                        A modern AI code editor with co-pilot support,
                        debugging assistance, and intelligent coding workflows.
                    </div>
                </div>                <div class="feature-card">
                    <div class="feature-icon">🎨</div>
                    <div class="feature-title">Jarvis ImageLab</div>
                    <div class="feature-description">
                        Create high-quality AI-generated images, posters,
                        concepts, and creative assets instantly.
                    </div>
                </div>                <div class="feature-card">
                    <div class="feature-icon">✨</div>
                    <div class="feature-title">Jarvis PromptLab</div>
                    <div class="feature-description">
                        Generate optimized prompts for coding, writing,
                        automation, AI systems, and productivity workflows.
                    </div>
                </div>                <div class="feature-card">
                    <div class="feature-icon">📄</div>
                    <div class="feature-title">Jarvis ScholarHub</div>
                    <div class="feature-description">
                        RAG-powered PDF chatbot for extracting insights,
                        summaries, contextual answers, and knowledge.
                    </div>
                </div>                <div class="feature-card">
                    <div class="feature-icon">👨‍🎓</div>
                    <div class="feature-title">Jarvis ResumeLab</div>
                    <div class="feature-description">
                        Automate repetitive workflows with LLM orchestration,
                        intelligent pipelines, and contextual AI systems.
                    </div>
                </div>            </div>        </div>        <!-- =====================================================
             MODELS
        ====================================================== -->        <div class="models-section" id="models">            <div class="model-wrapper">                <div class="section-title">
                    Multi-Model Intelligence
                </div>                <div class="section-subtitle">
                    Jarvis integrates powerful AI models intelligently
                    so users always get the best model for every task.
                </div>                <div class="model-row">                    <div class="model-chip">⚡ Cohere</div>
                    <div class="model-chip">🌌 Gemini</div>
                    <div class="model-chip">🦙 Llama</div>
                    <div class="model-chip">🔥 Mistral</div>                </div>            </div>        </div>        <!-- =====================================================
             CTA
        ====================================================== -->        <div class="cta-section" id="about">            <div class="cta-title">
                One AI Workspace.<br>
                Infinite Possibilities.
            </div>            <div class="cta-description">
                Stop switching between tools. Jarvis combines voice AI,
                image generation, coding intelligence, prompt engineering,
                and document reasoning into one premium SaaS experience.
            </div>            <div class="hero-buttons" style="justify-content:center;">                <a href="#" class="primary-btn">
                    Get Started Free
                </a>                <a href="#" class="secondary-btn">
                    Open Dashboard
                </a>            </div>        </div>        <!-- =====================================================
             FOOTER
        ====================================================== -->        <div class="footer">
            Built with intelligence • Powered by Jarvis AI
        </div>    </div>    """, unsafe_allow_html=True)   
    components.html("""
    <script>    const cards = window.parent.document.querySelectorAll('.feature-card');    cards.forEach((card) => {        card.addEventListener('mousemove', (e) => {            const rect = card.getBoundingClientRect();            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;            card.style.background = `
                radial-gradient(
                    circle at ${x}px ${y}px,
                    rgba(124,92,255,0.18),
                    rgba(255,255,255,0.03)
                )
            `;
        });        card.addEventListener('mouseleave', () => {            card.style.background = `
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.05),
                    rgba(255,255,255,0.02)
                )
            `;
        });    });    </script>
    """, height=0)
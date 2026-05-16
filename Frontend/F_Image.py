import streamlit as st
import textwrap
import random

def inject_css():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* =========================================================
       GLOBAL
    ========================================================= */

    .stApp{
        background:
        radial-gradient(circle at top left,#131726 0%,#09090f 40%),
        radial-gradient(circle at bottom right,#1b1033 0%,#09090f 45%);
        font-family:'Inter',sans-serif;
        color:white;
        overflow-x:hidden;
    }

    .jarvislab-wrapper{
        max-width:1200px;
        margin:auto;
        padding:40px 30px 100px 30px;
        position:relative;
    }

    /* =========================================================
       ANIMATED BACKGROUND BLOBS
    ========================================================= */

    .bg-blob{
        position:absolute;
        border-radius:50%;
        filter:blur(90px);
        opacity:.18;
        z-index:0;
        animation:blobFloat 10s ease-in-out infinite;
    }

    .blob1{
        width:300px;
        height:300px;
        background:#7c5cff;
        top:0;
        left:-100px;
    }

    .blob2{
        width:260px;
        height:260px;
        background:#00d4ff;
        right:-80px;
        top:200px;
        animation-delay:2s;
    }

    .blob3{
        width:240px;
        height:240px;
        background:#ff4ecd;
        bottom:100px;
        left:30%;
        animation-delay:4s;
    }

    @keyframes blobFloat{
        0%,100%{
            transform:translateY(0px) translateX(0px);
        }
        50%{
            transform:translateY(-30px) translateX(20px);
        }
    }

    /* =========================================================
       HERO SECTION
    ========================================================= */

    .hero-section{
        position:relative;
        z-index:2;
        text-align:center;
        padding-top:50px;

        animation:fadeUp 1s ease;
    }

    .hero-badge{
        display:inline-flex;
        align-items:center;
        gap:8px;

        padding:10px 18px;

        border-radius:999px;

        background:rgba(255,255,255,0.05);
        border:1px solid rgba(255,255,255,0.08);

        color:#cfcfff;
        font-size:13px;
        font-weight:600;

        margin-bottom:30px;

        backdrop-filter:blur(14px);
    }

    .pulse-dot{
        width:8px;
        height:8px;
        border-radius:50%;
        background:#7c5cff;

        animation:pulse 1.8s infinite;
    }

    @keyframes pulse{
        0%{
            transform:scale(1);
            opacity:1;
        }
        50%{
            transform:scale(1.8);
            opacity:.4;
        }
        100%{
            transform:scale(1);
            opacity:1;
        }
    }

    /* =========================================================
       LOGO
    ========================================================= */

    .logo{
        font-size:6rem;
        font-weight:800;
        letter-spacing:-2px;

        position:relative;

        display:inline-block;

        animation:logoEntry 1s ease;
    }

    .logo-gradient{
        position:relative;

        background:linear-gradient(
        90deg,
        #7C5CFF,
        #00D4FF,
        #FF4ECD,
        #7C5CFF
        );

        background-size:300% 300%;

        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;

        animation:gradientMove 6s ease infinite;

        filter:drop-shadow(0 0 20px rgba(124,92,255,.35));
    }

    .logo-gradient::after{
        content:"";

        position:absolute;

        top:0;
        left:-140%;

        width:140%;
        height:100%;

        background:linear-gradient(
        120deg,
        transparent,
        rgba(255,255,255,.35),
        transparent
        );

        transform:skewX(-20deg);

        animation:shimmer 4s infinite;
    }

    @keyframes gradientMove{
        0%{background-position:0% 50%;}
        50%{background-position:100% 50%;}
        100%{background-position:0% 50%;}
    }

    @keyframes shimmer{
        0%{
            left:-140%;
            opacity:0;
        }

        30%{
            opacity:1;
        }

        60%{
            left:140%;
            opacity:.8;
        }

        100%{
            left:140%;
            opacity:0;
        }
    }

    @keyframes logoEntry{
        from{
            opacity:0;
            transform:translateY(25px);
            filter:blur(10px);
        }

        to{
            opacity:1;
            transform:translateY(0);
            filter:blur(0);
        }
    }

    /* =========================================================
       SUBTEXT
    ========================================================= */

    .hero-sub{
        margin-top:20px;
        font-size:18px;
        line-height:1.8;
        color:#b9bfd3;

        max-width:820px;
        margin-left:auto;
        margin-right:auto;
    }

    /* =========================================================
       BUTTONS
    ========================================================= */

    .button-row{
        display:flex;
        justify-content:center;
        gap:18px;
        margin-top:40px;
        flex-wrap:wrap;
    }

    .saas-btn{
        padding:14px 26px;
        border-radius:14px;

        font-size:15px;
        font-weight:600;

        text-decoration:none;

        transition:.3s ease;

        position:relative;
        overflow:hidden;
    }

    .primary-btn{
        background:linear-gradient(135deg,#7c5cff,#ff4ecd);
        color:white;

        box-shadow:
        0 10px 30px rgba(124,92,255,.35);
    }

    .primary-btn:hover{
        transform:translateY(-4px);
        box-shadow:
        0 14px 40px rgba(124,92,255,.5);
    }

    .secondary-btn{
        background:rgba(255,255,255,.04);
        border:1px solid rgba(255,255,255,.08);
        color:#d9d9ff;
        backdrop-filter:blur(12px);
    }

    .secondary-btn:hover{
        background:rgba(255,255,255,.08);
        transform:translateY(-4px);
    }

    /* =========================================================
       FEATURE GRID
    ========================================================= */

    .feature-grid{
        margin-top:90px;

        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(260px,1fr));

        gap:24px;

        position:relative;
        z-index:2;
    }

    .feature-card{
        padding:28px;

        border-radius:24px;

        background:rgba(255,255,255,.04);

        border:1px solid rgba(255,255,255,.08);

        backdrop-filter:blur(18px);

        transition:.35s ease;

        position:relative;

        overflow:hidden;

        animation:fadeUp 1s ease;
    }

    .feature-card::before{
        content:"";

        position:absolute;

        inset:0;

        background:linear-gradient(
        135deg,
        rgba(124,92,255,.12),
        transparent,
        rgba(0,212,255,.08)
        );

        opacity:0;

        transition:.4s ease;
    }

    .feature-card:hover::before{
        opacity:1;
    }

    .feature-card:hover{
        transform:translateY(-8px);

        border-color:rgba(124,92,255,.3);

        box-shadow:
        0 18px 45px rgba(0,0,0,.35),
        0 0 30px rgba(124,92,255,.12);
    }

    .feature-icon{
        font-size:2rem;
        margin-bottom:18px;
    }

    .feature-title{
        font-size:20px;
        font-weight:700;
        margin-bottom:12px;
        color:white;
    }

    .feature-desc{
        color:#b6bdd1;
        line-height:1.7;
        font-size:14px;
    }

    /* =========================================================
       USER GUIDE
    ========================================================= */

    .guide-box{
        margin-top:100px;

        background:
        linear-gradient(
        135deg,
        rgba(124,92,255,.12),
        rgba(255,78,205,.06)
        );

        border:1px solid rgba(255,255,255,.08);

        border-radius:30px;

        padding:50px;

        position:relative;
        overflow:hidden;

        backdrop-filter:blur(18px);

        animation:fadeUp 1.2s ease;
    }

    .guide-box::before{
        content:"";

        position:absolute;

        width:400px;
        height:400px;

        border-radius:50%;

        background:radial-gradient(
        circle,
        rgba(124,92,255,.15),
        transparent
        );

        top:-150px;
        right:-150px;
    }

    .guide-title{
        font-size:2rem;
        font-weight:800;
        margin-bottom:30px;

        background:linear-gradient(90deg,#ffffff,#c6d4ff);

        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }

    .guide-item{
        color:#c9d0e2;
        line-height:1.9;
        margin-bottom:14px;
        font-size:15px;

        transition:.3s ease;
    }

    .guide-item:hover{
        transform:translateX(6px);
        color:white;
    }

    /* =========================================================
       FADEUP
    ========================================================= */

    @keyframes fadeUp{
        from{
            opacity:0;
            transform:translateY(20px);
        }

        to{
            opacity:1;
            transform:translateY(0);
        }
    }

    /* =========================================================
       RESPONSIVE
    ========================================================= */

    @media(max-width:768px){

        .logo{
            font-size:4rem;
        }

        .hero-sub{
            font-size:16px;
        }

        .guide-box{
            padding:30px;
        }
    }
    
    /* =========================
       STREAMLIT BUTTON STYLING
    ========================== */

    .stButton > button {
        background: linear-gradient(135deg, #7c3aed, #ec4899) !important;
        color: white !important;

        border: none !important;
        border-radius: 12px !important;

        padding: 10px 18px !important;
        font-size: 14px !important;
        font-weight: 600 !important;

        box-shadow: 0 8px 25px rgba(124, 58, 237, 0.35) !important;

        transition: all 0.25s ease !important;

        position: relative;
        overflow: hidden;
    }

    /* Hover effect */
    .stButton > button:hover {
        transform: translateY(-2px) scale(1.02) !important;
        box-shadow: 0 12px 35px rgba(236, 72, 153, 0.45) !important;
        border: none !important;
    }

    /* Click effect */
    .stButton > button:active {
        transform: scale(0.98) !important;
    }

    /* Optional glow animation */
    .stButton > button::before {
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.25),
            transparent
        );
        transition: left 0.5s ease;
    }

    .stButton > button:hover::before {
        left: 100%;
    }

    </style>
    """, unsafe_allow_html=True)

def landing_section():
    st.markdown("""
    <div class="jarvislab-wrapper">
        <!-- Animated Background -->
        <div class="bg-blob blob1"></div>
        <div class="bg-blob blob2"></div>
        <div class="bg-blob blob3"></div>
        <!-- HERO -->
        <div class="hero-section">
            <div class="hero-badge">
                <div class="pulse-dot"></div>
                AI Powered Image Generation Platform
            </div>
            <div class="logo">
                <span class="logo-gradient">
                    JarvisLab
                </span>
            </div>
            <div class="hero-sub">
                Generate stunning AI-powered images from simple prompts.
                Transform imagination into cinematic visuals, artworks,
                realistic renders, anime, product concepts, wallpapers,
                and creative assets instantly using advanced multimodal AI.
            </div>
            <div class="button-row">
                <a href="#" class="saas-btn primary-btn">
                    ✨ Generate Images
                </a>
                <a href="#" class="saas-btn secondary-btn">
                    🚀 Explore Features
                </a>
            </div>
        </div>
        <!-- FEATURE GRID -->
        <div class="feature-grid">
            <div class="feature-card">
                <div class="feature-icon">🎨</div>
                <div class="feature-title">
                    Prompt to Image
                </div>
                <div class="feature-desc">
                    Describe your imagination naturally and let AI
                    generate ultra high-quality visuals instantly.
                </div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <div class="feature-title">
                    Lightning Fast Generation
                </div>
                <div class="feature-desc">
                    Optimized AI pipelines generate images rapidly
                    while maintaining premium visual quality.
                </div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🧠</div>
                <div class="feature-title">
                    Intelligent Prompt Understanding
                </div>
                <div class="feature-desc">
                    AI understands cinematic lighting, styles,
                    compositions, emotions, and artistic direction.
                </div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🌌</div>
                <div class="feature-title">
                    Multiple Art Styles
                </div>
                <div class="feature-desc">
                    Generate anime, realistic renders, futuristic art,
                    game concepts, logos, wallpapers, and more.
                </div>
            </div>
        </div>
        <!-- USER GUIDE -->
        <div class="guide-box">
            <div class="guide-title">
                JarvisLab User Guide
            </div>
            <div class="guide-item">
                ✨ Describe your imagination naturally and the AI will generate visuals instantly.
            </div>
            <div class="guide-item">
                🎨 Add styles like cinematic, anime, realistic, futuristic, cyberpunk, or fantasy.
            </div>
            <div class="guide-item">
                🌌 Mention lighting, colors, camera angle, and environment for better results.
            </div>
            <div class="guide-item">
                ⚡ Generate wallpapers, characters, posters, concepts, thumbnails, and product ideas.
            </div>
            <div class="guide-item">
                🧠 AI intelligently enhances prompts for better image composition and quality.
            </div>
            <div class="guide-item">
                🚀 Experiment with different prompts to unlock creative possibilities.
            </div>
            <div class="guide-item">
                🔍 Use detailed prompts for cinematic and highly realistic outputs.
            </div>
            <div class="guide-item">
                📸 Generate social media content, branding assets, and creative inspirations instantly.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    return st.button("🚀 Get Started")


def prompt_section():

    st.markdown('<div class="section-header">✨ Create Your Masterpiece</div>', unsafe_allow_html=True)
    
    prompt = st.text_area(
        "Describe your vision",
        placeholder="e.g., A futuristic city at sunset with flying cars, neon lights, and holographic billboards...",
        height=200,
        label_visibility="collapsed"
    )

    generate = st.button("🎨 Generate Image")
    return prompt, generate
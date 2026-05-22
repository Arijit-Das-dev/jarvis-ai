import streamlit as st



def inject_css():
     st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    /* =========================================================
       GLOBAL
    ========================================================= */

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(124,92,255,0.14), transparent 30%),
            radial-gradient(circle at bottom right, rgba(0,212,255,0.12), transparent 30%),
            linear-gradient(135deg, #050816 0%, #090d1f 35%, #0d1024 70%, #060816 100%);
        color: white;
        overflow-x: hidden;
    }

    [data-testid="stHeader"]{
        background: transparent;
    }

    .block-container{
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 1250px;
    }

    /* =========================================================
       FLOATING BACKGROUND
    ========================================================= */

    .floating-orb{
        position:absolute;
        border-radius:50%;
        filter: blur(80px);
        opacity:0.25;
        pointer-events:none;
        animation: floatOrb 10s ease-in-out infinite;
    }

    .orb1{
        width:260px;
        height:260px;
        background:#7c5cff;
        top:-80px;
        right:-80px;
    }

    .orb2{
        width:220px;
        height:220px;
        background:#00d4ff;
        bottom:-60px;
        left:-60px;
        animation-delay: -5s;
    }

    @keyframes floatOrb{
        0%,100%{
            transform:translateY(0px) translateX(0px);
        }
        50%{
            transform:translateY(-30px) translateX(15px);
        }
    }

    /* =========================================================
       HERO SECTION
    ========================================================= */

    .jarvislab-wrapper{
        position:relative;
        overflow:hidden;

        background: rgba(12,18,38,0.72);
        border:1px solid rgba(255,255,255,0.08);

        backdrop-filter: blur(24px);

        border-radius:32px;

        padding:70px;

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
       BADGE
    ========================================================= */

    .hero-badge{
        display:inline-flex;
        align-items:center;
        gap:10px;

        padding:10px 18px;

        border-radius:999px;

        background: rgba(124,92,255,0.12);

        border:1px solid rgba(124,92,255,0.25);

        color:#c8bcff;

        font-size:13px;
        font-weight:600;
        letter-spacing:0.4px;

        margin-bottom:28px;

        animation: badgeGlow 4s infinite ease-in-out;
    }

    @keyframes badgeGlow{
        0%,100%{
            box-shadow:0 0 0px rgba(124,92,255,0);
        }
        50%{
            box-shadow:0 0 22px rgba(124,92,255,0.45);
        }
    }

    /* =========================================================
       LOGO / TITLE
    ========================================================= */

    .logo {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom:20px;
    }

    .logo-icon{
        width:58px;
        height:58px;

        border-radius:18px;

        display:flex;
        align-items:center;
        justify-content:center;

        background:
            linear-gradient(135deg,
            rgba(124,92,255,0.22),
            rgba(0,212,255,0.16));

        border:1px solid rgba(255,255,255,0.08);

        box-shadow:
            0 0 35px rgba(124,92,255,0.35);

        font-size:26px;

        animation: iconFloat 4s ease-in-out infinite;
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
        font-size:4.8rem;
        font-weight:900;
        line-height:1;

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

        animation: gradientFlow 8s linear infinite;

        letter-spacing:-3px;
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
        color:#8b93b7;
        font-size:14px;
        margin-top:8px;
        letter-spacing:0.6px;
    }

    /* =========================================================
       HERO DESCRIPTION
    ========================================================= */

    .hero-desc{
        margin-top:30px;

        max-width:850px;

        font-size:18px;
        line-height:1.9;

        color:#aeb7d1;
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

        margin-top:38px;
    }

    .feature-tag{
        padding:12px 18px;

        border-radius:14px;

        background: rgba(255,255,255,0.04);

        border:1px solid rgba(255,255,255,0.08);

        color:#d8dff5;

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

        border:1px solid rgba(124,92,255,0.35);

        box-shadow:
            0 10px 25px rgba(124,92,255,0.18);
    }

    /* =========================================================
       GUIDE SECTION
    ========================================================= */

    .guide-section{
        margin-top:60px;
    }

    .guide-title{
        font-size:28px;
        font-weight:800;
        margin-bottom:28px;

        color:white;
    }

    .guide-grid{
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
        gap:20px;
    }

    .guide-card{
        background: rgba(255,255,255,0.035);

        border:1px solid rgba(255,255,255,0.08);

        border-radius:22px;

        padding:26px;

        transition:0.35s ease;

        position:relative;
        overflow:hidden;
    }

    .guide-card::after{
        content:'';
        position:absolute;
        top:0;
        left:0;
        width:100%;
        height:2px;

        background:linear-gradient(
            90deg,
            #7C5CFF,
            #00D4FF
        );

        transform:scaleX(0);
        transform-origin:left;

        transition:0.4s ease;
    }

    .guide-card:hover::after{
        transform:scaleX(1);
    }

    .guide-card:hover{
        transform:translateY(-6px);

        border-color:rgba(124,92,255,0.25);

        box-shadow:
            0 15px 35px rgba(0,0,0,0.35),
            0 0 30px rgba(124,92,255,0.12);
    }

    .guide-icon{
        font-size:26px;
        margin-bottom:16px;
    }

    .guide-text{
        color:#c7d0ea;
        line-height:1.8;
        font-size:15px;
    }

    /* =========================================================
       BUTTON STYLES
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

        font-weight:700;

        font-size:15px;

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

        background:linear-gradient(
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

        .jarvislab-wrapper{
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

def render_promptlab_home():

    st.markdown("""
    <style>
    .glass-wrapper {
        display: flex;
        justify-content: center;
        gap: 25px;
        margin-top: 20px;
        flex-wrap: wrap;
    }
    
    .glass-card-mini {
        width: 220px;
        padding: 25px;
        border-radius: 18px;
        background: rgba(30,30,50,0.5);
        backdrop-filter: blur(12px);
        border:1px solid rgba(255,255,255,0.08);
        box-shadow: 0 8px 30px rgba(0,0,0,0.4);
        color:#d4d4ff;
        font-size:14px;
        line-height:1.6;
        text-align:center;
        transition: all 0.35s ease;
        animation: fadeUp 0.8s ease forwards;
        opacity: 0;
    }

    .glass-card-mini:nth-child(1) { animation-delay: 0.1s; }
    .glass-card-mini:nth-child(2) { animation-delay: 0.3s; }
    .glass-card-mini:nth-child(3) { animation-delay: 0.5s; }

    .glass-card-mini:hover {
        transform: translateY(-6px);
        box-shadow: 0 12px 40px rgba(139,92,246,0.4);
    }

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .promptlab-title {
        font-size: 56px;
        font-weight: 700;
        text-align: center;
        letter-spacing: -1px;

        background: linear-gradient(270deg, #a78bfa, #ec4899, #7c3aed, #c4b5fd);
        background-size: 600% 600%;

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        animation: gradientMove 6s ease infinite, fadeUp 1s ease forwards;
        opacity: 0;
    }
                
    /* underline base */
    .promptlab-title::after {
        content: "";
        position: absolute;
        left: 50%;
        bottom: -6px;
        width: 0%;
        height: 3px;
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        border-radius: 10px;
        transform: translateX(-50%);
        
        /* smooth animation */
        transition: width 0.4s ease;
    }

    /* animate on load */
    .promptlab-title.animate::after {
        width: 60%;
    }

    /* hover effect (expand slightly) */
    .promptlab-title:hover::after {
        width: 80%;
    }

    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    </style>
    <!-- 🔥 REMOVE BIG TOP SPACE -->
    <div style="text-align:center; margin-top:10px;">  
        <h1 style="
            font-size:42px;
            font-weight:700;
            background: linear-gradient(135deg,#ffffff,#c4b5fd);
            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;
            margin-bottom:15px;
        ">           
        <div class="promptlab-title animate">
         PromptLab
        </div>       
         </h1>
        <div class="glass-wrapper">
            <div class="glass-card-mini">
                🧠 Generate structured, production-ready prompts instantly.
            </div>
            <div class="glass-card-mini">
                ⚡ Turn simple ideas into powerful AI instructions.
            </div>
            <div class="glass-card-mini">
                🚀 Build better workflows with optimized prompts.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

import streamlit as st


def landingSection2():
    # ── Inject global CSS ──────────────────────────────────────────────────────
    st.markdown("""

    <div class="jarvislab-wrapper">
        <div class="floating-orb orb1"></div>
        <div class="floating-orb orb2"></div>
        <div class="hero-badge">
            ⚡ AI Prompt Engineering Platform
        </div>
        <div class="logo">
            <div class="logo-icon">
                🧠
            </div>
            <div class="logo-text">
                <div class="logo-main">
                    PromptLab
                </div>
                <div class="logo-sub">
                    GENERATE PROFESSIONAL AI PROMPTS IN SECONDS
                </div>
            </div>
        </div>
        <div class="hero-desc">
            PromptLab helps users generate
            <strong>high-quality AI prompts</strong>
            for every possible use case.
            Create prompts for
            YouTube content,
            AI agents,
            LLM system prompts,
            coding assistants,
            marketing,
            SEO,
            copywriting,
            automation workflows,
            startup ideas,
            image generation,
            chatbot personalities,
            emails,
            business strategy,
            education,
            resume generation,
            content writing,
            and much more.
            Turn simple ideas into
            structured, production-ready prompts instantly.
        </div>
        <div class="feature-tags">
            <div class="feature-tag">
                ⚡ Instant Prompt Generation
            </div>
            <div class="feature-tag">
                🧠 System Prompt Engineering
            </div>
            <div class="feature-tag">
                🎬 YouTube Content Prompts
            </div>
            <div class="feature-tag">
                💻 Coding & Debugging Prompts
            </div>
            <div class="feature-tag">
                🎨 Image Generation Prompts
            </div>
            <div class="feature-tag">
                📈 Marketing & SEO Prompts
            </div>
            <div class="feature-tag">
                🤖 AI Agent Instructions
            </div>
            <div class="feature-tag">
                🚀 Startup & Business Prompts
            </div>
        </div>
        <div class="guide-section">
            <div class="guide-title">
                User Guide
            </div>
            <div class="guide-grid">
                <div class="guide-card">
                    <div class="guide-icon">🧠</div>
                    <div class="guide-text">
                        Generate detailed prompts for LLMs like Gemini, GPT, Claude, Cohere, Llama, and Mistral instantly.
                    </div>
                </div>
                <div class="guide-card">
                    <div class="guide-icon">🎬</div>
                    <div class="guide-text">
                        Create YouTube video prompts including titles, hooks, thumbnails, scripts, SEO keywords, and storytelling structures.
                    </div>
                </div>
                <div class="guide-card">
                    <div class="guide-icon">⚡</div>
                    <div class="guide-text">
                        Build powerful system prompts for AI assistants, automation agents, customer support bots, and workflows.
                    </div>
                </div>
                <div class="guide-card">
                    <div class="guide-icon">🎨</div>
                    <div class="guide-text">
                        Generate cinematic image-generation prompts for Midjourney, Flux, Stable Diffusion, and AI art tools.
                    </div>
                </div>
                <div class="guide-card">
                    <div class="guide-icon">💻</div>
                    <div class="guide-text">
                        Create coding prompts for debugging, code generation, optimization, architecture planning, and interview preparation.
                    </div>
                </div>
                <div class="guide-card">
                    <div class="guide-icon">📈</div>
                    <div class="guide-text">
                        Generate marketing prompts for ads, copywriting, social media, sales funnels, branding, and audience targeting.
                    </div>
                </div>
                <div class="guide-card">
                    <div class="guide-icon">🚀</div>
                    <div class="guide-text">
                        Use PromptLab to brainstorm startup ideas, SaaS concepts, monetization strategies, and business execution plans.
                    </div>
                </div>
                <div class="guide-card">
                    <div class="guide-icon">📚</div>
                    <div class="guide-text">
                        Create educational prompts for notes, explanations, quizzes, tutorials, concept breakdowns, and learning roadmaps.
                    </div>
                </div>
            </div>
        </div>
    </div>

    """, unsafe_allow_html=True)

    col1, col2, col3, col5, col6 = st.columns(5)

    with col3:

        return st.button("Get started")
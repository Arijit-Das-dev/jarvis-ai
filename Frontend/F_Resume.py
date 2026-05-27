import streamlit as st
import streamlit.components.v1 as components
import time as t
# =========================
# CSS INJECTION
# =========================
def inject_css():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    /* =========================
       GLOBAL
    ========================== */

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    .stApp{
        background:
        radial-gradient(circle at top left, rgba(124,92,255,0.18), transparent 28%),
        radial-gradient(circle at bottom right, rgba(0,212,255,0.12), transparent 25%),
        linear-gradient(135deg,#07070d 0%, #0f1020 35%, #14162b 100%);
        overflow-x:hidden;
    }

    /* =========================
       MAIN WRAPPER
    ========================== */

    .jarviscv-wrapper{
        position:relative;
        width:100%;
        padding:40px 3% 80px 3%;
        overflow:hidden;
    }

    /* =========================
       FLOATING BLURS
    ========================== */

    .blur-orb{
        position:absolute;
        border-radius:50%;
        filter:blur(90px);
        opacity:0.4;
        animation: floatOrb 10s ease-in-out infinite;
        pointer-events:none;
    }

    .orb1{
        width:260px;
        height:260px;
        background:#7C5CFF;
        top:-60px;
        left:-50px;
    }

    .orb2{
        width:240px;
        height:240px;
        background:#00D4FF;
        right:-70px;
        bottom:100px;
        animation-delay:4s;
    }

    @keyframes floatOrb{
        0%{
            transform:translateY(0px) translateX(0px);
        }
        50%{
            transform:translateY(-20px) translateX(15px);
        }
        100%{
            transform:translateY(0px) translateX(0px);
        }
    }

    /* =========================
       HERO SECTION
    ========================== */

    .hero-container{
        position:relative;
        z-index:2;
        max-width:1350px;
        margin:auto;
        padding:70px;
        border-radius:34px;

        background:rgba(255,255,255,0.04);

        border:1px solid rgba(255,255,255,0.08);

        backdrop-filter: blur(18px);

        box-shadow:
        0 10px 40px rgba(0,0,0,0.45),
        inset 0 1px 0 rgba(255,255,255,0.05);

        overflow:hidden;
    }

    /* =========================
       TOP BADGE
    ========================== */

    .top-badge{
        display:inline-flex;
        align-items:center;
        gap:10px;

        padding:10px 18px;

        border-radius:999px;

        background:rgba(124,92,255,0.12);

        border:1px solid rgba(124,92,255,0.25);

        color:#cfc7ff;

        font-size:13px;
        font-weight:600;
        letter-spacing:0.4px;

        margin-bottom:28px;

        animation: fadeUp 0.8s ease;
    }

    .pulse-dot{
        width:8px;
        height:8px;
        border-radius:50%;
        background:#7C5CFF;

        box-shadow:0 0 15px #7C5CFF;

        animation:pulse 1.8s infinite;
    }

    @keyframes pulse{
        0%{
            transform:scale(1);
            opacity:1;
        }
        50%{
            transform:scale(1.5);
            opacity:0.5;
        }
        100%{
            transform:scale(1);
            opacity:1;
        }
    }

    /* =========================
       LOGO TEXT
    ========================== */

    .logo{
        display:flex;
        align-items:center;
        gap:14px;
        margin-bottom:30px;
    }

    .logo-text{
        font-size:5.4rem;
        font-weight:900;
        line-height:1;

        background: linear-gradient(
            90deg,
            #ffffff 0%,
            #7C5CFF 30%,
            #00D4FF 65%,
            #ffffff 100%
        );

        background-size:300% auto;

        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;

        animation: gradientFlow 6s linear infinite;
    }

    @keyframes gradientFlow{
        0%{
            background-position:0% center;
        }
        100%{
            background-position:300% center;
        }
    }

    /* =========================
       SUBTITLE
    ========================== */

    .hero-subtitle{
        max-width:850px;

        font-size:19px;
        line-height:1.9;

        color:rgba(255,255,255,0.72);

        margin-bottom:42px;

        animation:fadeUp 1s ease;
    }

    /* =========================
       BUTTONS
    ========================== */

    .hero-buttons{
        display:flex;
        gap:18px;
        flex-wrap:wrap;

        margin-top:15px;
    }

    .hero-btn{
        padding:15px 28px;
        border-radius:16px;
        font-size:15px;
        font-weight:700;

        text-decoration:none;

        transition:all 0.35s ease;

        display:inline-flex;
        align-items:center;
        gap:10px;
    }

    .primary-btn{
        background:linear-gradient(90deg,#7C5CFF,#00D4FF);
        color:white;

        box-shadow:
        0 0 30px rgba(124,92,255,0.45);
    }

    .primary-btn:hover{
        transform:translateY(-4px);
        box-shadow:
        0 0 50px rgba(124,92,255,0.7);
    }

    .secondary-btn{
        background:rgba(255,255,255,0.05);
        color:#e8e8ff;

        border:1px solid rgba(255,255,255,0.08);
    }

    .secondary-btn:hover{
        background:rgba(255,255,255,0.08);
        transform:translateY(-4px);
    }

    /* =========================
       FEATURE GRID
    ========================== */

    .feature-grid{
        display:grid;

        grid-template-columns:
        repeat(auto-fit,minmax(320px,1fr));

        gap:24px;

        margin-top:70px;
    }

    .feature-card{
        position:relative;

        background:rgba(255,255,255,0.03);

        border:1px solid rgba(255,255,255,0.08);

        border-radius:24px;

        padding:34px;

        overflow:hidden;

        transition:all 0.4s ease;
    }

    .feature-card:hover{
        transform:translateY(-10px);

        border-color:rgba(124,92,255,0.35);

        box-shadow:
        0 20px 50px rgba(0,0,0,0.45),
        0 0 40px rgba(124,92,255,0.18);
    }

    .feature-card::before{
        content:"";

        position:absolute;

        top:0;
        left:0;

        width:100%;
        height:4px;

        background:linear-gradient(90deg,#7C5CFF,#00D4FF);

        transform:scaleX(0);

        transform-origin:left;

        transition:transform 0.4s ease;
    }

    .feature-card:hover::before{
        transform:scaleX(1);
    }

    .feature-icon{
        font-size:42px;
        margin-bottom:18px;
    }

    .feature-title{
        font-size:24px;
        font-weight:800;
        color:white;
        margin-bottom:14px;
    }

    .feature-desc{
        color:rgba(255,255,255,0.68);
        line-height:1.8;
        font-size:15px;
        margin-bottom:20px;
    }

    .feature-list{
        display:flex;
        flex-direction:column;
        gap:12px;
    }

    .feature-item{
        color:#d6d9ff;
        font-size:14px;
        line-height:1.6;

        display:flex;
        gap:12px;
        align-items:flex-start;
    }

    .feature-item span{
        color:#00D4FF;
        font-weight:800;
    }

    /* =========================
       GUIDE SECTION
    ========================== */

    .guide-section{
        margin-top:70px;
    }

    .guide-title{
        font-size:34px;
        font-weight:800;
        color:white;

        margin-bottom:30px;
    }

    .guide-grid{
        display:grid;

        grid-template-columns:
        repeat(auto-fit,minmax(280px,1fr));

        gap:20px;
    }

    .guide-card{
        background:rgba(255,255,255,0.03);

        border:1px solid rgba(255,255,255,0.07);

        border-radius:20px;

        padding:26px;

        transition:all 0.35s ease;
    }

    .guide-card:hover{
        transform:translateY(-8px);

        border-color:rgba(0,212,255,0.25);

        box-shadow:
        0 0 30px rgba(0,212,255,0.12);
    }

    .guide-text{
        color:#dbe0ff;
        font-size:14px;
        line-height:1.8;
    }

    /* =========================
       ANIMATION
    ========================== */

    @keyframes fadeUp{
        from{
            opacity:0;
            transform:translateY(20px);
        }

        to{
            opacity:1;
            transform:translateY(0px);
        }
    }

    /* =========================
       RESPONSIVE
    ========================== */

    @media(max-width:900px){

        .hero-container{
            padding:45px 28px;
        }

        .logo-text{
            font-size:3.4rem;
        }

        .hero-subtitle{
            font-size:16px;
        }
    }
    
    /* =========================
   STREAMLIT BUTTON UI
    ========================= */

    .stButton > button {

        width: 100%;

        background:
        linear-gradient(
            135deg,
            #7C5CFF 0%,
            #5B8CFF 45%,
            #00D4FF 100%
        );

        color: white;

        border: 1px solid rgba(255,255,255,0.08);

        border-radius: 18px;

        padding: 0.95rem 1.4rem;

        font-size: 15px;

        font-weight: 700;

        letter-spacing: 0.3px;

        position: relative;

        overflow: hidden;

        transition: all 0.35s ease;

        box-shadow:
        0 10px 30px rgba(124,92,255,0.35),
        inset 0 1px 0 rgba(255,255,255,0.12);

        backdrop-filter: blur(10px);

        min-height: 54px;
    }


    /* =========================
    SHINE EFFECT
    ========================= */

    .stButton > button::before {

        content: "";

        position: absolute;

        top: 0;
        left: -120%;

        width: 70%;
        height: 100%;

        background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.22),
            transparent
        );

        transform: skewX(-20deg);

        transition: all 0.7s ease;
    }

    .stButton > button:hover::before {

        left: 140%;
    }


    /* =========================
    HOVER
    ========================= */

    .stButton > button:hover {

        transform:
        translateY(-4px)
        scale(1.01);

        box-shadow:
        0 18px 45px rgba(124,92,255,0.45),
        0 0 35px rgba(0,212,255,0.25);

        border-color:
        rgba(255,255,255,0.18);
    }


    /* =========================
    ACTIVE
    ========================= */

    .stButton > button:active {

        transform:
        scale(0.98);

        box-shadow:
        0 8px 20px rgba(124,92,255,0.28);
    }


    /* =========================
    FOCUS
    ========================= */

    .stButton > button:focus {

        outline: none !important;

        border:
        1px solid rgba(0,212,255,0.45);

        box-shadow:
        0 0 0 4px rgba(0,212,255,0.12),
        0 12px 35px rgba(124,92,255,0.35);
    }


    /* =========================
    OPTIONAL SECONDARY STYLE
    ========================= */

    div[data-testid="column"] .stButton.secondary > button {

        background:
        rgba(255,255,255,0.04);

        color:
        #e5e7ff;

        border:
        1px solid rgba(255,255,255,0.08);

        box-shadow:
        none;
    }

    div[data-testid="column"] .stButton.secondary > button:hover {

        background:
        rgba(255,255,255,0.08);

        border-color:
        rgba(124,92,255,0.25);

        box-shadow:
        0 0 25px rgba(124,92,255,0.18);
    }
    /* ============================= */
    /* MAIN TWO SECTION WRAPPER */
    /* ============================= */

    .resume-main-grid{
        display:flex;
        justify-content:center;
        align-items:stretch;
        gap:35px;
        margin-top:60px;
        flex-wrap:wrap;
    }

    /* ============================= */
    /* RESUME GLASS BOX */
    /* ============================= */

    .resume-box{
        position:relative;

        width:470px;
        min-height:620px;

        padding:45px;

        border-radius:30px;

        background:
            linear-gradient(
                145deg,
                rgba(25,20,40,0.82),
                rgba(12,10,24,0.92)
            );

        border:1px solid rgba(255,255,255,0.08);

        backdrop-filter: blur(24px);

        overflow:hidden;

        transition:0.45s ease;

        box-shadow:
            0 10px 40px rgba(0,0,0,0.45),
            0 0 80px rgba(124,92,255,0.12);
    }

    /* ============================= */
    /* HOVER */
    /* ============================= */

    .resume-box:hover{

        transform:
            translateY(-10px)
            scale(1.015);

        border:1px solid rgba(124,92,255,0.25);

        box-shadow:
            0 25px 60px rgba(0,0,0,0.55),
            0 0 120px rgba(124,92,255,0.25);
    }

    /* ============================= */
    /* ANIMATED GLOW */
    /* ============================= */

    .resume-glow{
        position:absolute;

        width:260px;
        height:260px;

        background:
            radial-gradient(
                circle,
                rgba(124,92,255,0.35),
                transparent 70%
            );

        top:-80px;
        right:-80px;

        filter:blur(40px);

        animation:floatGlow 6s ease-in-out infinite;
    }

    @keyframes floatGlow{

        0%{
            transform:translateY(0px);
        }

        50%{
            transform:translateY(20px);
        }

        100%{
            transform:translateY(0px);
        }
    }

    /* ============================= */
    /* CARD TAG */
    /* ============================= */

    .resume-tag{

        display:inline-block;

        padding:8px 18px;

        border-radius:999px;

        background:rgba(124,92,255,0.12);

        border:1px solid rgba(124,92,255,0.25);

        color:#b9a8ff;

        font-size:13px;
        font-weight:600;

        margin-bottom:30px;

        letter-spacing:0.5px;
    }

    /* ============================= */
    /* TITLE */
    /* ============================= */

    .resume-title{

        font-size:52px;
        font-weight:800;

        line-height:1.1;

        margin-bottom:25px;

        background:
            linear-gradient(
                90deg,
                #ffffff,
                #c4b5fd,
                #8b5cf6
            );

        background-size:300% 300%;

        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;

        animation:titleGradient 6s ease infinite;
    }

    @keyframes titleGradient{

        0%{
            background-position:0% 50%;
        }

        50%{
            background-position:100% 50%;
        }

        100%{
            background-position:0% 50%;
        }
    }

    /* ============================= */
    /* SUBTITLE */
    /* ============================= */

    .resume-subtitle{

        color:rgba(255,255,255,0.72);

        font-size:15px;

        line-height:1.9;

        margin-bottom:40px;
    }

    /* ============================= */
    /* FEATURES */
    /* ============================= */

    .resume-feature-list{

        display:flex;
        flex-direction:column;
        gap:18px;
    }

    .resume-feature{

        padding:16px 18px;

        border-radius:16px;

        background:rgba(255,255,255,0.03);

        border:1px solid rgba(255,255,255,0.05);

        color:#d8d8ff;

        font-size:14px;

        transition:0.3s ease;
    }

    .resume-feature:hover{

        transform:translateX(8px);

        border:1px solid rgba(124,92,255,0.25);

        background:rgba(124,92,255,0.08);
    }

    /* ============================= */
    /* BUTTON */
    /* ============================= */

    div.stButton > button{

        width:100%;

        margin-top:30px;

        height:58px;

        border:none;

        border-radius:18px;

        background:
            linear-gradient(
                90deg,
                #7C5CFF,
                #00D4FF
            );

        color:white;

        font-size:16px;
        font-weight:700;

        transition:0.35s ease;

        box-shadow:
            0 0 30px rgba(124,92,255,0.35);
    }

    div.stButton > button:hover{

        transform:
            translateY(-3px)
            scale(1.01);

        box-shadow:
            0 0 45px rgba(124,92,255,0.6);

        background:
            linear-gradient(
                90deg,
                #8d72ff,
                #36deff
            );
    }

    /* ============================= */
    /* RESPONSIVE */
    /* ============================= */

    @media(max-width:1100px){

        .resume-box{
            width:100%;
        }
    }
    
    /* FILE UPLOADER */

    [data-testid="stFileUploader"] {

        background: rgba(20,20,35,0.7);

        border: 1px solid rgba(124,92,255,0.25);

        padding: 25px;

        border-radius: 20px;

        backdrop-filter: blur(20px);

        box-shadow:
            0 0 30px rgba(124,92,255,0.15);

        transition: 0.3s ease;
    }

    [data-testid="stFileUploader"]:hover {

        border: 1px solid rgba(124,92,255,0.5);

        box-shadow:
            0 0 50px rgba(124,92,255,0.3);
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;600&display=swap');

    .parsing-loader{
        display:flex;
        justify-content:center;
        align-items:center;
        gap:14px;
        margin-top:120px;
        font-family:'Inter',sans-serif;
    }

    .loader-dots{
        display:flex;
        gap:8px;
    }

    .loader-dots span{
        width:10px;
        height:10px;
        border-radius:50%;

        background:linear-gradient(
            135deg,
            #7C5CFF,
            #00D4FF
        );

        animation:bounce 0.8s infinite ease-in-out;
    }

    .loader-dots span:nth-child(2){
        animation-delay:0.15s;
    }

    .loader-dots span:nth-child(3){
        animation-delay:0.3s;
    }

    .loader-text{

        font-size:20px;
        font-weight:600;

        background:linear-gradient(
            90deg,
            #ffffff,
            #c4b5fd,
            #7C5CFF
        );

        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }

    @keyframes bounce{

        0%,100%{
            transform:translateY(0px);
            opacity:0.5;
        }

        50%{
            transform:translateY(-8px);
            opacity:1;
        }
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700&display=swap');

    .jarvis-header{
        text-align:center;
        margin-top:-65px;
        margin-bottom:40px;  /* ADD THIS */

        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
    }

    .jarvis-title{
        font-size:60px;
        font-weight:700;

        background:linear-gradient(90deg,#7C5CFF,#00D4FF,#ffffff);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }

    .jarvis-subtitle{
        margin-top:10px;
        font-size:16px;
        color:#c4b5fd;
        opacity:0.85;
        letter-spacing:0.5px;
    }

    .ats-card{
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    padding:20px;
    animation:fadeIn 0.6s ease-in-out;
    }

    .ats-circle{
        width:140px;
        height:140px;
        border-radius:50%;
        border:8px solid #00ff99;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:38px;
        font-weight:bold;
        color:white;
        box-shadow:0 0 25px #00ff99;
        animation:pulse 2s infinite;
    }

    .ats-card p{
        margin-top:15px;
        font-size:18px;
        font-weight:600;
        color:white;
    }

    @keyframes pulse{
        0%{
            transform:scale(1);
        }
        50%{
            transform:scale(1.05);
        }
        100%{
            transform:scale(1);
        }
    }

    @keyframes fadeIn{
        from{
            opacity:0;
            transform:translateY(20px);
        }

        to{
            opacity:1;
            transform:translateY(0);
        }
    }     
    /* TEXT INPUT MAIN BOX */
    div[data-baseweb="input"] > div {
        background: rgba(20, 20, 20, 0.85);
        border: 1px solid rgba(0, 255, 153, 0.3);
        border-radius: 10px;
        padding: 8px;
        box-shadow: 0 0 10px rgba(0, 255, 153, 0.15);
        transition: all 0.3s ease-in-out;
    }

    /* INPUT FIELD TEXT */
    input {
        color: white !important;
        font-size: 16px !important;
        background: transparent !important;
    }

    /* FOCUS EFFECT */
    div[data-baseweb="input"] > div:focus-within {
        border: 1px solid #00ff99;
        box-shadow: 0 0 18px #00ff99;
        transform: scale(1.01);
    }

    /* PLACEHOLDER STYLE */
    input::placeholder {
        color: rgba(255, 255, 255, 0.4) !important;
    }
    
    /* =========================
       SUBHEADER STYLE
    ========================== */

    .jarvis-subheader {
        position: relative;
        font-size: 1.8rem;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 18px;
        padding-left: 18px;

        background: linear-gradient(
            90deg,
            #ffffff 0%,
            #d6ccff 35%,
            #8b5cf6 70%,
            #00d4ff 100%
        );

        background-size: 300% 300%;

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        animation:
            gradientFlow 6s ease infinite,
            fadeSlideUp 0.8s ease;
    }

    /* glowing left accent */
    .jarvis-subheader::before {
        content: "";
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 5px;
        height: 80%;

        border-radius: 30px;

        background: linear-gradient(
            180deg,
            #7c5cff,
            #00d4ff
        );

        box-shadow:
            0 0 12px rgba(124,92,255,0.8),
            0 0 25px rgba(0,212,255,0.4);

        animation: glowPulse 2.5s ease infinite;
    }

    /* animated underline */
    .jarvis-subheader::after {
        content: "";
        position: absolute;
        bottom: -6px;
        left: 18px;

        width: 120px;
        height: 2px;
        border-radius: 50px;

        background: linear-gradient(
            90deg,
            rgba(124,92,255,0),
            #7c5cff,
            #00d4ff,
            rgba(0,212,255,0)
        );

        background-size: 200% 100%;

        animation: lineMove 4s linear infinite;
    }

    /* =========================
       ANIMATIONS
    ========================== */

    @keyframes gradientFlow {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }

    @keyframes glowPulse {
        0%,100% {
            opacity: 1;
            transform: translateY(-50%) scaleY(1);
        }
        50% {
            opacity: 0.7;
            transform: translateY(-50%) scaleY(1.15);
        }
    }

    @keyframes lineMove {
        0% {
            background-position: 0% 50%;
        }
        100% {
            background-position: 200% 50%;
        }
    }

    @keyframes fadeSlideUp {
        from {
            opacity: 0;
            transform: translateY(12px);
        }
        to {
            opacity: 1;
            transform: translateY(0px);
        }
    }
    </style>
    """, unsafe_allow_html=True)

# =========================
# HTML SECTION
# =========================
def landing_section1():

    st.markdown("""
    <div class="jarviscv-wrapper">
        <div class="blur-orb orb1"></div>
        <div class="blur-orb orb2"></div>
        <div class="hero-container">
            <div class="top-badge">
                <div class="pulse-dot"></div>
                AI Resume Intelligence Platform
            </div>
            <div class="logo">
                <div class="logo-text">JarvisCV</div>
            </div>
            <div class="hero-subtitle">
                Build professional, recruiter-ready resumes with AI-powered career intelligence.
                Analyze ATS compatibility, optimize keywords, improve formatting, and generate
                high-impact resumes designed for modern hiring systems.
            </div>
            <!-- FEATURE GRID -->
            <div class="feature-grid">
                <div class="feature-card">
                    <div class="feature-icon">📄</div>
                    <div class="feature-title">
                        AI Resume Builder
                    </div>
                    <div class="feature-desc">
                        Generate clean, modern, recruiter-focused resumes with intelligent AI assistance.
                    </div>
                    <div class="feature-list">
                        <div class="feature-item">
                            <span>✓</span>
                            Create professional resumes instantly
                        </div>
                        <div class="feature-item">
                            <span>✓</span>
                            AI-generated career descriptions
                        </div>
                        <div class="feature-item">
                            <span>✓</span>
                            Modern ATS-friendly formatting
                        </div>
                        <div class="feature-item">
                            <span>✓</span>
                            Export high-quality resumes
                        </div>
                    </div>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🎯</div>
                    <div class="feature-title">
                        ATS Resume Analyzer
                    </div>
                    <div class="feature-desc">
                        Upload resumes and receive intelligent ATS scoring with optimization suggestions.
                    </div>
                    <div class="feature-list">
                        <div class="feature-item">
                            <span>✓</span>
                            Instant ATS compatibility score
                        </div>
                        <div class="feature-item">
                            <span>✓</span>
                            Keyword optimization analysis
                        </div>
                        <div class="feature-item">
                            <span>✓</span>
                            Detects formatting issues
                        </div>
                        <div class="feature-item">
                            <span>✓</span>
                            AI-powered resume improvements
                        </div>
                    </div>
                </div>
            </div>
            <!-- GUIDE SECTION -->
            <div class="guide-section">
                <div class="guide-title">
                    Why Use JarvisCV?
                </div>
                <div class="guide-grid">
                    <div class="guide-card">
                        <div class="guide-text">
                            🚀 Create recruiter-ready resumes optimized for modern hiring systems and ATS platforms.
                        </div>
                    </div>
                    <div class="guide-card">
                        <div class="guide-text">
                            🧠 AI intelligently improves resume structure, keywords, formatting, and readability.
                        </div>
                    </div>
                    <div class="guide-card">
                        <div class="guide-text">
                            🎯 Receive instant ATS scoring and identify weak areas affecting interview opportunities.
                        </div>
                    </div>
                    <div class="guide-card">
                        <div class="guide-text">
                            ⚡ Optimize resumes for specific job roles using AI-powered career recommendations.
                        </div>
                    </div>
                    <div class="guide-card">
                        <div class="guide-text">
                            📈 Improve recruiter visibility with intelligent keyword enhancement and content refinement.
                        </div>
                    </div>
                    <div class="guide-card">
                        <div class="guide-text">
                            ✨ Build clean, premium-quality resumes without needing design or formatting skills.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    start_button = st.button("Get started")

    return start_button

# =========================
# RESUME BUILDER SECTION
# =========================

def resumeBuilder():

    st.markdown("""
    <div class="resume-box resume-builder-card">
        <div class="resume-glow"></div>
        <div class="resume-tag">
            ✨ AI Resume Studio
        </div>
        <div class="resume-title">
            Resume Builder
        </div>
        <div class="resume-subtitle">
            Build professional ATS-optimized resumes using AI.  
            Generate clean layouts, structured sections, and industry-ready resumes instantly.
        </div>
        <div class="resume-feature-list">
            <div class="resume-feature">
                ⚡ AI Generated Resume Sections
            </div>
            <div class="resume-feature">
                🎯 ATS Friendly Formatting
            </div>
            <div class="resume-feature">
                📄 Export as Professional PDF
            </div>
            <div class="resume-feature">
                🧠 Smart Skills & Summary Suggestions
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    start1_btn =  st.button("Open Resume Builder", key="resume_builder_btn")

    return start1_btn

# =========================
# RESUME ANALYSIS SECTION
# =========================

def resumeAnalysis():

    st.markdown("""
    <div class="resume-box resume-analysis-card">
        <div class="resume-glow"></div>
        <div class="resume-tag">
            🔍 AI ATS Scanner
        </div>
        <div class="resume-title">
            Resume Analysis
        </div>
        <div class="resume-subtitle">
            Upload your resume and let AI analyze ATS compatibility, keyword optimization,
            formatting quality, and improvement areas instantly.
        </div>
        <div class="resume-feature-list">
            <div class="resume-feature">
                📊 ATS Score Detection
            </div>
            <div class="resume-feature">
                🐞 Resume Weak Point Analysis
            </div>
            <div class="resume-feature">
                🚀 AI Improvement Suggestions
            </div>
            <div class="resume-feature">
                💼 Recruiter Optimization Tips
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    start_btn2 = st.button("Analyze Resume", key="resume_analysis_btn")
    
    return start_btn2

# RESUME ANALYSIS HEADING SECTION
def heading():

    st.markdown("""
    <div class="jarvis-header">
        <div class="jarvis-title">
            JarvisCV Intelligence Engine
        </div>
        <div class="jarvis-subtitle">
            Upload your resume to get started
        </div>
    </div>
    """, unsafe_allow_html=True)

def parsing_loader():

    placeholder = st.empty()

    with placeholder:
        st.markdown("""
        <div class="parsing-loader">
            <div class="loader-dots">
                <span></span>
                <span></span>
                <span></span>
            </div>
            <div class="loader-text">
                Parsing document...
            </div>
        </div>
        """, unsafe_allow_html=True)

    t.sleep(5)
    placeholder.empty()

# =========================
# ANALYZER UI
# =========================

def analyzing_resume():
    placeholder = st.empty()

    with placeholder:
        st.markdown("""
        <div class="parsing-loader">
            <div class="loader-dots">
                <span></span>
                <span></span>
                <span></span>
            </div>
            <div class="loader-text">
                showing info about your resume...
            </div>
        </div>
        """, unsafe_allow_html=True)

    t.sleep(5)
    placeholder.empty()

def show_ats_score(score):

    st.markdown(f"""
    <div class="ats-card">
        <div class="ats-circle">
            <span>{score}/100</span>
        </div>
        <p>ATS SCORE</p>
    </div>
    """, unsafe_allow_html=True)

def subheader(text):

    st.markdown(
        f'''
        <div class="jarvis-subheader">
            {text}
        </div>
        ''',
        unsafe_allow_html=True
    )

def inject_css_2():
    st.markdown("""
    <style>

    /* =====================================================
       GLOBAL
    ===================================================== */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #0f1117;
        color: #ffffff;
    }

    section[data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* =====================================================
       MAIN CONTAINER
    ===================================================== */
    .main-container {
        padding: 2rem;
        border-radius: 22px;
        background: linear-gradient(
            145deg,
            rgba(255,255,255,0.03),
            rgba(255,255,255,0.01)
        );
        border: 1px solid rgba(255,255,255,0.08);
        backdrop-filter: blur(10px);
        margin-bottom: 2rem;
    }

    /* =====================================================
       HERO SECTION
    ===================================================== */
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 10px;
        color: white;
    }

    .hero-subtitle {
        color: #9ca3af;
        font-size: 1rem;
        margin-bottom: 2rem;
    }

    .highlight {
        color: #8b5cf6;
    }

    /* =====================================================
       TEMPLATE CARDS
    ===================================================== */
    .template-card {
        background: #161b22;
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 18px;
        padding: 20px;
        transition: 0.3s ease;
        text-align: center;
        height: 320px;
    }

    .template-card:hover {
        transform: translateY(-6px);
        border: 1px solid #8b5cf6;
        box-shadow: 0 0 25px rgba(139,92,246,0.3);
    }

    .template-title {
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 16px;
        color: white;
    }

    .resume-preview {
        background: linear-gradient(
            180deg,
            #ffffff 0%,
            #d1d5db 100%
        );
        border-radius: 10px;
        height: 200px;
        margin-bottom: 15px;
    }

    /* =====================================================
       SECTION BOX
    ===================================================== */
    .section-box {
        background: #161b22;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.06);
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 20px;
        color: #ffffff;
        border-left: 4px solid #8b5cf6;
        padding-left: 14px;
    }

    .section-desc {
        color: #9ca3af;
        margin-bottom: 1rem;
    }

    /* =====================================================
       STREAMLIT INPUTS
    ===================================================== */

    /* TEXT INPUT */
    .stTextInput input {
        background-color: #111827 !important;
        color: white !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        padding: 14px !important;
        font-size: 15px !important;
    }

    .stTextInput input:focus {
        border: 1px solid #8b5cf6 !important;
        box-shadow: 0 0 0 2px rgba(139,92,246,0.25) !important;
    }

    /* TEXT AREA */
    .stTextArea textarea {
        background-color: #111827 !important;
        color: white !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        padding: 14px !important;
    }

    .stTextArea textarea:focus {
        border: 1px solid #8b5cf6 !important;
        box-shadow: 0 0 0 2px rgba(139,92,246,0.25) !important;
    }

    /* DATE INPUT */
    .stDateInput input {
        background-color: #111827 !important;
        color: white !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
    }

    /* BUTTON */
    .stButton > button {
        width: 100%;
        border-radius: 14px;
        height: 50px;
        border: none;
        background: linear-gradient(
            135deg,
            #8b5cf6,
            #6366f1
        );
        color: white;
        font-size: 16px;
        font-weight: 700;
        transition: 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(139,92,246,0.35);
    }

    /* DOWNLOAD BUTTON */
    .stDownloadButton > button {
        width: 100%;
        border-radius: 14px;
        height: 50px;
        border: none;
        background: linear-gradient(
            135deg,
            #10b981,
            #059669
        );
        color: white;
        font-size: 16px;
        font-weight: 700;
        transition: 0.3s ease;
    }

    .stDownloadButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(16,185,129,0.35);
    }

    /* =====================================================
       LABELS
    ===================================================== */
    label {
        color: #e5e7eb !important;
        font-weight: 600 !important;
    }

    /* =====================================================
       SCROLLBAR
    ===================================================== */
    ::-webkit-scrollbar {
        width: 10px;
    }

    ::-webkit-scrollbar-track {
        background: #111827;
    }

    ::-webkit-scrollbar-thumb {
        background: #8b5cf6;
        border-radius: 10px;
    }
    
    /* =====================================================
    SELECT BOX
    ===================================================== */

    /* Main Selectbox Container */
    .stSelectbox > div > div {
        background-color: #111827 !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        min-height: 50px !important;
        transition: 0.3s ease;
    }

    /* Hover Effect */
    .stSelectbox > div > div:hover {
        border: 1px solid #8b5cf6 !important;
        box-shadow: 0 0 0 2px rgba(139,92,246,0.15);
    }

    /* Selected Text */
    .stSelectbox div[data-baseweb="select"] > div {
        color: white !important;
        font-size: 15px !important;
        padding-left: 6px;
    }

    /* Dropdown Icon */
    .stSelectbox svg {
        fill: #8b5cf6 !important;
    }

    /* Dropdown Popup */
    div[role="listbox"] {
        background-color: #111827 !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 12px !important;
        padding: 6px !important;
    }

    /* Dropdown Options */
    div[role="option"] {
        background-color: transparent !important;
        color: white !important;
        border-radius: 10px !important;
        margin-bottom: 4px;
        transition: 0.2s ease;
    }

    /* Hovered Option */
    div[role="option"]:hover {
        background-color: rgba(139,92,246,0.18) !important;
        color: #ffffff !important;
    }

    /* Selected Option */
    div[aria-selected="true"] {
        background-color: #8b5cf6 !important;
        color: white !important;
    }

    /* Label */
    .stSelectbox label {
        color: #e5e7eb !important;
        font-weight: 600 !important;
        margin-bottom: 8px !important;
    }

    </style>
    """, unsafe_allow_html=True)

# =========================================================
# HERO SECTION
# =========================================================
def hero_section():

    st.markdown("""
    <div class="main-container">
        <div class="hero-title">
            Build Your <span class="highlight">Professional Resume</span>
        </div>
        <div class="hero-subtitle">
            Create ATS-friendly resumes with beautiful templates
            in just a few minutes.
        </div>
    </div>
    """, unsafe_allow_html=True)

def template_section():

    st.markdown("""
    <div class="section-box">
        <div class="section-title">
            Choose Resume Template
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="template-card">
            <div class="template-title">Minimal</div>
            <div class="resume-preview"></div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="template-card">
            <div class="template-title">Classic</div>
            <div class="resume-preview"></div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="template-card">
            <div class="template-title">Modern</div>
            <div class="resume-preview"></div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# PROFESSIONAL SUMMARY
# =========================================================
def Personal_Information():

    st.markdown("""
    <div class="section-box">
        <div class="section-title">
            Personal Information
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# WORK EXPERIENCE
# =========================================================
def Work_Experience():

    st.markdown("""
    <div class="section-box">
        <div class="section-title">
            Work Experience
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# EDUCATION
# =========================================================
def Education():

    st.markdown("""
    <div class="section-box">
        <div class="section-title">
            Education
        </div>
    </div>
    """, unsafe_allow_html=True)

def Technical_Skills():

    st.markdown("""
    <div class="section-box">
        <div class="section-title">
            Technical Skills
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# PROJECTS
# =========================================================
def Projects():

    st.markdown("""
    <div class="section-box">
        <div class="section-title">
            Projects
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# CERTIFICATIONS
# =========================================================
def Certifications():

    st.markdown("""
    <div class="section-box">
        <div class="section-title">
            Certifications
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# DOWNLOAD SECTION
# =========================================================
def Download_Section():

    st.markdown("""
    <div class="section-box">
        <div class="section-title">
            Export Resume
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.download_button(
        label="Download Resume PDF",
        data="Sample Resume",
        file_name="resume.pdf",
        mime="application/pdf"
    )

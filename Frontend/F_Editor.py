import streamlit as st
from streamlit_monaco import st_monaco
import re 

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Jarvis Editor",
    layout="centered"
)

# ---------- GLOBAL CSS -----------
def inject_css():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp{
        background:
        radial-gradient(circle at top left, rgba(124,58,237,0.16), transparent 30%),
        radial-gradient(circle at bottom right, rgba(59,130,246,0.14), transparent 35%),
        linear-gradient(135deg,#060816 0%,#090b1d 35%,#0f1024 70%,#060816 100%);
        overflow-x:hidden;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"]{
        background: rgba(8,10,24,0.92);
        border-right:1px solid rgba(255,255,255,0.06);
        backdrop-filter: blur(20px);
    }

    section[data-testid="stSidebar"] *{
        color:white !important;
    }

    .block-container{
        padding-top: 2rem !important;
        max-width: 1200px !important;
    }

    header[data-testid="stHeader"]{
        background: transparent;
    }

    /* HERO SECTION */

    .jarvis-wrapper{
        position:relative;
        overflow:hidden;
        border-radius:32px;
        padding:70px 60px;
        background:
        linear-gradient(135deg,
        rgba(18,20,40,0.94) 0%,
        rgba(12,14,30,0.96) 100%);
        border:1px solid rgba(255,255,255,0.08);

        box-shadow:
        0 10px 40px rgba(0,0,0,0.45),
        0 0 120px rgba(124,58,237,0.16);

        margin-bottom:40px;
    }

    .jarvis-wrapper::before{
        content:'';
        position:absolute;
        inset:0;
        background:
        radial-gradient(circle at top right,
        rgba(124,58,237,0.22),
        transparent 35%);
        pointer-events:none;
    }

    .orb{
        position:absolute;
        border-radius:50%;
        filter:blur(90px);
        opacity:0.28;
        pointer-events:none;
    }

    .orb1{
        width:240px;
        height:240px;
        background:#7c3aed;
        top:-80px;
        right:-50px;
        animation: float 9s ease-in-out infinite;
    }

    .orb2{
        width:220px;
        height:220px;
        background:#2563eb;
        bottom:-80px;
        left:-50px;
        animation: float 10s ease-in-out infinite;
    }

    @keyframes float{
        0%,100%{
            transform:translateY(0px);
        }
        50%{
            transform:translateY(-20px);
        }
    }

    .badge{
        display:inline-flex;
        align-items:center;
        gap:10px;

        padding:10px 18px;
        border-radius:999px;

        background:rgba(124,58,237,0.14);
        border:1px solid rgba(124,58,237,0.35);
        color:#c4b5fd;
        font-size:13px;
        font-weight:600;
        letter-spacing:0.08em;
        text-transform:uppercase;

        margin-bottom:30px;
    }
    .pulse{
        width:8px;
        height:8px;
        border-radius:50%;
        background:#8b5cf6;
        box-shadow:0 0 10px #8b5cf6;
        animation:pulse 2s infinite;
    }
    @keyframes pulse{
        0%,100%{
            transform:scale(1);
            opacity:1;
        }
        50%{
            transform:scale(1.5);
            opacity:0.5;
        }
    }
    .hero-title{
        font-size: clamp(42px,6vw,78px);
        font-weight:900;
        line-height:1.05;
        letter-spacing:-0.04em;
        color:white;
        margin-bottom:25px;
        max-width:900px;
    }
    .hero-title span{
        background:linear-gradient(
        135deg,
        #a78bfa 0%,
        #60a5fa 50%,
        #ec4899 100%
        );

        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }
    .hero-sub{
        max-width:720px;
        font-size:19px;
        line-height:1.8;
        color:rgba(220,220,240,0.72);
        margin-bottom:40px;
    }
    .button-row{
        display:flex;
        gap:18px;
        flex-wrap:wrap;
        margin-bottom:60px;
    }
    .primary-btn{
        padding:16px 28px;
        border-radius:16px;
        text-decoration:none;
        background:linear-gradient(
        135deg,
        #7c3aed 0%,
        #4f46e5 100%
        );
        color:white !important;
        font-weight:600;
        font-size:15px;
        transition:0.3s ease;
        box-shadow:
        0 8px 25px rgba(124,58,237,0.45);
    }
    .primary-btn:hover{
        transform:translateY(-4px);
        box-shadow:
        0 14px 40px rgba(124,58,237,0.65);
    }
    .secondary-btn{
        padding:16px 28px;
        border-radius:16px;
        text-decoration:none;
        background:rgba(255,255,255,0.04);
        border:1px solid rgba(255,255,255,0.08);
        color:#d4d4ff !important;
        font-weight:500;
        font-size:15px;
        transition:0.3s ease;
    }
    .secondary-btn:hover{
        background:rgba(255,255,255,0.08);
        transform:translateY(-4px);
    }
    /* STATS */
    .stats-grid{
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
        gap:22px;
        margin-top:10px;
    }
    .stat-card{
        background:rgba(255,255,255,0.03);
        border:1px solid rgba(255,255,255,0.06);
        border-radius:22px;
        padding:28px;
        transition:0.35s ease;
    }
    .stat-card:hover{
        transform:translateY(-6px);
        border-color:rgba(124,58,237,0.35);
    }
    .stat-number{
        font-size:42px;
        font-weight:800;

        background:linear-gradient(
        135deg,
        #c4b5fd,
        #60a5fa
        );

        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }

    .stat-label{
        color:rgba(220,220,240,0.62);
        margin-top:8px;
        font-size:14px;
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

# Landing Page 1
def landing_section1():
    st.markdown("""
    <div class="jarvis-wrapper">
        <div class="orb orb1"></div>
        <div class="orb orb2"></div>
        <div class="badge">
            <div class="pulse"></div>
            AI POWERED DEVELOPMENT ENVIRONMENT
        </div>
        <div class="hero-title">
            Build Faster with
            <span>Jarvis Editor</span>
        </div>
        <div class="hero-sub">
            Jarvis Editor is an intelligent AI-powered coding environment
            designed to help developers write, debug, optimize, and understand
            code faster using advanced LLMs and real-time AI assistance.
        </div>
        <div class="button-row">
            <a href="#" class="primary-btn">🚀 Launch Editor</a>
            <a href="#" class="secondary-btn">⚡ Explore Features</a>
        </div>
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">AI</div>
                <div class="stat-label">
                    Integrated Copilot Assistance
                </div>
            </div>
            <div class="stat-card">
                <div class="stat-number">24/7</div>
                <div class="stat-label">
                    Real-time Debugging Help
                </div>
            </div>
            <div class="stat-card">
                <div class="stat-number">∞</div>
                <div class="stat-label">
                    Programming Possibilities
                </div>
            </div>
            <div class="stat-card">
                <div class="stat-number">LLM</div>
                <div class="stat-label">
                    Powered Intelligent Compiler
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)

    col1,col2,_,_,col3, _ = st.columns(6)

    with col2:
        button = st.button("🚀 Get Started")
    
    return button

# ---------- CODE EDITOR ----------
def code_editor():
    st.subheader("🖥️ Code Editor")

    languages = [
        "python", "javascript", "cpp", "java", "c",
        "html", "css", "sql"
    ]

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        lang = st.selectbox("Language", languages, index=None)

    code = st_monaco(
        language=lang,
        theme="vs-dark",
        height=300   # medium height
    )

    # small submit button
    btn_col, _ = st.columns([1, 6])
    with btn_col:
        submit = st.button("Submit")

    return code, submit

def normalize_llm_output(text: str) -> str:
    # Convert ### **CORRECT** / ### **WRONG** → **CORRECT**
    text = re.sub(
        r'^\s*#{1,6}\s*\*\*(.*?)\*\*',
        r'**\1**',
        text,
        flags=re.MULTILINE
    )
    return text.strip()

def output_box(content: str, title: str = "OUTPUT"):
    content = normalize_llm_output(content)

    st.markdown(f"""
    <div class="output-container">
        <div class="output-title">
            🧠 {title}
        </div>
    """, unsafe_allow_html=True)

    # Let Streamlit render markdown
    st.markdown(content)

    st.markdown("</div>", unsafe_allow_html=True)

def ai_chat_input():
    # Clear Chat button
    if st.button("Clear Chat 🗑️", use_container_width=False):
        st.session_state["chat_messages"] = []
        st.rerun()
    
    # Inject chat CSS
    st.markdown("""
    <style>
    #chat-history-box {
        max-height: 500px;
        overflow-y: auto;
        padding: 10px;
        background: rgba(10, 10, 25, 0.5);
        border-radius: 15px;
        border: 1px solid rgba(147, 51, 234, 0.3);
    }
    .user-bubble {
        background: linear-gradient(135deg, #8b5cf6, #d946ef);
        color: white;
        float: right;
        clear: both;
        border-radius: 12px 12px 4px 12px;
        padding: 8px 12px;
        max-width: 95%;
        margin: 4px 0;
        box-shadow: 0 2px 8px rgba(139, 92, 246, 0.3);
        font-size: 14px;
    }
    .assistant-bubble {
        background: rgba(30, 20, 60, 0.8);
        color: #e0d4ff;
        float: left;
        clear: both;
        border-radius: 12px 12px 12px 4px;
        border: 1px solid rgba(167, 139, 250, 0.3);
        padding: 8px 12px;
        max-width: 95%;
        margin: 4px 0;
        font-size: 14px;
    }
    .message-label {
        font-size: 10px;
        margin-bottom: 3px;
        font-weight: 600;
    }
    .user-label {
        color: #c4b5fd;
    }
    .assistant-label {
        color: #a78bfa;
    }
    .clearfix {
        clear: both;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Chat history container
    st.markdown('<div id="chat-history-box">', unsafe_allow_html=True)
    
    # Render all messages
    for msg in st.session_state["chat_messages"]:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="user-bubble">
                <div class="message-label user-label">You <span style="float:right">{msg["time"]}</span></div>
                {msg["content"]}
            </div>
            <div class="clearfix"></div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="assistant-bubble">
                <div class="message-label assistant-label">🤖 Jarvis <span style="float:right">{msg["time"]}</span></div>
                {msg["content"]}
            </div>
            <div class="clearfix"></div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Auto-scroll
    st.markdown("""
    <script>
    const chatBox = document.getElementById('chat-history-box');
    if (chatBox) chatBox.scrollTop = chatBox.scrollHeight;
    </script>
    """, unsafe_allow_html=True)
    
    # Input
    user_input = st.chat_input("Ask Jarvis...")
    
    return user_input
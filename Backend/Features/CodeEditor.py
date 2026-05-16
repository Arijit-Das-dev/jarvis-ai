import streamlit as st
import Frontend.F_Editor as ui 
from DB.MongoDB.EditorDB import save_user_code, save_user_query
from Backend.Services.modelMistral import modelMistral
import uuid
import os
import sys
from datetime import datetime

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

st.set_page_config(layout="wide")
ui.inject_css()

# ---------- Session variables (TOP) ----------
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

# ---------------- Session State ----------------
if "started" not in st.session_state:
    st.session_state.started = False

if "chat_messages" not in st.session_state:
    st.session_state["chat_messages"] = []

userId = st.session_state.user_id

# ---------------- Landing Page ----------------
if not st.session_state.started:
    start = ui.landing_section1() 

    # If "Get Started" clicked, update session_state and rerun
    if start:
        st.session_state.started = True
        st.rerun()

else:
    # Chat in existing sidebar
    with st.sidebar:
        user_input = ui.ai_chat_input()

        if user_input:
            with st.spinner("🤖 Jarvis is thinking..."):
                # Append user message
                st.session_state["chat_messages"].append({
                    "role": "user",
                    "content": user_input,
                    "time": datetime.now().strftime("%I:%M %p")
                })

                # Save to DB
                save_user_query(user_id=userId, user_query=user_input)

                # Call AI
                result2 = modelMistral.mistralModel2(code2=user_input)

                # Append AI response
                st.session_state["chat_messages"].append({
                    "role": "assistant",
                    "content": result2,
                    "time": datetime.now().strftime("%I:%M %p")
                })

            st.rerun()
    
    # Main area for editor
    code, submit = ui.code_editor()

    if submit:
        # save user code to DB
        save_user_code(user_id=userId, user_code=code)

        # Extract result from Backend/Services/modelMistral.py
        result_1 = modelMistral.mistralModel1(code1=code)

        # Send to UI
        ui.output_box(result_1)
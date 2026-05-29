import streamlit as st
import Frontend.F_PromptEng as ui
import uuid
from Backend.Services.gemini_client import modelGemini
from DB.mongo_db.PromptEngDB import save_user_query, save_gemini_response

ui.inject_css()

# ---------- Session variables (TOP) ----------
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

# ---------------- Session State ----------------
if "started" not in st.session_state:
    st.session_state.started = False

if "message" not in st.session_state:
    st.session_state.message = []  

userId = st.session_state.user_id

if not st.session_state.started:
    start = ui.landingSection2() # just renders user guide

    # If "Get Started" clicked, update session_state and rerun
    if start:
        st.session_state.started = True
        st.rerun()

else:
    user_input = st.chat_input("Describe your prompt....")  # ← Move this UP

    # Only show welcome if no messages AND no input is being submitted
    if len(st.session_state.message) == 0 and not user_input:
        ui.render_promptlab_home()

    for i in st.session_state.message:
        with st.chat_message(i["role"]):
            st.markdown(i["msg"])

    if user_input:

        st.session_state.message.append({
            "role": "user",
            "msg": user_input
        })

        # SAVING TO DB
        save_user_query(user_id=userId, user_query=user_input)
        
        with st.chat_message(name="user"):
            st.code(user_input)

        with st.chat_message(name="assistant"):
            with st.spinner("Thinking...."):
                ai_response = modelGemini.askGemini(query=user_input)
                st.info(ai_response)

        # SAVING AI RESPONSE TO DB
        save_gemini_response(user_id=userId, ai_respose=ai_response)

        st.session_state.message.append({
            "role": "assistant",
            "msg": ai_response
        })
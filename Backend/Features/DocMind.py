import streamlit as st
import Frontend.F_DocMind as ui
import uuid
import sys
import os
from datetime import datetime
from Backend.Core.Features.RagPipeLine.IngestionPipeLine import INGESTION_PIPELINE_MODEL
from Backend.Core.Features.RagPipeLine.RetrievalPipeLine import RETRIEVAL_PIPELINE_MODEL

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

st.set_page_config(
    page_title="DocMind",
    layout="centered"
)
ui.inject_css()


if "db_ready" not in st.session_state:
    st.session_state.db_ready = False

# ---------- Session variables (TOP) ----------
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())


# ---------------- Session State ----------------
if "started" not in st.session_state:
    st.session_state.started = False

# ---------------- Chat History -----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# USER ID
userId = st.session_state.user_id


# ==================== SUBMIT FUNCTION ==================== #
def submit():

    user_text = st.session_state.user_input

    if user_text:

        # USER MESSAGE
        st.session_state.messages.append({
            "role": "user",
            "msg": user_text
        })

        # RAG PIPELINE
        rp = RETRIEVAL_PIPELINE_MODEL()

        # AI RESPONSE
        ai_res = rp.final_answer(user_text)

        st.session_state.messages.append({
            "role": "assistant",
            "msg": ai_res
        })

        # CLEAR INPUT
        st.session_state.user_input = ""

# ---------------- Landing Page ----------------
if not st.session_state.started:
    start = ui.landing_section1() 

    # If "Get Started" clicked, update session_state and rerun
    if start:
        st.session_state.started = True
        st.rerun()
else:

    pdf_doc = st.sidebar.file_uploader(
    label="Upload pdf",
    type=["pdf"],
    help="Only pdf files are supported"
    )

    if pdf_doc:

        os.makedirs("Assets/pdf", exist_ok=True)
        file_path = os.path.join("Assets/pdf", pdf_doc.name)

        if not os.path.exists(file_path):
            with open(file_path, "wb") as f:
                f.write(pdf_doc.getbuffer())
            st.sidebar.success("PDF uploaded successfully")
        else:
            st.sidebar.success("Start Chat")

    if st.sidebar.button("Confirm") and not st.session_state.db_ready:

        with st.spinner("Indexing documents...."):

            ingest = INGESTION_PIPELINE_MODEL()
            doc = ingest.load_all_docs(file_path="Assets/pdf")
            chunks = ingest.text_to_chunks(doc)
            vector_db = ingest.create_vector_db(chunks)

        st.success("Documents indexed successfully")

    col1, col2 = st.columns(2)

    with col1:

        chat_container = st.container(height=500)

        with chat_container:

            for message in st.session_state.messages:

                with st.chat_message(message["role"]):
                    st.markdown(message["msg"])

        st.text_input(
            label="",
            placeholder="Ask your query",
            key="user_input",
            on_change=submit
        )

    with col2:

        user = st.text_area(
            label="Write bellow",
            height=500,
            placeholder="Lets start making notes..."
        )

        
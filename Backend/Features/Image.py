import streamlit as st
import Frontend.F_Image as ui
import requests
from PIL import Image
from io import BytesIO
import uuid
from DB.mongo_db.image_db import insert_into_user

# ---------- Session variables (TOP) ----------
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

user_id = st.session_state.user_id

st.set_page_config(

    page_title="ImageLab",
    layout="centered"
    )

ui.inject_css()

if "img_started" not in st.session_state:
    st.session_state.img_started = False

if not st.session_state.img_started:
    start = ui.landing_section()
    if start:
        st.session_state.img_started = True
        st.rerun()
else:
    prompt, generate = ui.prompt_section()
    
    if generate:

        if prompt:

            insert_into_user(user_id=user_id, prompt=prompt)

            with st.spinner("Generating image, Please wait..."):
                try:
                    url = f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}"
                    response = requests.get(url)
                    img = Image.open(BytesIO(response.content))
                    
                    # Display image
                    st.image(img, caption=f"Generated: {prompt}", use_container_width=True)
                    
                    # Download button
                    buf = BytesIO()
                    img.save(buf, format="PNG")
                    st.download_button(
                        label="Download Image",
                        data=buf.getvalue(),
                        file_name="generated_image.png",
                        mime="image/png"
                    )
                except Exception as e:
                    st.error(f"Error generating image: {e}")
        else:
            st.warning("Please enter the prompt first !")        
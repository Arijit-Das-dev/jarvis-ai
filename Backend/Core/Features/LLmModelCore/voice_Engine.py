""" CORE ENGINE """
""" 1. speak(), 
    2. Listen_wake_word(), 
    3. take_command()
"""

import edge_tts
import asyncio
import os
import base64
import speech_recognition as sr
import streamlit as st
import uuid
import time as t
import warnings
import pyaudio
import io
from DB.MongoDB.MainDB import insert_into_user


if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

user_id = st.session_state.user_id
warnings.filterwarnings("ignore")

class CoreEngine:

    def __init__(self):
        self.is_speaking = False

    def speak(self, text):

        async def generate_audio():
            communicate = edge_tts.Communicate(
                text=text,
                voice="en-US-GuyNeural",
                rate="+3%",
                pitch="+5Hz"
            )

            audio_bytes = b""
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    audio_bytes += chunk["data"]

            return audio_bytes

        try:
            self.is_speaking = True   # 🔴 LOCK MIC

            audio_bytes = asyncio.run(generate_audio())
            audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

            audio_html = f"""
            <audio autoplay>
                <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
            </audio>
            """

            st.markdown(audio_html, unsafe_allow_html=True)

            # ⏳ WAIT till audio finishes (important!)
            t.sleep(len(text) * 0.06)

        except Exception as e:
            st.error(f"Edge TTS Error: {str(e)}")

        finally:
            self.is_speaking = False   # 🟢 UNLOCK MIC

    # -> ----------- PASSIVE WAKE LISTENING ------------- <-
    def listen_wake_word(self):

        r = sr.Recognizer()

        # Optimized settings for wake word detection
        r.energy_threshold = 300  # Lower = more sensitive
        r.pause_threshold = 0.5   # Shorter pause detection
        r.dynamic_energy_threshold = True  # Auto-adjust to environment
        
        wake_words = ["jarvis", "jarves", "jar vis", "javis"]  # Common mishearings
        
        while True:
            try:
                with sr.Microphone() as source:
                    print("🎧 Listening for wake word...")
                    
                    # Better ambient noise adjustment => [Noise cancelation]
                    r.adjust_for_ambient_noise(source, duration=1)
                    
                    # Shorter phrase limit for wake word
                    audio = r.listen(source, timeout=10, phrase_time_limit=5)

                # Recognize speech
                said = r.recognize_google(audio, language='en-in').lower()
                print(f"Detected: '{said}'")
                st.write(f"Heard: {said}")

                # Check wake word with fuzzy matching
                if any(wake_word in said for wake_word in wake_words):
                    print("🚀 Wake word detected: JARVIS!!!")
                    return True

            except sr.WaitTimeoutError:
                print("⏳ Listening...")
                continue

            except sr.UnknownValueError:
                print("❌ Could not understand — retrying...")
                continue

            except sr.RequestError as e:
                st.error(f"⚠️ Network error: {e}")
                continue

            except Exception as e:
                print(f"⚠️ Error: {e}")
                continue

    # -> ----------- ACTIVE COMMAND LISTENING ------------ <-
    def take_command(self):

        if self.is_speaking:
            return "none"   # 🚫 Ignore input while speaking

        r = sr.Recognizer()
        r.energy_threshold = 200
        r.pause_threshold = 1.0
        r.dynamic_energy_threshold = True

        try:
            with sr.Microphone() as source:
                st.write("🎧 Listening for command...")
                r.adjust_for_ambient_noise(source, duration=1.5)

                audio = r.listen(
                    source,
                    timeout=30,
                    phrase_time_limit=25
                )

            query = r.recognize_google(audio, language='en-in').lower()

            insert_into_user(user_id=user_id, query_user=query)

            st.success(f"✅ You said: {query}")
            return query

        except:
            return "none"
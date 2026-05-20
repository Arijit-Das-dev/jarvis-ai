""" SETTING UP Model : LLaMa"""

import os
import uuid
import streamlit as st
import warnings
import requests
from Backend.Core.Features.LLmModelCore.voiceEngine import CoreEngine
from Backend.Config.settings import settings
from DB.MySQL.weather_db import insert_weather
from DB.MongoDB.MainDB import insert_into_assistant
from groq import Groq


if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

user_id = st.session_state.user_id
warnings.filterwarnings("ignore")

""" SETTING UP JARVIS VIA LLAMA MODEL """ # TEMPLETE
class Jarvis(CoreEngine):

    def __init__(self):

        API_KEY = settings.GROQ_API_KEY
        self.client = Groq(api_key=API_KEY)
        self.chat_history = [] # Chat history

    def ask_llama(self, prompt):

        self.chat_history.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=self.chat_history  # send full chat history
        )

        bot_reply = response.choices[0].message.content

        # Store assistant reply too
        self.chat_history.append({

            "role": "assistant", 
            "content": bot_reply
        })

        return bot_reply

    def JarvisRun(self, user2):


            if "weather" in user2:

                latitude = 22.57
                longitude = 88.36

                url = (
                    f"https://api.open-meteo.com/v1/forecast?"
                    f"latitude={latitude}&longitude={longitude}"
                    f"&current_weather=true"
                    f"&hourly=relativehumidity_2m,pressure_msl,cloudcover"
                )

                try:
                    response = requests.get(url)
                    data = response.json()

                    # Current weather
                    temperature = data['current_weather']['temperature']
                    windspeed = data['current_weather']['windspeed']
                    winddirection = data['current_weather']['winddirection']
                    weather_code = data['current_weather']['weathercode']

                    # Hourly extra parameters (take index 0 = current hour)
                    humidity = data['hourly']['relativehumidity_2m'][0]
                    pressure = data['hourly']['pressure_msl'][0]
                    cloud_cover = data['hourly']['cloudcover'][0]
                    insert_weather(temperature, windspeed, winddirection, weather_code, humidity, pressure, cloud_cover)

                except Exception as e:

                    print(f"Error : {e}")
                    j.speak(f"{e}")
                
                j.speak(f"Today's temperature is {temperature} degree celsius ")
                j.speak(f"windspeed is {windspeed} kilometre per hour")

            elif "exit" in user2:

                self.speak('''Okay sir, i am going to sleep now, if you need anything, just wake me up by saying "hey jarvis" ''')
                return "exit"
            else:
                try:
                    root_dir = os.path.abspath(
                        os.path.join(os.path.dirname(__file__), "..", "..")
                    )
                    prompt_path = os.path.join(root_dir, "Prompt", "mainPrompt.txt")

                    with open(prompt_path, "r", encoding="utf-8") as f:
                        system_prompt = f.read()

                    final_prompt = f"{system_prompt}\nUser: {user2}\nAssistant:"
                    
                    reply = self.ask_llama(final_prompt)
                    print("Assistant:", reply)
                    self.speak(reply)
                    insert_into_assistant(user_id=user_id, ai_answer=reply)

                except Exception as e:

                    print("LLM Error:", e)
                    self.speak("I did not hear that properly, tell that again")

j = Jarvis()
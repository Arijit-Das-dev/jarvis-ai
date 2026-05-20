""" Greet function """
import requests
from datetime import datetime
import time as t
from Backend.Services.llama_client import Jarvis

j = Jarvis()

def greet():

    latitude = 22.57
    longitude = 88.36

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    try:
       
       response = requests.get(url)
       data = response.json()

       temperature = data['current_weather']['temperature']
       windspeed = data['current_weather']['windspeed']

    except Exception as e:

        print(f"Error : {e}")
        j.speak(f"{e}")

    # TIME CONFIGURATION
    hour = datetime.now().hour

    if 5 <= hour < 12:
        j.speak("Good morning sir. Welcome to a brand-new day.")
        t.sleep(1.2)
    elif 12 <= hour < 17:
        j.speak("Good afternoon sir. I hope your day is going smoothly.")
        t.sleep(1.2)
    elif 17 <= hour < 21:
        j.speak("Good evening sir, welcome back.")
        t.sleep(1.2)
    else:
        j.speak("Welcome back sir!")
        t.sleep(1.2)

    j.speak(f"Today's temperature is {temperature} degree celsius ")
    t.sleep(1.5)
    j.speak(f"windspeed is {windspeed} kilometre per hour")
    t.sleep(1.3)

    j.speak("Tell me how can I assist you?")
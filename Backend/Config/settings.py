# Storing API keys , database urls, hosts, passwords

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    # LLMs (LLaMa, Mistral)
    GROQ_API_KEY = os.getenv("GROQ_API_KEY") # LLaMa
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY") # MISTRAL
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") # GEMINI
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    GPT_API_KEY = os.getenv("GPT_API_KEY")
    
    # DATABASE (MYSQL, MONGODB)
    MONGO_DB_URL = os.getenv("MONGODB_URL") # MongoDB
    MY_SQL_HOST = os.getenv("MYSQL_HOST")
    MY_SQL_USER = os.getenv("MYSQL_USER")
    MY_SQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MY_SQL_JARVIS_WAKE = os.getenv("MYSQL_JARVIS_WAKE")
    MYSQL_JARVIS_WEATHER = os.getenv("MYSQL_JARVIS_WEATHER")

settings = Settings()
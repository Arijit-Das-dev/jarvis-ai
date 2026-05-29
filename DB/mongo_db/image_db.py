"""
Docstring for 3 Third Project.ImageDB

Stores users prompt

"""

from pymongo import MongoClient
from datetime import datetime
from Backend.Config.settings import settings


def connect_db():

    client = MongoClient(settings.MONGO_DB_URL)

    db = client["Jarvis_lab_db"]

    user_prompt = db["User_Prompt"]

    return user_prompt

def insert_into_user(user_id, prompt):

    user_prompt = connect_db()

    document = {

        "user_id":user_id,
        "user_prompt":prompt,
        "date":datetime.now()

    }

    user_prompt.insert_one(document)
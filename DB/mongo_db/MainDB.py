"""
Docstring for 3 Third Project.MainDB

Storing user queries and assistant queries to MongoDB
"""
from pymongo import MongoClient
from datetime import datetime
from Backend.Config.settings import settings

def connect_db():

    client = MongoClient(settings.MONGO_DB_URL)

    db = client["Jarvis_main_db"]

    user_query = db["User_Query"]

    assistant_answer = db["Assistant_Answer"]

    return user_query, assistant_answer

def insert_into_user(user_id, query_user):

    user_query, _ = connect_db()

    document = {

        "user_id":user_id,
        "query_user":query_user,
        "date":datetime.now()

    }

    user_query.insert_one(document)

def insert_into_assistant(user_id, ai_answer):

    _, assistant_query = connect_db()

    document = {

        "user_id":user_id,
        "ai_answer":ai_answer,
        "date":datetime.now()

    }

    assistant_query.insert_one(document)
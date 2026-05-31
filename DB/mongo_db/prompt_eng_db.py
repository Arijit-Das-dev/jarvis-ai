"""
Using MongoDB for storing user codes and user queries

"""

from pymongo import MongoClient
from datetime import datetime
from Backend.Config.settings import settings 
from Backend.Utils.mongo_doc_builder import MongoDocumentBuilder

mongo = MongoDocumentBuilder()

def connect_db():

    """
    Connect to MongoDB and return collections
    """

    # Build connection with MongoDB Compass
    client = MongoClient(settings.MONGO_DB_URL)

    # Created database in MongoDB Compass
    db = client["Jarvis_Prompt_Editor_DB"]

    # Select colections

    """ Collection 1"""
    code_collection = db["Prompt_editor"] # Stores user code

    """ Collection 2"""
    co_pilot_collection = db["gemini_response"] # Stores user query

    return code_collection, co_pilot_collection

def save_user_query(user_id, user_query):

    """
    Docstring for save_user_code
    
    :param user_id: Description
    :param user_query: Description

    save user id and user code 
    """

    code_collection, _ = connect_db()

    document = mongo.prompt_db_user_document(
        user_id=user_id,
        user_query=user_query,
        date=datetime.now()
    )

    code_collection.insert_one(document)

def save_gemini_response(user_id, ai_respose):

    """
    Docstring for save_user_query
    
    :param user_id: Description
    :param user_query: Description

    save co-pilot user id and user query
    """

    _, co_pilot_collection = connect_db()

    document = mongo.prompt_db_assistant_document(
        user_id=user_id,
        ai_response=ai_respose,
        date=datetime.now()
    )

    co_pilot_collection.insert_one(document)
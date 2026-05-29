"""
Using MongoDB for storing user codes and user queries

"""

from pymongo import MongoClient
from datetime import datetime
from Backend.Config.settings import settings 

def connect_db():

    """
    Connect to MongoDB and return collections
    """

    # Build connection with MongoDB Compass
    client = MongoClient(settings.MONGO_DB_URL)

    # Created database in MongoDB Compass
    db = client["Jarvis_Code_Db"]

    # Select colections

    """ Collection 1"""
    code_collection = db["code_editor"] # Stores user code

    """ Collection 2"""
    co_pilot_collection = db["co_pilot"] # Stores user query

    return code_collection, co_pilot_collection

def save_user_code(user_id, user_code):

    """
    Docstring for save_user_code
    
    :param user_id: Description
    :param user_query: Description

    save user id and user code 
    """

    code_collection, _ = connect_db()

    document = {

        "user_id":user_id,
        "user_code":user_code,
        "date":datetime.now()

    }

    code_collection.insert_one(document)

def save_user_query(user_id, user_query):

    """
    Docstring for save_user_query
    
    :param user_id: Description
    :param user_query: Description

    save co-pilot user id and user query
    """

    _, co_pilot_collection = connect_db()

    document = {

        "user_id":user_id,
        "user_query":user_query,
        "date":datetime.now()

    }

    co_pilot_collection.insert_one(document)
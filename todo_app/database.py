import os
import certifi
import pymongo
import data
from pymongo import MongoClient

dbpassword = os.environ['dbpassword']

CONNECTION = f'mongodb+srv://marklawrence:{dbpassword}@cluster0.ukgck.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true'
MONGODB = "todo_list"
MONGOCOLLECTION = "todo_items"

def mongodb_connection():
    mongo_client = MongoClient(CONNECTION, tlsCAfile=certifi.where())
    dbname = mongo_client[MONGODB]
    return dbname
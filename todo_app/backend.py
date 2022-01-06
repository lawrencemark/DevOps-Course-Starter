import database
import random
import time


itemList = []

def mongodb_getcollections():
    itemList.clear()
    dbname = database.mongodb_connection()
    item_col = dbname[database.MONGOCOLLECTION]
    for i in item_col.find():
        itemList.append(i)

def mongodb_addcollection(taskName,taskDesc,taskStatus):
    item_Number = f'ItemNo_{random.randrange(1,1000000)}'
    item_Name = taskName
    item_Description = taskDesc
    Status = taskStatus
    
    if (len(item_Number) > 0) and (len(item_Name) > 0) and (len(taskStatus) > 0):
         
        item_collection = {
            "Item_number": item_Number,
            "Item_name": item_Name,
            "Item_description": item_Description,
            "Status": Status
        } 
         
        dbname = database.mongodb_connection()
        item_col = dbname[database.MONGOCOLLECTION]
        item_col.insert_one(item_collection)

def mongodb_delcollection(item_Number):
    query = { "Item_number": item_Number}
    dbname = database.mongodb_connection()
    item_col = dbname[database.MONGOCOLLECTION]
    item_col.delete_one(query)

def mongodb_updatecollection(item_Number, status):
    query = { "Item_number": item_Number}
    replaceStatus = { "$set": {"Status": status } }
    dbname = database.mongodb_connection()
    item_col = dbname[database.MONGOCOLLECTION]
    item_col.update_one(query, replaceStatus)


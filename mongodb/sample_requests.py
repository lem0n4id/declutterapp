from bson.objectid import ObjectId
from mongodb_base import get_database, generate_objectid
db = get_database()

def get_count(collection_name: str):
    return db[collection_name].count_documents({})

def get_user_id_from_email(email:str):
    from pandas import DataFrame
    collection_users = db["users"]
    data=collection_users.find({"email":email})
    df=DataFrame(data)
    return df.iloc[0]["user_id"]

def add_entry_in_users(user: dict)->None:
    """
    {
     user_id:ObjectId(f"user{count}"),
     name:"John Doe",
     email:"john1234@gmail.com", 
     pending_entry_ids: ["ObjectID('60c01917706af33ed8db96')"],
     finished_entry_ids:[]
    }
    """
    collection_users = db["users"]
    collection_users.insert_one(user)
    return

def modify_entry_array_user(userid:str, field: str, status_entry_id: str):
    """
    userid = pending_entry_ids or finished_entry_ids
    refer: https://docs.mongodb.com/manual/reference/operator/update/#array
    """
    collection_users = db["users"]
    collection_users.update_one({'user_id': userid}, {'$addToSet': {field: status_entry_id}})
    return

def add_entry_in_entries(entry: dict):
    """
    {
     entry_id:"ObjectID('60c01917706af33ed8db96')",
     name:"Why web3 matters", 
     url:"https://blog.mcgee.cat/why-web3-matters",
     importance:"",
     created_date:"2021-10-15T18:28:23.382748", 
     remind_on:"2021-10-16T18:28:23.382748",
     read_status:false,
     tags:["Tech","Web3"],
     host:ObjectId(“user1”)
    }
    """
    collection_entries = db["entries"]
    collection_entries.insert_one(entry)
    return

def add_entry_in_interests(entry: dict):
    """
    {
    entry_id:"ObjectID(6798922vxvjhs882)",
    category:"Tech", 
    weight:["casual":0, 
            "moderate":1,
            "important":0]
    host:ObjectId(“user1”)
    }
    """
    collection_entries = db["interests"]
    collection_entries.insert_one(entry)
    return

def query_users(userid: ObjectId):
    collection_users = db["users"]
    item_details=collection_users.find({"user_id":userid})
    return item_details

def query_entries(host: ObjectId):
    collection_entries = db["entries"]
    item_details=collection_entries.find({"host":host})
    return item_details

def query_interests(host: ObjectId):
    collection_interests = db["interests"]
    item_details=collection_interests.find({"host":host})
    return item_details

if __name__ == "__main__":
    pass
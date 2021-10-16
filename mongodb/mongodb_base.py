def get_database():
    from mongodb.creds import USERNAME, PASSWORD

    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo

    CONNECTION_STRING = "mongodb+srv://%s:%s@declutter-v1.ws6rm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"%(USERNAME, PASSWORD)
    # Create a connection using MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)
    
    # Create the database 
    return client['data']

def generate_objectid(id: str = ''):
    from bson.objectid import ObjectId
    if id:
        return ObjectId(id)
    return ObjectId()


    

if __name__ == "__main__":    
    
    # Get the database
    db = get_database()
    collection_users = db["users"]
    obj1=generate_objectid()
    user1={
        "user_id":obj1,
        "name":"John Doe",
        "email":"john1234@gmail.com", 
        "pending_entry_ids": [],
        "finished_entry_ids":[]
    }
    collection_users.insert_one(user1)
    a=collection_users.find({"name":"John Doe"})
    for i in a:
        print(i)

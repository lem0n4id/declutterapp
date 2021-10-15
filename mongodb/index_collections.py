from mongodb_base import get_database
db=get_database()

def user_index():
    collection_users = db["users"]
    category_index = collection_users.create_index("category")
def entries_index():
    collection_users = db["entries"]
    category_index = collection_users.create_index("host")
def interests_index():
    collection_users = db["interests"]
    category_index = collection_users.create_index("host")

user_index()
entries_index()
interests_index()
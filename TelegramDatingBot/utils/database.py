import pymongo

def connect_to_database():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['dating_bot']
    return db

def get_user(user_id):
    db = connect_to_database()
    users_collection = db['users']
    user = users_collection.find_one({'user_id': user_id})
    if user is None:
        return None
    return User(user['user_id'], user['name'], user['age'], user['interests'])

def create_user(user_id, name, age, interests):
    db = connect_to_database()
    users_collection = db['users']
    users_collection.insert_one({'user_id': user_id, 'name': name, 'age': age, 'interests': interests})

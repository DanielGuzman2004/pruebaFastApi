from models.model import Bank,  UpdateBankModel
from config.config import blogsCollection
from serializer.serializar import converBlogsList
from bson import ObjectId

def home():
    return {
        "status": "ok",
        "message": "Welcome to FastApi with python"
    }



def new_user(user: Bank):
    blogsCollection.insert_one(user.model_dump())
    return {
        "status": "OK",
        "message": "User Registered Successfully"
    }



def get_users():
    users = blogsCollection.find()
    users_list = converBlogsList(users)
    return {
        "status": "OK",
        "message": "Existing users in DB",
        "data": users_list
    }



def update_user(id: str, user: Bank):
    blogsCollection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(user)}
    )
    return {
        "status": "OK",
        "message": "User Modified Successfully"
    }



def update_user_balance(id: str, user: UpdateBankModel):
    blogsCollection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": {"balance": user.balance}}
    )
    return {
        "status": "OK",
        "message": "User balance modified successfully"
    }



def delete_user(id: str):
    blogsCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {
        "status": "OK",
        "message": "Users successfully deleted from DB",
    }
from models.model import Bank,  UpdateBankModel, ResponseModel
from config.config import blogsCollection
from serializer.serializar import converBlogsList
from bson import ObjectId

def home():
    return ResponseModel(
        status="ok",
        message="Welcome to FastApi with python"
    )

def new_user(user: Bank):
    inserted_user = blogsCollection.insert_one(user.model_dump())
    user_id = str(inserted_user.inserted_id)  # Convertir ObjectId a string
    return ResponseModel(
        status="OK",
        message="User Registered Successfully",
        data={"user_id": user_id}
    )

def get_users():
    users = blogsCollection.find()
    users_list = converBlogsList(users)
    return ResponseModel(
        status="OK",
        message="Existing users in DB",
        data=users_list
    )

def update_user(id: str, user: Bank):
    blogsCollection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(user)}
    )
    return ResponseModel(
        status="OK",
        message="User Modified Successfully"
    )

def update_user_balance(id: str, user: UpdateBankModel):
    blogsCollection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": {"balance": user.balance}}
    )
    return ResponseModel(
        status="OK",
        message="User balance modified successfully"
    )

def delete_user(id: str):
    blogsCollection.find_one_and_delete({"_id": ObjectId(id)})
    return ResponseModel(
        status="OK",
        message="Users successfully deleted from DB"
    )
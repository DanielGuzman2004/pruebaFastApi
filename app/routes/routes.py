from fastapi import APIRouter
from controllers.controllers import home, new_user, get_users, update_user, update_user_balance, delete_user
from models.model import Bank, UpdateBankModel, ResponseModel

endPoints = APIRouter()

@endPoints.get("/", response_model=ResponseModel)
def home_route():
    return home()

@endPoints.post("/new/user", response_model=ResponseModel)
def new_user_route(user: Bank):
    return new_user(user)

@endPoints.get("/users", response_model=ResponseModel)
def get_users_route():
    return get_users()

@endPoints.put("/update/{id}", response_model=ResponseModel)
def update_user_route(id: str, user: Bank):
    return update_user(id, user)

@endPoints.patch("/edit/balance/{id}", response_model=ResponseModel)
def update_user_balance_route(id: str, user: UpdateBankModel):
    return update_user_balance(id, user)

@endPoints.delete("/delete/{id}", response_model=ResponseModel)
def delete_user_route(id: str):
    return delete_user(id)
from fastapi import APIRouter
from controllers.controllers import home, new_user, get_users, update_user, update_user_balance, delete_user

endPoints = APIRouter()

endPoints.get("/")(home)
endPoints.post('/new/user')(new_user)
endPoints.get('/users')(get_users)
endPoints.put('/update/{id}')(update_user)
endPoints.patch('/edit/balance/{id}')(update_user_balance)
endPoints.delete('/delete/{id}')(delete_user)
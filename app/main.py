from fastapi import FastAPI
from routes.routes import endPoints

usuario = FastAPI() 
usuario.include_router(endPoints)
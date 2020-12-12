from fastapi import FastAPI
from datetime import datetime
from entities.Users import *
from service.Storage import *
from service.Loader import *

app = FastAPI()

print("Started!")


@app.get("/ping")
async def pong():
    return {
        "pong": datetime.now().time()
    }


@app.get("/users")
async def loadUsers():
    return {
        "users": LoadUsers()
    }

print("Stoped")

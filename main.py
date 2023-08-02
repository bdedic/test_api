from fastapi import FastAPI, HTTPException
from models import User, Role
from typing import List
from uuid import UUID, uuid4

app = FastAPI()

db: List[User] = [
  User(id = uuid4(),first_name = "Bojan", last_name = "Dedic", roles = [Role.admin]),
  User(id = uuid4(),first_name = "Test", last_name = "User", roles = [Role.user])
]

@app.get("/azure-test-api")
async def root():
  return {"Azure API test"}

@app.get("/api/v1/users")
async def get_users():
  return db

@app.post("/api/v1/users")
async def register_user(user: User):
  db.append(user)
  return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
  for user in db:
    if user.id == user_id:
      db.remove(user)
      return
  raise HTTPException(status_code = 404, detail = f"User with id: {user_id} does not exist")
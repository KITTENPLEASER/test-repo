from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class User(BaseModel):
    name: str
    age: int


@app.get("/")
def root():
    return {"message":"Hello, world!"}

@app.get("/hello/{name}")
def test(name: str):
    return {"message":f"hello,{name}"}

@app.post("/users")
def create_user(user: User):
    return {"message": f"Создан пользователь {user.name}. Возраст {user.age}"}
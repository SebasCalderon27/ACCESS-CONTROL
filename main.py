from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Logueo(BaseModel):
    email: str
    password: str

User_db = {
    "email": "sebas.calderon@gmail.com",
    "password": "Admin123"
}


@app.post("/login")
def login(user: Logueo):
    if user.email == User_db["email"] and user.password == User_db["password"]:
        return {"message": "Login exitoso"}
    else:
        return {"message": "Credenciales inválidas"}

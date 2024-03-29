from fastapi import FastAPI
import jwt

flag = 'kxctf{flag}'
secret = flag[:6]

app = FastAPI()

@app.get("/")
async def root():
    return 'У меня есть две ручки (смотри в исходный код)'   

@app.get("/gen-jwt/{name}")
async def create_session(name: str):
    return {
        "jwt": jwt.encode({"name": name, "isAdmin": False}, secret, algorithm="HS256")
    }


@app.get("/check-jwt/{jwt_token}")
async def check_jwt(jwt_token: str):
    try:
        json = jwt.decode(jwt_token, secret, algorithms=["HS256"])
    except Exception as e:
        return {"err": str(e)}

    if "isAdmin" in json and json.get("isAdmin"):
        return {"msg": f"Привет, админ! Держи флаг: {flag}"}
    elif "name" in json:
        return {"msg": f"Привет, {json['name']}!"}

    return {"msg": "Что-то пошло не так =("}
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.models import UserCreate, UserLogin, UserResponses
from app.utils import hash_password, verify_password, create_access_token
from datetime import timedelta
from jose import jwt
import environ


env = environ.Env()


app = FastAPI()


fake_users_db = {}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/register/")
async def register(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_password = hash_password(user.password)
    fake_users_db[user.username] = {
        "username": user.username,
        "password": hashed_password,
    }
    return {"msg": "User created successfully!"}


@app.post("/token/", response_model=UserResponses)
async def login(user: UserLogin):
    stored_user = fake_users_db.get(user.username)
    if not stored_user:
        raise HTTPException(status_code=401, detail="User not found")

    if not verify_password(user.password, stored_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid password")

    access_token = create_access_token(data={"sub": user.username})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username,
    }


@app.get("/users")
def get_user():
    return fake_users_db


@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    try:

        payload = jwt.decode(
            token,
            '8bfa4b980c749cbc48d0cef2f459ea6d795029bf8dd3da82868bf9c820f89d71',
            algorithms=["HS256"],
        )
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

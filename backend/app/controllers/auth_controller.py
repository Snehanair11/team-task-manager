from app.config.db import db
from app.models.user import User
from fastapi import HTTPException
from passlib.context import CryptContext
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET = os.getenv("JWT_SECRET")

if not SECRET:
    raise RuntimeError("JWT_SECRET missing in .env")


# 🔥 FIX: truncate password to avoid bcrypt 72-byte crash
def hash_password(password: str):
    return pwd_context.hash(password[:72])


def verify_password(plain, hashed):
    return pwd_context.verify(plain[:72], hashed)


async def signup(user: User):
    try:
        existing = await db.users.find_one({"email": user.email})
        if existing:
            raise HTTPException(status_code=400, detail="User already exists")

        user_dict = user.dict()
        user_dict["password"] = hash_password(user.password)

        result = await db.users.insert_one(user_dict)

        user_dict["_id"] = str(result.inserted_id)
        user_dict.pop("password")

        return user_dict

    except Exception as e:
        print("SIGNUP ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))


async def login(data: dict):
    try:
        user = await db.users.find_one({"email": data["email"]})

        if not user:
            raise HTTPException(status_code=400, detail="Invalid credentials")

        if not verify_password(data["password"], user["password"]):
            raise HTTPException(status_code=400, detail="Invalid credentials")

        token = jwt.encode(
            {"id": str(user["_id"]), "role": user["role"]},
            SECRET,
            algorithm="HS256"
        )

        user["_id"] = str(user["_id"])
        user.pop("password")

        return {
            "token": token,
            "user": user
        }

    except Exception as e:
        print("LOGIN ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))
    
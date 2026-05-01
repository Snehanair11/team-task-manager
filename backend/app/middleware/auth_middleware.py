from fastapi import Request, HTTPException
from jose import jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("JWT_SECRET")

async def get_current_user(request: Request):
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise HTTPException(status_code=401, detail="No token provided")

    try:
        token = auth_header.split(" ")[1]
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
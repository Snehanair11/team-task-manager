from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class User(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    password: str = Field(..., min_length=6)
    role: str = "member"


# 🔹 Optional: for login requests (cleaner than using dict)
class LoginModel(BaseModel):
    email: EmailStr
    password: str

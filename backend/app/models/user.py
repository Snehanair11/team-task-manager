from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "member"


class LoginModel(BaseModel):
    email: EmailStr
    password: str

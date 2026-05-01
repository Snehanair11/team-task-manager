from fastapi import APIRouter
from app.models.user import User
from app.controllers.auth_controller import signup, login

router = APIRouter()

@router.post("/signup")
async def signup_route(user: User):
    return await signup(user)

@router.post("/login")
async def login_route(data: dict):
    return await login(data)
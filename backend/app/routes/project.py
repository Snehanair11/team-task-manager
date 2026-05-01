from fastapi import APIRouter, Depends
from app.controllers.project_controller import create_project, get_projects
from app.middleware.auth_middleware import get_current_user

router = APIRouter()

@router.post("/")
async def create(data: dict, user=Depends(get_current_user)):
    return await create_project(data, user)


@router.get("/")
async def get(user=Depends(get_current_user)):
    return await get_projects(user)
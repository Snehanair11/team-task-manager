from fastapi import APIRouter, Depends
from app.controllers.task_controller import create_task, get_tasks, update_task
from app.middleware.auth_middleware import get_current_user

router = APIRouter()

@router.post("/")
async def create(data: dict, user=Depends(get_current_user)):
    return await create_task(data, user)


@router.get("/")
async def get(user=Depends(get_current_user)):
    return await get_tasks(user)


@router.put("/{task_id}")
async def update(task_id: str, data: dict, user=Depends(get_current_user)):
    return await update_task(task_id, data, user)
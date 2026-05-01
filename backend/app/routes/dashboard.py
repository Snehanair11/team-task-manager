from fastapi import APIRouter, Depends
from app.middleware.auth_middleware import get_current_user

router = APIRouter()

@router.get("/")
async def dashboard(user=Depends(get_current_user)):
    return {
        "total_tasks": 0,
        "completed_tasks": 0,
        "pending_tasks": 0,
        "overdue_tasks": 0
    }
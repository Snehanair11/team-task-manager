from app.config.db import db
from fastapi import HTTPException

async def create_task(data: dict, user):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can assign tasks")

    task = {
        "title": data["title"],
        "description": data["description"],
        "project_id": data["project_id"],
        "assigned_to": data["assigned_to"],
        "status": "todo",
        "due_date": data.get("due_date")
    }

    result = await db.tasks.insert_one(task)
    task["_id"] = str(result.inserted_id)

    return task


async def get_tasks(user):
    tasks = []

    async for t in db.tasks.find():
        t["_id"] = str(t["_id"])
        tasks.append(t)

    return tasks


async def update_task(task_id: str, data: dict, user):
    task = await db.tasks.find_one({"_id": task_id})

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Only assigned user OR admin can update
    if user["role"] != "admin" and task["assigned_to"] != user["id"]:
        raise HTTPException(status_code=403, detail="Not allowed")

    await db.tasks.update_one(
        {"_id": task_id},
        {"$set": {"status": data["status"]}}
    )

    return {"message": "Task updated"}
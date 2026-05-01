from app.config.db import db
from fastapi import HTTPException

async def create_project(data: dict, user):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can create project")

    project = {
        "title": data["title"],
        "description": data["description"],
        "created_by": user["id"],
        "team_members": data.get("team_members", [])
    }

    result = await db.projects.insert_one(project)
    project["_id"] = str(result.inserted_id)

    return project


async def get_projects(user):
    projects = []

    async for p in db.projects.find():
        p["_id"] = str(p["_id"])
        projects.append(p)

    return projects
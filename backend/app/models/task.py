from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    title: str
    description: str
    project_id: str
    assigned_to: str
    status: Optional[str] = "todo"
    due_date: Optional[str] = None
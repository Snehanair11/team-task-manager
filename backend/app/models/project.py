from pydantic import BaseModel
from typing import List

class Project(BaseModel):
    title: str
    description: str
    created_by: str
    team_members: List[str] = []
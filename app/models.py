from pydantic import BaseModel


class Task(BaseModel):
    task_id: int
    task_name: str
    is_completed: bool

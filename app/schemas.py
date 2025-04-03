from pydantic import BaseModel

class TaskBase(BaseModel):
    task_name: str
    is_completed: bool

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int

    class Config:
        orm_mode = True

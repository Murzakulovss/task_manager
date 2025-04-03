from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, models, schemas
from app.crud import create_task, get_tasks
from app.schemas import TaskCreate, TaskResponse
from typing import List

router = APIRouter()

@router.get("/tasks/", response_model=List[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db=db)

@router.post("/tasks/", response_model=TaskResponse)
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db=db, task_name=task.task_name)

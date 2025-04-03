from sqlalchemy.orm import Session
from app.models import Task

def get_tasks(db: Session):
    return db.query(Task).all()

def create_task(db: Session, task_name: str):
    db_task = Task(task_name=task_name)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task



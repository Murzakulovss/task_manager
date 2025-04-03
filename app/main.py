from fastapi import FastAPI
from models import Task
from typing import List
app = FastAPI()

tasks = []

@app.get("/tasks", response_model=List[Task])
async def read_tasks():
    return tasks

@app.post("/tasks", response_model= Task)
async def create_task(task: Task):
    tasks.append(task)
    return Task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    tasks[task_id] = Task
    return Task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    del tasks[task_id]
    return {"message:" "Task deleted"}

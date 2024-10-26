from typing import Union, List
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Task(BaseModel):
    id: int
    name: str
    description: Union[str, None] = None

class TaskCreate(BaseModel):
    name: str
    description: Union[str, None] = None

tasks = []

@app.post("/tasks")
async def create_task(task: TaskCreate):
    new_task = Task(id=len(tasks) + 1, name=task.name, description=task.description)
    tasks.append(new_task)
    return {"ok": True, "task": new_task}

@app.get("/tasks")
async def get_tasks():
    return {"data": tasks}

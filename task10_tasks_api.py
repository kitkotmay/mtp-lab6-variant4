from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Task API")


class Task(BaseModel):
    title: str
    completed: bool = False


tasks = {}
next_id = 1


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Задача не найдена",
        )

    return tasks[task_id]


@app.post("/tasks")
def create_task(task: Task):
    global next_id

    task_data = {
        "id": next_id,
        **task.model_dump(),
    }

    tasks[next_id] = task_data
    next_id += 1

    return task_data


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Задача не найдена",
        )

    task_data = {
        "id": task_id,
        **task.model_dump(),
    }

    tasks[task_id] = task_data

    return task_data


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Задача не найдена",
        )

    deleted_task = tasks.pop(task_id)

    return {
        "message": "Задача удалена",
        "task": deleted_task,
    }

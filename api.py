from fastapi import FastAPI
from app import ToDoList

app = FastAPI()
todo = ToDoList()

@app.get("/tasks")
def get_tasks():
    return [task.to_dict() for task in todo.list_tasks()]

@app.post("/tasks")
def add_task(description: str):
    todo.add_task(description)
    return {"message": "Task added"}

@app.patch("/tasks/{task_id}")
def complete_task(task_id: int):
    task = todo.complete_task(task_id)
    if task:
        return {"message": f"Completed task {task_id}"}
    return {"error": "Invalid task id"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    removed = todo.delete_task(task_id)
    if removed:
        return {"message": f"Deleted task {task_id}"}
    return {"error": "Invalid task id"}

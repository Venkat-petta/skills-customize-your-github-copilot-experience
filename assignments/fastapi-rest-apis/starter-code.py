from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


tasks = [
    {"id": 1, "title": "Learn FastAPI", "description": "Build an API from scratch", "completed": False}
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API!"}


# TODO: Add endpoints to list, create, get by id, update, and delete tasks.
# Example:
# @app.get("/tasks")
# def get_tasks():
#     return tasks


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

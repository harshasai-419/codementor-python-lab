from fastapi import FastAPI
from app.database import init_db
from app.routes.tasks import router as task_router

app = FastAPI(
    title="CodeMentor Python Lab",
    description="Task Management API for AI code analysis",
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    init_db()


app.include_router(task_router)


@app.get("/")
def home():
    return {
        "message": "CodeMentor Python Lab API",
        "status": "running"
    }
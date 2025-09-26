import uvicorn

from sqlmodel import select
from fastapi import APIRouter, FastAPI, HTTPException, status, Query
from app.models import Task, TaskCreate
from app.db import SessionDep

router = APIRouter()


@router.post("/tasks", response_model = Task, tags = ['tasks'])
async def taskCreate(task_data : TaskCreate, session: SessionDep):
    task = Task.model_validate(task_data.model_dump())
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.get("/tasks", response_model = list[Task], tags = ['tasks']) 
async def task_list(session: SessionDep):
    statament = select(Task)
    result = session.exec(statament)
    tasks = result.all()
    return tasks

@router.get("/tasks/{id_task}", response_model = Task, tags=['tasks'])
async def task_id(id_task : int, session : SessionDep):
    statament = select(Task).where(Task.id == id_task)
    task = session.exec(statament).one()
    return task




import uvicorn

from sqlmodel import select, update
from fastapi import APIRouter, FastAPI, HTTPException, status, Query
from app.models import Task, TaskCreate, TaskUpdate
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

@router.delete("/tasks/{id_task}", tags = ['tasks'])
async def task_delete(id_task : int, session : SessionDep):
    task_db = session.get(Task, id_task)
    if not task_db:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = "Task doesn't exist"
        )

    session.delete(task_db)
    session.commit()
    return {'message': 'Task deleted successfully', 'deleted_task': task_db.dict()}


@router.patch("/tasks/{id_task}", tags = ['tasks'])
async def task_put(id_task : int, data : TaskUpdate, session : SessionDep):
    task_db = session.get(Task, id_task)
    if not task_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Task doesn't exist"
        )
    
    update_data = data.dict(exclude_unset=True)

    if update_data:
        statement = update(Task).where(Task.id == id_task).values(**update_data)
    
        session.exec(statement)
        session.commit()
        task_db = session.get(Task, id_task)


    return task_db
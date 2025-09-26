import uvicorn

from sqlmodel import select
from fastapi import APIRouter, FastAPI, HTTPException, status, Query
from models import Task
from db import SessionDep, create_all_tables


router = APIRouter()

@router.get("/tasks", response_model = Task, tags = ['tasks'])
async def task():
    return {"messege" : "Prueba"}



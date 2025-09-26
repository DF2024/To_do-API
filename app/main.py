import uvicorn

from fastapi import FastAPI, Request
from sqlmodel import select
from app.routers import todo
from app.db import SessionDep, create_all_tables


app = FastAPI(
    lifespan = create_all_tables
)

app.include_router(todo.router)
import uvicorn

from fastapi import FastAPI, Request
from db import SessionDep, create_all_tables
from sqlmodel import select
from routers import todo


app = FastAPI(
    lifespan = create_all_tables
)

app.include_router(todo.router)
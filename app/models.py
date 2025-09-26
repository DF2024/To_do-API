from pydantic import BaseModel, field_validator
from datetime import date
from sqlmodel import SQLModel, Field, Relationship, Session
from typing import Optional


# id
# title (titulo de la tarea)
# description (opcional)
# status (pendiente, en proceso, completada)
# create_at (fecha de creación)


class Task(SQLModel, table = True):
    id : int | None = Field(primary_key=True)
    title : str = Field(default = None)
    description : str = Field(default = None)
    status : str = Field(default = None)
    create_at : date = Field(default = None)



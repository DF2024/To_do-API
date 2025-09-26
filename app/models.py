from pydantic import BaseModel, field_validator
from datetime import date
from sqlmodel import SQLModel, Field, Relationship, Session
from typing import Optional
from enum import Enum

# id
# title (titulo de la tarea)
# description (opcional)
# status (pendiente, en proceso, completada)
# create_at (fecha de creación)

##  STATUS

class StatusEnum(str, Enum):   
    COMPLETADO = "completado"
    PROCESO = "proceso"
    INCOMPLETADO = "incompletado"

## TASK

class TaskBase(SQLModel):
    title : str = Field(default = None)
    description : str = Field(default = None)
    status : StatusEnum = Field(default=StatusEnum.INCOMPLETADO)
    create_at : date = Field(default = None)

class TaskCreate(TaskBase):
    pass

class Task(TaskBase, table = True):
    id : int | None = Field(default = None, primary_key=True)

class TaskUpdate(TaskBase):
    pass

 

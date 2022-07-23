from ctypes import addressof
from dataclasses import dataclass
from lib2to3.pytree import type_repr
from fastapi import Body, FastAPI,Depends
from pydantic import BaseModel
import models
from database import engine,get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Data(BaseModel):
    user:str
    address:str




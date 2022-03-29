from typing import List
from fastapi import Depends, FastAPI,status, Response,HTTPException
from . import schemes,models
from http import HTTPStatus
from .database import engine, SessionLocal,get_db
from sqlalchemy.orm import Session
from .routers import blog,user
from .hashing import Hash
models.Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(blog.rounter)
app.include_router(user.rounter) 
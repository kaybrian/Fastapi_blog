from fastapi import FastAPI
from . import models
from .database import engine 
from .routers import blog,user,authenticate
models.Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(authenticate.router)
app.include_router(blog.router)
app.include_router(user.router) 

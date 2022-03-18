from fastapi import FastAPI
from . import schemes,models
from .database import engine

models.Base.metadata.create_all(engine)
app = FastAPI()


@app.post('/blog/')
def create(request:schemes.Blog):
    return {"title":request.title,"body":request.body}
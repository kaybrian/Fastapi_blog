from fastapi import FastAPI
from . import schemes

app = FastAPI()


@app.post('/blog/')
def create(request:schemes.Blog):
    return {"title":request.title,"body":request.body}
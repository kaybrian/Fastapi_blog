from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.get('/blog')
def index(limit=10 , published : bool = True , sort : Optional[str] = None):
    if published:
        return {"Data":f'limit -> {limit} published blogs from the data base'}
    else:
        return {"Data":f'limit -> {limit} blogs from the data base'}

@app.get('/blog/unpublished')
def blog_unpublished():
    return {"Data":f'Unpublished blog'}

@app.get('/blog/{blog_id}')
def blog(blog_id:int):
    return {"Data":f'Blog ID is {blog_id}'}

@app.get('/blog/{blog_id}/comments')
def blog_comments(blog_id:int, limit=10):
    return {"Comments":f'Comments of blog ID-> {blog_id}'}


@app.post('/blog')
def create_blog(blog:Blog):
    return blog
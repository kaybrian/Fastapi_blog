from sys import prefix
from fastapi import APIRouter, Depends, HTTPException,status,Response
from typing import List
from .. import schemes,models
from http import HTTPStatus
from ..database import engine, get_db
from sqlalchemy.orm import Session
from ..repo import blog
models.Base.metadata.create_all(engine)

rounter = APIRouter(
    prefix="/blog",
    tags=['blog'],
)


@rounter.get('/',response_model=List[schemes.ShowBlog])   
def get_all_blogspot(db:Session = Depends(get_db)):
    return blog.get_all(db)
    
@rounter.post('/', status_code=status.HTTP_201_CREATED)
def create(request:schemes.Blog, db:Session = Depends(get_db)):
    return blog.create(request,db)


@rounter.get('/{id}', status_code=status.HTTP_200_OK,response_model=schemes.ShowBlog)
def get_blog(id:int,response: Response, db:Session = Depends(get_db)):
    return blog.show(id,db)


@rounter.delete('/{id}', status_code=HTTPStatus.NO_CONTENT)
def delete_blog(id:int,response: Response, db:Session = Depends(get_db)):
    return blog.destroy(id,db)


@rounter.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def blog_update(id:int,request:schemes.Blog, response: Response, db:Session = Depends(get_db)):
    return blog.update(id,request,db)


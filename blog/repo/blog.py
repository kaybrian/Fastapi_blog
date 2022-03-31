from sqlalchemy.orm import Session
from .. import models,schemes
from fastapi import APIRouter, Depends, HTTPException,status,Response
from http import HTTPStatus


def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request:schemes.Blog,db:Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)  
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the blog {id} you want to update doesnot exist")
    blog.delete(synchronize_session=False)    
    db.commit()
    return Response(status_code=HTTPStatus.NO_CONTENT.value)

def update(id:int, request:schemes.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the blog {id} you want to update doesnot exist")
    blog.update(request)
    db.commit()
    return "updated the title"

def show(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with ID of {id} is not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"Datail":f"Blog with ID of {id} is not found"}
    return blog
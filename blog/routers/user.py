from fastapi import APIRouter, Depends, HTTPException,status,Response
from typing import List
from .. import schemes,models
from http import HTTPStatus
from ..database import engine, get_db
from sqlalchemy.orm import Session
from ..hashing import Hash

models.Base.metadata.create_all(engine)

rounter = APIRouter()


# Creating the users in the Database 
@rounter.post('/user', response_model=schemes.UserShow,tags=['User'])
def create_user(request:schemes.User,db:Session = Depends(get_db)):
    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  
    return new_user
 
@rounter.get('/user/{id}', status_code=status.HTTP_200_OK,response_model=schemes.UserShow,tags=['User'])
def get_user(id:int,response: Response, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with ID of {id} is not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"Datail":f"User with ID of {id} is not found"}
    return user 
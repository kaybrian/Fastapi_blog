from fastapi import APIRouter, Depends, HTTPException,status,Response
from .. import schemes,models
from http import HTTPStatus
from ..database import engine, get_db
from sqlalchemy.orm import Session
from ..repo import user

models.Base.metadata.create_all(engine)

rounter = APIRouter(
    prefix="/user",
    tags=['User']
)


# Creating the users in the Database 
@rounter.post('/', response_model=schemes.UserShow )
def create_user(request:schemes.User,db:Session = Depends(get_db)):
    return user.user_create(request,db)
 
@rounter.get('/{id}', status_code=status.HTTP_200_OK,response_model=schemes.UserShow )
def get_user(id:int,response: Response, db:Session = Depends(get_db)):
    return user.show(id,db)
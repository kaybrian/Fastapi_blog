from fastapi import APIRouter, Depends, HTTPException,status,Response
from .. import models,schemes, database
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(
    prefix='/login',
    tags = ['Authentication'],
)


@router.post('/')
def login(request:schemes.Login,db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No user found in the system")
    if not Hash.verify(user.password , request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect Username or Password")
    # generate a JWT token
    
    return user
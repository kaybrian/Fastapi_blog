from fastapi import APIRouter, Depends, HTTPException,status,Response
from .. import models,schemes, database
from sqlalchemy.orm import Session
from ..hashing import Hash
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .. import token

router = APIRouter(
    prefix='/login',
    tags = ['Authentication'],
)


@router.post('/')
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No user found in the system")
    if not Hash.verify(user.password , request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Incorrect Username or Password",
            headers={"WWW-Authenticate": "Bearer"}
            )
    # generate a JWT token
    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
    
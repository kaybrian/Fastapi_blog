from pydantic import BaseModel
from typing import List,Optional


class Blog(BaseModel):
    title:str
    body:str

    class Config():
        orm_mode = True


class User(BaseModel):
    name:str
    email:str
    password:str

class UserShow(BaseModel):
    name:str
    email:str
    blogs:List[Blog] = []
    class Config():
        orm_mode = True

class ShowBlog(Blog):
    title:str
    body:str
    author:UserShow
    class Config():
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
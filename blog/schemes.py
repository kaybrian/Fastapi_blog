from pydantic import BaseModel
from typing import List

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

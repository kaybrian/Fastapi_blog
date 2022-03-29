from typing import List
from fastapi import Depends, FastAPI,status, Response,HTTPException
from . import schemes,models
from http import HTTPStatus
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .hashing import Hash
models.Base.metadata.create_all(engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.get('/blog',response_model=List[schemes.ShowBlog],tags=['blog'])   
def get_all_blogspot(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs
    

@app.post('/blog/', status_code=status.HTTP_201_CREATED,tags=['blog'])
def create(request:schemes.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)  
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog/{id}', status_code=status.HTTP_200_OK,response_model=schemes.ShowBlog,tags=['blog'])
def get_blog(id,response: Response, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with ID of {id} is not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"Datail":f"Blog with ID of {id} is not found"}
    return blog


@app.delete('/blog/{id}', status_code=HTTPStatus.NO_CONTENT,tags=['blog'])
def delete_blog(id,response: Response, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the blog {id} you want to update doesnot exist")
    blog.delete(synchronize_session=False)    
    db.commit()
    return Response(status_code=HTTPStatus.NO_CONTENT.value)



@app.put('/bog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['blog'])
def blog_update(id,request:schemes.Blog, response: Response, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the blog {id} you want to update doesnot exist")
    blog.update(request)
    db.commit()
    return "updated the title"


# Creating the users in the Database 
@app.post('/user', response_model=schemes.UserShow,tags=['User'])
def create_user(request:schemes.User,db:Session = Depends(get_db)):
    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  
    return new_user
 
@app.get('/user/{id}', status_code=status.HTTP_200_OK,response_model=schemes.UserShow,tags=['User'])
def get_user(id:int,response: Response, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with ID of {id} is not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"Datail":f"User with ID of {id} is not found"}
    return user 
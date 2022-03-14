from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"Data":{"message": "Hello World"}}

@app.get('/about')
def about():
    return {"Data":{"message": "About Page"}}
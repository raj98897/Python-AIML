from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello! World"}

@app.get("/user/{name}/{age}")
def user(name:str=Path(...,min_length=1, max_length=10), age:int=Path(...,ge=1, le=100), percent:float=Query(..., ge=1, le=100)):
    return {"user": name, "age": age}    

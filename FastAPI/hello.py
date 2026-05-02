import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
app = FastAPI()

@app.get("/hello")
async def index():
   return {"message": "Hello There"}

class Students(BaseModel):
   id : int
   name : str = Field(..., title="Name of student", min_length=1, max_length=10)
   subjects : List[str] = []

@app.post("/student/")
async def student_data(s1 : Students):
   return s1   

@app.get("/all")
async def All_data(s2 : Students):
   return s2

if __name__ == "__main__":
   uvicorn.run("hello:app", host="127.0.0.1", port=7000, reload=True)
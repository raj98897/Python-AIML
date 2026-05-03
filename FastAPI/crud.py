import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data = []

@app.get("/")
async def great():
    return {"message": "It's working"}

class Book(BaseModel):
    id : int
    title : str
    author : str
    publisher : str

@app.post("/add_book")
async def add_book(book: Book):
    data.append(book.model_dump())
    return data

@app.get("/list")
async def get_book():
    return data

@app.get("/list/{id}")
async def get_single(id: int):
    return data[id]

@app.put("/book/{id}")
def add_book(id: int, book: Book):
   data[id-1] = book
   return data

@app.delete("/book/{id}")
def delete_book(id: int):
   data.pop(id-1)
   return data    






if __name__ == "__main__":
    uvicorn.run("crud:app", host="127.0.0.1", port=9000, reload=True)






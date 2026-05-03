from pydantic import BaseModel


class StudentCreate(BaseModel):
    name : str
    age : int
    course : str

class StudentResponse(StudentCreate):
    id : int
    class config:
        orm_mode = True    
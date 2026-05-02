from typing import List
from pydantic import BaseModel

class Students(BaseModel):
    id : int
    name : str
    subjects : List[str] = []

data = {
    'id': 1,
    'name': 'Raaz',
    'subjects': ["Hindi", "English", "Maths"]
}
s1 = Students(**data)
print(s1)
print(s1.model_dump())
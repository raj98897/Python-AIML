from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Student
@app.post("/students/")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# Get All Students
@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

# Get Single Student
@app.get("/students/{id}")
def get_student(id: int, db: Session = Depends(get_db)):
    return db.query(models.Student).filter(models.Student.id == id).first()

# Update Student
@app.put("/students/{id}")
def update_student(id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    stu = db.query(models.Student).filter(models.Student.id == id).first()
    stu.name = student.name
    stu.age = student.age
    stu.course = student.course
    db.commit()
    return stu

# Delete Student
@app.delete("/students/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):
    stu = db.query(models.Student).filter(models.Student.id == id).first()
    db.delete(stu)
    db.commit()
    return {"message": "Deleted"}
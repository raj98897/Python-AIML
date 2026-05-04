from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

# 1. database connection
engine = create_engine("sqlite:///vehicles.db")

# 2. Session
Session = sessionmaker(engine)
db = Session()

# 3. Base
Base = declarative_base()

# 4. Table define
class Vehicles(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    model = Column(String)
    color = Column(String)

# 5. Table create

Base.metadata.create_all(engine)

# 6. Insert data
new_vehicle = Vehicles(name="Toyota",model="Corola",color="red")
db.add(new_vehicle)
db.commit()
print("New vehicle added successfully.")
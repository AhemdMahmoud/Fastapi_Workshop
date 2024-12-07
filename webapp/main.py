#r Restful methods in FastAPI

from fastapi import FastAPI,Query
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class Student(BaseModel):
    id: int
    name : str
    grad : int

Students = [
    Student(id=1,name="John",grad=90),
    Student(id=2,name="Jane",grad=80)
]

@app.get("/students")
def get_students():
    return Students

@app.post("/students")
def add_student(student: Student):
    Students.append(student)
    return student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for i in range(len(Students)):
        if Students[i].id == student_id:
            Students[i] = student
            return student
    return {"error":"Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index , student in enumerate(Students):
        if student.id == student_id:
            Students.pop(index)
            return {"message":"Student deleted"}

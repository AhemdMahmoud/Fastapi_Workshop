from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

app = FastAPI()

# Add CORS middleware for frontend communication
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.student_management
students_collection = db.students


# Pydantic model for student
class Student(BaseModel):
    id: int
    name: str
    grad: int


@app.get("/students")
async def get_students():
    students = []
    async for student in students_collection.find():
        student["_id"] = str(student["_id"])
        students.append(student)
    return students


@app.post("/students")
async def add_student(student: Student):
    # Check if student ID already exists
    existing_student = await students_collection.find_one({"id": student.id})
    if existing_student:
        raise HTTPException(status_code=400, detail="Student with this ID already exists.")

    result = await students_collection.insert_one(student.dict())
    student_dict = student.dict()
    student_dict["_id"] = str(result.inserted_id)
    return student_dict


@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student):
    result = await students_collection.update_one(
        {"id": student_id}, {"$set": student.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found.")
    return {"message": "Student updated successfully."}


@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    result = await students_collection.delete_one({"id": student_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found.")
    return {"message": "Student deleted successfully."}

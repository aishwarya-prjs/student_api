from fastapi import APIRouter, HTTPException
from app.models import Student
from app import services

router = APIRouter()

@router.post("/students")
def create_student(student: Student):
    return services.add_student(student)

@router.get("/students/{student_id}")
def read_student(student_id: int):
    student = services.get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    updated = services.update_student(student_id, student)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    deleted = services.delete_student(student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted"}
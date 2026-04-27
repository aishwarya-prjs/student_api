from utils.logger import logger

students_db = {}

def add_student(student):
    students_db[student.id] = student
    return student

def get_student(student_id):
    return students_db.get(student_id)

def update_student(student_id, student):
    if student_id in students_db:
        students_db[student_id] = student
        return student
    return None

def delete_student(student_id):
    return students_db.pop(student_id, None)
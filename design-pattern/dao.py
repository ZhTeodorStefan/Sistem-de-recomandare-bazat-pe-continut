from pymongo import MongoClient
from dto import StudentDTO

class StudentDAO:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://teodorstefanzaharia:OdTvBHwBaENZZiC0@main.g8ezz.mongodb.net/')
        self.db = self.client['testare']
        self.collection = self.db['studenti']

    def add_student(self, student_dto):
        student_data = {
            'school': student_dto.school,
            'student_name': student_dto.student_name
        }
        self.collection.insert_one(student_data)

    def get_all_students(self, school):
        students = self.collection.find({'school': school})
        student_names = [student['student_name'] for student in students]
        return StudentDTO(school, student_names).getall()
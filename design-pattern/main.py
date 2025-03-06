# https://www.analyticsvidhya.com/blog/2023/02/what-are-data-access-object-and-data-transfer-object-in-python/

from dao import StudentDAO
from dto import StudentDTO

student_dao = StudentDAO()

student1= "Lary"
student2 = "Mike"
school = "Hindenburg"

stud1 = StudentDTO(school,student1)
stud2 = StudentDTO(school,student2)

student_dao.add_student(stud1)
student_dao.add_student(stud2)

student_names = student_dao.get_all_students("Hindenburg")
print(student_names)
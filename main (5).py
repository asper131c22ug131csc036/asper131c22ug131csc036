class Student:

  def __init__(self, name, rno, cgpaverage):
    self.name = name
    self.rno = rno
    self.cgpaverage = cgpaverage


def sort_students(student_list):
  sorted_students = sorted(student_list,
class Student:

  def __init__(self, name, rno, cgpaverage):
    self.name = name
    self.rno = rno
    self.cgpaverage = cgpaverage


def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda x: x.cgpaverage,
                           reverse=True)
  return sorted_students


students = [
    Student("Aravind", "101", 3.0),
    Student("Barath", "102", 3.4),
    Student("Chandru", "103", 3.8),
    Student("Dharunraj", "104", 3.3)
]
sorted_students = sort_students(students)
for student in sorted_students:
  print(
      f"Name: {student.name}, rno: {student.rno}, CGPAVERAGE: {student.cgpaverage}"
  )￼Not                           key=lambda x: x.cgpaverage,
                           reverse=True)
  return sorted_students


students = [
Student("Aravind", "101", 3.0),
    Student("Barath", "102", 3.4),
    Student("Chandru", "103", 3.8),
    Student("Dharunraj", "104", 3.3)
]

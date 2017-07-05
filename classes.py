students = []

class Student:
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

        # student = {"name": name, "student_id": student_id}
        # students.append(student)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    # def add_student(self, name, student_id=332):
    #     student = {"name": name, "student_id": student_id}
    #     students.append(student)

# student = Student()
# student.add_student("Mark")

mark = Student("Mark")
print(mark)
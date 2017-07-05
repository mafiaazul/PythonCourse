students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append( student["name"].title() )
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)

def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students(f):
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")

def read_students(f):
    for line in f:
        yield line

read_file()
print_students_titlecase()

student_name = input( "Enter student name:" )
student_id = input( "Enter student ID: " )

add_student( student_name, student_id )
save_file(student_name)

# student_list = get_students_titlecase()

print_students_titlecase()

#answer = input("Do you want to add a student? Yes/No: ")
# while answer == 'Yes':
#     student_name = input( "Enter student name:" )
#     student_id = input( "Enter student ID: " )
#     add_student( student_name, student_id )
#     answer = input("Would you like to add another one? Yes/No: ")

# print(students)

# def var_args(name, **kwargs):
#    print(name)
#    print(kwargs["description"], kwargs["feedback"])

# add_student(name="Mark", student_id=15)

# var_args("Mark", description="Loves Python", feedback=None, pluralsight_subscriber=True)

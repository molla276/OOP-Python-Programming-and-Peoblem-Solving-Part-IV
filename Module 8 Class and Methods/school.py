class Students:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age 
        self. id = id

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
class Teacher:
    def __init__(self,name,course):
        self.name = name
        self.course = course

class School:
    def __init__(self, name, teachers, course, student):
        self.name = name
        self.teacher = teachers
        self.courses = courses
        self.students = student
    def get_students(self):
        for student in self.students:
            print(student.name)

school_name = 'Phitron'
ds_course = Course('Data Structure',  'Einisten')
teacher_1 = Teacher('Einistain',ds_course)
algo_course = Course('Algoritham', 'Edison')
teacher_2 = Teacher('Edison',algo_course)

student_1 = Students('Ariful',19,45)
student_2 = Students('Tasif',10,10)
student_3 = Students('Jarif',20,10)

teachers = [teacher_1,teacher_2]
students = [student_1,student_2,student_3]
courses = [algo_course, ds_course]


my_school = School(school_name, teachers,courses,students)
print(my_school.students)
my_school.get_students()



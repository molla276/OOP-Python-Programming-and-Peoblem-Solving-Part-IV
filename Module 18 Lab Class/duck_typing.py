class School:
    def __init__(self, name) -> None:
        self.schoolName = name
    def say_hello(self):
        print('Hello from school')
class Teacher:
    def __init__(self, name) -> None:
        self.teacherName = name
    def say_hello(self):
        print (f'Hello from {self.teacherName}')
        # print(f'Hello I am {self.studentName}')

class Student:
    def __init__(self, name,obj) -> None:
        self.studentName = name
        obj.say_hello()

school = School('trust school')
teacher = Teacher('Ms Rahima')
student = Student('Ariful',teacher)

class School:
    def __init__(self, name, address, principle= ''):
        self.name = name
        self.address = address
        self.principle= principle
        self.grades = []

    def add_grade(self, name, teacher):
        new_grade = Grade(name, teacher)
        self.grades.append(new_grade)

    def remove_grade(self, name):
        idx = 0
        for i, grade in enumerate(self.grades):
            if grade.name == name:                                                                                  
                idx = i
        del self.grades[idx]

class Grade:
    def __init__(self, name, teacher):
        self.students = []
        self.students = []
        self.teacher = teacher

    def __repr__(self):
        return f'{self.name} with teacher {self.treacher}'

    def __del__(self):
        print(f'Deleting{self.name}')


oxford = School('Oxford kid Academy', 'Mirput', 'Obayed Alam')
oxford.add_grade('class 3', 'Osman Gani')
oxford.add_grade('Class 5', 'Naxmul Islam')
oxford.add_grade('class 7', 'Tanai Islam')

print(oxford.grades)
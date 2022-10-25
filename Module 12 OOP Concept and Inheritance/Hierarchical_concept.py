class Employee:
    def __init__(self, name, id, salary, position, experience):
        self.name = name
        self.id = id
        self.salary = salary
        self.position = position
        self.experience = experience

class Developer(Employee):
    def __init__(self, name,id,salary,position, experience,tech, focus):
        self.tech = tech
        self.are_of_work = focus
        super().__init__(name,id,salary,position,experience)


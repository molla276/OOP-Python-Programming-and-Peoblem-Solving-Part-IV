from ast import Delete


class Student:
    def __init__(self, name, id, marks):
        self._name = name
        self.__id = id
        self.marks = marks

    @property
    def student_id(self):
        return self.__id 

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        return self._name 

chowsury = Student('Ariful Islam', 155, 100)
print(chowsury.student_id)
print(chowsury.student_name)
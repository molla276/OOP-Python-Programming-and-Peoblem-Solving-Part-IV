#Instance method
#Static method
#Class method
#Abstract method

class School:
    school_name = 'ABC School' #class variable
    def __init__(self, name) -> None:
        self.name = name #instance variable
    def printname(self):
        print(self.name)
    def change_name(self, name):
        self.school_name = name
    @classmethod
    def change_school_name(cls):
        cls.school_name = 'ABCD School'
    @staticmethod
    def greet():
        print('Hello Students')

s1 = School('naim')
s2 = School('Arif')
# School().get_name()
# s1.change_name('Habijabi school')
# School.change_school_name()
# print(s2.school_name)
School.greet()
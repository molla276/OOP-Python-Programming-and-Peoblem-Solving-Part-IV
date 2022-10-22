class Person:
    def __init__(self, name, age, money) -> None:
        self.name = name
        self.age = age
        self.money = money
    def __add__(self, other):
        # return self.money + other.money
        # return self.age + other.age
        return self.name + ' ' +other.name

    def __len__(self):
        return self.height

    def __mul__(self,other):
        return self.money * other.money

    def __eq__(self,other):
        return self.age == other.age

    def __call__(self):
        print(f'This is {self.name} age {self.age} and have money {self.money}')

alim = Person('Alim', 15, 400,67)
dalim = Person('Dalim', 16, 500)

print(len(alim)) 
print(alim == dalim) 


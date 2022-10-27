#overriding
class Animal:
    def __init__(self,name):
        self.name = name

    def make_sound(self):
        print('animal making some sound')

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)

    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self, name)

    def make_sound(self):
        print('Bark Bark')

class Horse(Animal):
    def __init__(self,name):
        super().__init__(name)
        
    def make_sound(self):
        print("meee meee")

don = Cat('don')
# don.make_sound()

shepard = Dog('German shepard')
# shepard.make_sound()

horse = Horse('horse')
# horse.make_sound()

don2 = Dog('don2')

animals = [don, shepard, horse, don2]

for animal in animals:
    animal.make_sound()
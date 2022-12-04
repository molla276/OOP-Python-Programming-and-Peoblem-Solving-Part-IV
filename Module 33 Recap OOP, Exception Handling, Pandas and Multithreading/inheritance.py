#single inheritance
#multiple inheritance
#multilevel inheritance

#single inheritance

# class Parent:
#     def __init__(self):
#         self.string1 = "I am a parent"

# class Child(Parent):
#     def __init__(self):
#         self.string2 = "I am a child"
#         super().__init__()

# S = Child()
# print(S.string2)

#Multiple inheritance
class GrandParent:
    def __init__(self) -> None:
        self.string = "I'm a grandParent"
class Parent:
    def __init__(self):
        self.string1 = "I am a parent"

class Child(Parent, GrandParent):
    def __init__(self):
        self.string2 = "I am a child"
        Parent.__init__(self)
        GrandParent.__init__(self)

S = Child()                                                                                                 
print(S.string)
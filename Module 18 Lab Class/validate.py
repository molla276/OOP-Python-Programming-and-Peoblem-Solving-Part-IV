# class Item:
#     def __init__(self,ItemName,ItemPrice):
#         assert ItemPrice >= 0, f'Error line 3,{ItemPrice} is invalid'
#         self.ItemName = ItemName
#         self.ItemPrice = ItemPrice

# item = Item("Plate", -10)
# print(item.ItemName, item.ItemPrice)

class Person:
    def __init__(self, Name, age, phoneNumber):
        assert age > 15,f'Only greater than 13 acceptable'
        assert len(phoneNumber) == 11, f'Invalid phone number'
        self.Name = Name
        self.age = age
        self.phoneNumber = phoneNumber

    def __repr__(self) -> str:
        return f'{self.Name} {self.age} {self.phoneNumber}'

user = Person('Ariful', 26, '01675560811')
print(user)

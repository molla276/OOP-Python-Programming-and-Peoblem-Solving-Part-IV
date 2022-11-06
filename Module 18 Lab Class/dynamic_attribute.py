class Item:
    all = [] #class attribute

    def __init__(self, itemName, itemPrice): #instance attribute
        self.__itemName = itemName
        self.__itemPrice = itemPrice
        self.all.append(self)

    def __repr__(self) -> str:
        return f'Item({self.itemName},{self.itemPrice})'

item1 = Item('Messi', '1M')
item2 = Item('Ronaldo', '3M')
item1._Item__discount = 10
item1._Item__itemName = 'Messi is out of form'
print(item1._Item__discount)
print(item1.__dict__)




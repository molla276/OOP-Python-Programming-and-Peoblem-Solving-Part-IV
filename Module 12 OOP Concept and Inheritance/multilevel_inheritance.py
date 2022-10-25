from math import remainder
from pydoc import pager


class Vehicle:
    def __init__(self, name, license, price):
        self.name = name
        self.license = license
        self.price = price

    def start(self):
        print(f'{self.name} started')

class Bus(Vehicle):
    def __init__(self, name, license, price, seat, ticket_price):
        self.seat = seat
        self.ticket_price = ticket_price
        print('Vehicle class init called')

    def sell_ticket(self, customer_name, quantity, amount):
        self.available_sets = quantity
        remainder = amount - self.ticket_price * quantity
        if remainder >=0:
            return Ticket(customer_name)
        return 'no ticket for you'
class AcBus(Bus):
    def __init__(self):
        pass

class MiniBus(Bus):
    def __init__(self):
        print('mini bus created')
        super().__init__('Mini Mini', 'DHA158',1200000,50,450)
        
class Ticket:
    def __init__(self, owner):
        self.owner = owner

mini = MiniBus()
print(mini.seat)
class Bus:
    owner = 'Ena Transport'

    def __init__(self, route, license, driver, trips):
        self.route = route
        self.license = license
        self.driver = driver
        self.trips = trips

    def start_trips(self, start_times):
        self.trips.append(start_times)

class Driver:
    def __init__(self, name, mobile, license, address, salary):
        pass

    def driver(self, start, end):
        pass

    def take_vacation(self):
        pass

    def withdraw_salary(self):
        pass
class Passenger:
    def __init__(self, name, mobile, destination):
        pass
    def purchase_ticket(self, destination, money):
        pass
class Manager:
    def __init__(self, name, mobile, department):
        pass

class Counter:
    def __init__(self, manager, location):
        pass

rashed = Passenger('Arif','01675560811', 'khulna')

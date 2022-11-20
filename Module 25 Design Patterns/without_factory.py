class Bike:
    def __init__(self, driver, rate) -> None:
        self.rate = rate
        self.driver = driver

    def get_fare(self, distance):
        return distance * self.rate 

class Car:
    def __init__(self, driver, rate) -> None:
        self.rate = rate
        self.driver = driver

    def get_fare(self, distance):
        return distance * self.rate

class CNG:
    def __init__(self, mama, rate) -> None:
        self.driver = mama
        self.rate = rate

    def get_fare(self, distance):
        return distance * self.rate

b1 = Bike('Masud', 5)
c1 = Car('Masud', 10)
g1 = CNG('Karim', 8)

customers = [10,20,5]
for distance in customers:
    print(g1.get_fare(distance))
    print(b1.get_fare(distance))
    print(c1.get_fare(distance))
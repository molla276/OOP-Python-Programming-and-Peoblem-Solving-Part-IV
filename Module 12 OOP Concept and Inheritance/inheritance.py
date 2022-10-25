# inharitance
# base class will have only the common attributes and methods

class Device:
    def __init__(self, brand, price, color,disk_size):
        self.brand = brand
        self.price = price
        self.color = color
        self.disk_size = disk_size

    def re_sale(self):
        print('ready to sell again')

class Laptop(Device):
    def __init__(self, brand, price, color, disk_size):
        self.brand = brand
        self.price = price
        self.color = color
        self.disk_size = disk_size

    def run(self):
        print('running the laptop')

    def __repr__(self):
        return f'Laptop: {self.brand}: {self.price} : {self.color}'

    def purchase(self, money):
        if (money < self.price):
            return 'NO laptop for you'
        else:
            print('This is your laptop')
            return money - self.price


class Phone:
    def __init__(self, brand, price, color, camera, sim_num):
        self.brand = brand
        self.price = price
        self.color = color
        self.camera = camera
        self.sim_num = sim_num

    def __repr__(self):
        return f'Phone: {self.brand}: {self.price} : {self.color} : {self.camera} : {self.sim_num}'

    def is_dual_sim(self):
        return self.sim_num > 1

    def is_digital(self):
        return self.watch+j


class Watch:
    def __int__(self, brand, price, color, watch_type):
        self.brand = brand
        self.price = price
        self.color = color
        self.watch_type = watch_type

    def is_digital(self):
        return self.watch_type == 'digital'


class Manager:
    def __init__(self, name, salary, experience, designation):
        pass

    def withdraw_salary(self):
        pass

    def day_total_sales(self):
        pass

    def handle_customer_complain(self):
        pass


class SalesPerson:
    def __init__(self, name, salary, experience, designation, commission):
        pass

    def withdraw_salary(self):
        pass


Lenovo = Laptop('Lenovo', 17000, 'Red', '30GB')
hp = Laptop('Hp', 35000, 'Silver', '250gb')
print(hp)
print(Lenovo)
Oppo = Phone('Oppo', 5000, 'Grey', '12px', 2)
SamSung = Phone('SamSung', 20000, 'Black', '16px', 1)
print(Oppo)
print(SamSung)
hp.re_sale()

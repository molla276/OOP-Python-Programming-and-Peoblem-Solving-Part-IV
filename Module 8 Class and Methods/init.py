class Phone:
    manufacture = 'chine'
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color

    def send_sms(self,number,text):
        sms = f'sending: {text} to {number}'
        return sms

my_phone = Phone('oppo', 13000, 'red')
print(my_phone.brand, my_phone.manufacture)


her_phone = Phone('iphone',85000,'purple')
print(her_phone.brand, her_phone.price)

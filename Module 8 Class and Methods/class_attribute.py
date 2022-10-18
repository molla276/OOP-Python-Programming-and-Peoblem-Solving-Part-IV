class Shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_chart(self, item):
        self.cart.append(item)

shopper_1 = Shop('Alu khan')
shopper_1.add_to_chart('tshirt')
print(shopper_1.cart)

shopper_2 = Shop('Rohim khan')
shopper_2.add_to_chart('shoes')
print(shopper_2.cart)
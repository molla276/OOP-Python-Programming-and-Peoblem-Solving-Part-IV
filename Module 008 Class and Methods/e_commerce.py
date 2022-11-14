class Shopper:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self, items, price, quantity):
        self.cart.append({'items':items, 'price':price, 'quantity':quantity})

    def checkout(self, amount):
        price = 0
        for items in self.cart:
            print(items)
            price += items['price'] * items['quantity']
        if amount < price:
            return f'Please give me more money: {price - amount}'
        elif amount > price:
            return f'Here are the items and extra money: {amount - price}'
        else:
            return 'Here are the items'

shopping = Shopper('Bag Tan')
shopping.add_to_cart('Tshirt', 10000, 5)
shopping.add_to_cart('shirt', 20000, 3)
shopping.add_to_cart('Pshirt', 30000, 2)

reply = shopping.checkout(5000000)
print(reply) 

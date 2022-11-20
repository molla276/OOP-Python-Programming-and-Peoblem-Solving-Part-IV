class Date:
    def __init__(self) -> None:
        self.date = {
            'order1': {'item': 'laptop', 'price' : 45000},
            'order2': {'item': 'tab', 'price' : 5000},
            'order3': {'item': 'phone', 'price' : 65000},
            'order4': {'item': 'watch', 'price' : 25000},
        }

    def get_order_details(self, orderId):
        return self.date[orderId]

class Application:
    pass

class GUI:
    pass
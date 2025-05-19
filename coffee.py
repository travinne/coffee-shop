
class Coffee:

    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
            self._orders = []
        else:    
            raise ValueError('name of coffee must at least have 3 characters') 
          
    @property
    def name(self):
        return self._name
    
    def orders(self):
        return Coffee.orders()

    def customers(self):
        return list({order.customer for order in self._orders})
    
    def order_Number(self):
        return len(self._orders())

    def coffee_pricing(self):
        if not self._orders:
            return 0 
        return sum (order.price for order in self._orders) / len(self._orders)
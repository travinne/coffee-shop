from order import Order

class Customer:
    def __init__(self, name):
      self.name = name
      self._orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
      if isinstance(value, str) and len(value)  >= 1 and len(value) <= 15:
        self._name = value
      else:
        raise ValueError('Customer name must contain between 1 to 15 characters!')

    def orders(self):
        return self._orders

    def coffee(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        order =  Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order
        


    def  coffeeShop(cls, coffee):
        shoppers = {}
        for order in coffee.orders():
         
                shoppers[order.customer] = shoppers.get(order.customer, 0) + order.price
        if not shoppers:
            return None
        return max(shoppers, key = shoppers.get)
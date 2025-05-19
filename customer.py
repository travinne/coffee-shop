from order import Order

class customers:
  def __init__(self, name):
    self.name = name
    self.orders = []

  def name(self):
    return self.name

  def name(self, value):
    if isinstance(value, str) and len(value)  >= 1 and len(value) <= 15:
        self.name = value
    else:
        raise ValueError('Customer name must contain between 1 to 15 characters!')

  def orders(self):
    return [order for order in Order.allOrders if order.customers == self]

  def coffee(self):
    return list({order.coffee for order in self.orders()})

  def createOrder(self, coffee, price):
        return Order(self, coffee, price)


  def  coffeeShop(cls, coffee):
        customer_spending = {}
        for order in order.allOrders:
            if order.coffee == coffee:
                customer_spending[order.customers] = customer_spending.get(order.customers, 0) + order.price

        if not customer_spending:
            return None
        return max(customer_spending, key=customer_spending.get)
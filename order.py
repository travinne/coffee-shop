class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(price,(int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be  between float 1.0 and float 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price

    
    @property
    def price(self):
        return self._price
    @property
    def customer(self):
        return self._customer
    @property
    def coffee(self):
        return self._coffee
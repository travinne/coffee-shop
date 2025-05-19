from customer import Customer
from coffee import Coffee


customer1 = Customer("Alice")
customer2 = Customer("Bob")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")


customer1.create_order(coffee1, 3.5)
customer2.create_order(coffee2, 4.0)
customer1.create_order(coffee2, 5.0)


print(f"{coffee1.name} has {coffee1.order_Number()} orders")
print(f"Average price: {coffee1.coffee_pricing()}")
print(f"Most aficionado: {Customer.coffeeShop(coffee1).name}")

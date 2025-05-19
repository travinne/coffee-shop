from customer import customers
from coffee import Coffee


alice = customers("Alice")
bob = customers("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")


alice.create_order(latte, 3.5)
alice.create_order(espresso, 4.0)
bob.create_order(latte, 5.0)


print("Alice Coffees:", [c.name for c in alice.coffees()])
print("Latte Orders:", latte.num_orders())
print("Latte Avg Price:", latte.average_price())
print("Most aficionado of Latte:", Customer.most_aficionado(latte).name)
"""
Този модул изчислява общата цена на поръчка на пици.
"""

PIZZA_PRICE = 12.50
DELIVERY_COST = 2.99
pizza_ordered = 5

total_pizza_cost = PIZZA_PRICE * pizza_ordered

final_price = total_pizza_cost + DELIVERY_COST

message = f"Вие поръчахте {pizza_ordered} пици. Общата цена за плащане е: {final_price} лв."

print(message)


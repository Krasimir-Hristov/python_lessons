"""
Този модул изчислява общата цена на поръчка на пици.
"""

# Константи
PIZZA_PRICE = 12.50
DELIVERY_COST = 2.99

# <-- ЕДИН празен ред, за да отделим константите от основната логика.

while True:
    pizzas_ordered_str = input("Колко пици желаете да поръчате? ")

    try:
        pizzas_ordered = int(pizzas_ordered_str)
    except ValueError:
        print("Грешка: Моля, въведете цяло число.")
        continue

    if pizzas_ordered > 0:
        break
    else:
        print("Грешка: Броят на пиците трябва да е положително число.")

# <-- ЕДИН празен ред. Цикълът за валидация приключи. Започва нова логическа част - изчисленията.

total_pizza_cost = PIZZA_PRICE * pizzas_ordered
final_price = 0

if pizzas_ordered >= 5:
    final_price = total_pizza_cost
    print("Поздравления, получавате безплатна доставка!")
else:
    final_price = total_pizza_cost + DELIVERY_COST

# <-- ЕДИН празен ред. Изчисленията приключиха. Сега следва финалният изход.

print(f"Вие поръчахте {pizzas_ordered} пици.")
print(f"Общата сума за плащане е: {final_price:.2f} лв.")
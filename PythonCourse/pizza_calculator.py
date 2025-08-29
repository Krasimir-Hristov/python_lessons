"""
Този модул изчислява общата цена на поръчка на пици.
"""

PIZZA_PRICE = 12.50
DELIVERY_COST = 2.99

pizza_ordered = 0

while True:
    pizza_ordered_str = input("Колко пици искате да поръчате? ")

    try:
      pizza_ordered = int(pizza_ordered_str)
     

    except ValueError:
      print("Грешка: Моля, въведете цяло число.")
      continue

    if pizza_ordered > 0:
        break
    else:
        print("Грешка: Моля, въведете положително число.")
        
        

total_pizza_cost = PIZZA_PRICE * pizza_ordered
final_price = 0
if pizza_ordered >= 5:
  final_price = pizza_ordered * PIZZA_PRICE
  print("Вие получавате безплатна доставка!")
else:
 final_price = total_pizza_cost + DELIVERY_COST


print(f"Вие поръчахте {pizza_ordered} пици. ") 
print(f"Общата цена е {final_price:.2f} лева.")
  







"""Docstring"""

PIZZA_PRICE = 12.50
DELIVERY_COST = 2.99
FREE_DELIVERY_FROM = 5

def get_number_of_pizzas():
    """Get number of pizzas from user input and validate it."""

    while True:
        pizza_ordered_str = input("How many pizzas do you want to order? From 5 get free delivery!")

        try:
            pizza_ordered = int(pizza_ordered_str)

            if pizza_ordered > 0:
                return pizza_ordered
            else:
                print("Error: The number of pizzas must be a positive integer.")
        except ValueError:
            print("Error: Please enter a valid integer.")


def calculate_final_price(pizzas_ordered, free_delivery_from, pizza_price, delivery_cost ):
    """Calculate the final price based on the number of pizzas ordered."""
    
    total_price = 0

    if pizzas_ordered >= free_delivery_from:
        total_price = pizzas_ordered * pizza_price
        print("Congratualtions you got free delivery!!")
    else:
        total_price =(pizzas_ordered * pizza_price) + delivery_cost

    return total_price


total_pizzas = get_number_of_pizzas()

total_pizzas_cost = calculate_final_price(total_pizzas, FREE_DELIVERY_FROM, PIZZA_PRICE, DELIVERY_COST)


print("---Your Order---")
print(f"Count pizzas: {total_pizzas}")
print(f"Total cost: {total_pizzas_cost:.2f}")
       

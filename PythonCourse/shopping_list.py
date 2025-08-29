shoping_list = []

while True:
  
  try:
    product = input('Add new product or type "end" to finish: ')
    if product.lower() == 'end':
       break
    else:
       shoping_list.append(product)

  except ValueError:
      print("Error: Invalid input. Please try again.")
      continue
  

print("Your shopping list:")

for item in shoping_list:
      print(f"- {item}")

print(len(shoping_list), "items in total.")   
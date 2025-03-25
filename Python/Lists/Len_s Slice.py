# 1
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
# 2
price = [2, 6, 1, 3, 2, 7, 2]
#3
num_pizza = len(toppings)
#4
print(f"We sell {num_pizza} different kinds of pizzas.")
#5
pizzas = list(zip(price, toppings))
#6
print(pizzas)
#7
sorted_pizzas = sorted(pizzas)
#8
cheapest_pizza = sorted_pizzas[0]
#9
priciest_pizza = sorted_pizzas[6]
#10
three_cheapest = sorted_pizzas[:3]
#11
print(three_cheapest)
#12
num_two_dollar_slices = price.count(2)
print(num_two_dollar_slices)
print("Activity-1")
#1
list1 = range(2, 20, 2)
#2
print(len(list1))
#3
list2 = range(2, 20, 3)
print(len(list2))

print()
print("Activity-2")
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
#1
index4 = employees[4]
#2
print(len(employees))
#3&4
print(employees[5])

print()
print("Activity-3")
shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
#1
print(len(shopping_list))
#2
last_element = shopping_list[-1]
#3
element5 = shopping_list[5]
#4
print(element5)
print(last_element)

print()
print("Activity-4")
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
beginning = suitcase[0:2]
#1
print(beginning)
#2
beginning = suitcase[0:4]
print(beginning)
#3
middle = suitcase[2:4]
print(middle)

print()
print("Activity-5")
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
#1
start = suitcase[:3]
print(start)
#2
end = suitcase[2:]
print(end)

print()
print("Activity-6")
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie',
'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
#1
jake_votes = votes.count("Jake")
#2
print(jake_votes)

print()
print("Activity-7")
### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace',
'1600 Pennsylvania Ave', '10 Downing St.']
# Sort addresses here:
addresses.sort()
print(addresses)

### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
#3
names.sort()

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']
sorted_cities = cities.sort()
print(sorted_cities)
# It is not sorted because we sorted cities not sorted_cities variable
print(cities)

print()
print("Activity-8")
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
#1
games_sorted = sorted(games)
#2
print(games)
print(games_sorted)
# It is because the games_sorted list has the alphabetically arranged version of the list games.

print()
print("Activity-9")
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser',
'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets',
'sheets', 'pillow', 'pillow']
#1
inventory_len = len(inventory)
print(inventory_len)
#2
first = inventory[0]
print(first)
#3
last = inventory[18]
print(last)
#4
inventory_2_6 = inventory[2:6]
print(inventory_2_6)
#5
first_3 = inventory[:3]
print(first_3)
#6
twin_beds = inventory.count("twin bed")
print(twin_beds)
#7
print(inventory.sort())
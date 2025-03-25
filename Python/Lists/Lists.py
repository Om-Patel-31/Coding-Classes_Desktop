print("Activity-1")
heights = [61, 70, 67, 64, 65]
broken_heights = [65, 71, 59, 62]

print()
print("Activity-2")
ints_and_strings = [1, 2, 3, 'four', 'five','six','seven']
sam_height = ['Sam', 67]

print()
print("Activity-3")
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]
age = [['Aaron', 15], ['Dhruti', 16]]

print()
print("Activity-4")
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']
names_and_dog_names = zip(names, dogs_names)
print(list(names_and_dog_names))

print()
print("Actiivyt-5")
my_empty_list = []

print()
print("Activity-6")
orders = ['daisies', 'periwinkle']
print(list(orders))
orders.append('tulips')
print(list(orders))
orders.append('roses')
print(list(orders))

print()
print("Activity-7")
orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']
new_orders = orders + ['lilac', 'iris']
print(new_orders)
broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)

print()
print("Activity-8")
my_range = range(9)
print(list(my_range))
list2 = range(8)
print(list(list2))

print()
print("Activity-9")
list1 = range(5, 15, 3)
print(list(list1))
list3 = range(0, 40, 5)
print(list(list3))

print()
print("Activity-10")
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
age = []
age.append(42)
all_ages = [32, 41, 29]
all_ages.append(42)
name_and_age = zip(first_names, all_ages)
ids = range(4)
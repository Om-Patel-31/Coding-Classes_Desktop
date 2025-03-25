print("Activity-1")
dog_breeds = ['french_bulldog', 'dalmatian', 'shih tzu', 'poodle', 'collie']
for breed in dog_breeds:
    print(breed)

print()
print("Activity-2")
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
    print(game)
#print
print()
#3
for game in sport_games:
    print(game)

print()
print("Activity-3")
promise = "I will not chew gum in class"
for i in range(5):
    print(promise)
    
print()
print("Activity-4")
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for student in students_period_A:
    students_period_B.append(student)
    
print(students_period_B)

print()
print("Activity-5")
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle',
'collie']
dog_breed_I_want = 'dalmatian'
for dog in dog_breeds_available_for_adoption:
    print(dog)
    if dog == dog_breed_I_want:
        print("They have the dog I want")
        break
    
print()
print("Activity-6")
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for age in ages:
    if age<21:
        continue
    print(age)

print()
print("Activity-7")
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie",
"Arius", "Loki"]
students_in_poetry = []
while len(students_in_poetry) < 6:
    student = all_students.pop()
    students_in_poetry.append(student)

print(students_in_poetry)

print()
print("Activity-8")
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for scoops_sold in sales_data:
    for scoops in scoops_sold:
        print(scoops)
    
print()
print("Activity-9")
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster= [height for height in heights if height > 161]
print(can_ride_coaster)

print()
print("Activity-10")
celsius = [0, 10, 15,32, -5, 27, 3]
farhenheit = [temp * 9/5 + 32 for temp in celsius]
print(farhenheit)

print()
print("Actiivty-11")
# 1
single_digits = [0,1,2,3,4,5,6,7,8,9]
# 3
squares = []
# 2
for i in single_digits:
    print(i)
    # 4
    square = i ** 2
    squares.append(square)
# 5
print(squares)
# 6
cubes = [single_digits**3 for single_digits in single_digits]
# 7
print(cubes)
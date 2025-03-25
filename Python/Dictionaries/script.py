print("Activity-1")
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

print()
print("Activity-2")
translations = {"English":"Sindarin", "mountain":"orod", "bread":"bass", "friend":"mellon", "horse":"roch"}

print()
print("Activity-3")
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

print()
print("Activity-4")
my_empty_dictionary = {}

print()
print("Activity-5")
animals_in_zoo = {"zebras": 8, "monkeys": 12, "dinosaurs": 0}
print(animals_in_zoo)

print()
print("Actiivty-6")
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238, "theLooper": 138475, "stringQueen": 85739}
print(user_ids)

print()
print("Activity-7")
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia", "Supporting Actress": "Voila Davis"}
oscar_winners["Best Picture"]= "Moonlight"
print(oscar_winners)

print()
print("Activity-8")
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = list(zip(drinks, caffeine))
drinks_to_caffeine = {key:value for key, value in zipped_drinks}

print(zipped_drinks)
print(drinks_to_caffeine)

print()
print("Activity-9")
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 94, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
plays["Purple Haze"] = 1
plays["Respect"] = 94
library = {
    "The Best songs" : plays,
    "Sunday Feelings" : {}
        }
print(library)
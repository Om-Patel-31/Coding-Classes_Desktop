# Creating Menus
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __str__(self):
        return f"{self.name} is available from {self.start_time} to {self.end_time}"

    def calculate_bill(self, purchased_items):
        total = sum(self.items[item] for item in purchased_items if item in self.items)
        return f"The cost of your {self.name} order is ${total:.2f}"

# Creating Franchises
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
        
    def __str__(self):
        return f"Franchise located at {self.address}"
    
    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            start_hour = int(menu.start_time[:-2])
            end_hour = int(menu.end_time[:-2])
            if menu.start_time.endswith("pm") and start_hour != 12:
                start_hour += 12
            if menu.end_time.endswith("pm") and end_hour != 12:
                end_hour += 12
            if start_hour <= time < end_hour:
                available_menus.append(menu)
        return available_menus

# Creating Business
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises
    
    def __str__(self):
        return f"Business: {self.name} with {len(self.franchises)} franchise(s)"

# Brunch Menu
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 
    'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu("Brunch", brunch_items, "11am", "4pm")

# Early Bird Menu
earlybird_items = {
    'salumeria plate': 8.00, 
    'salad and breadsticks (serves 2, no refills)': 14.00, 
    'pizza with quattro formaggi': 9.00, 
    'duck ragu': 17.50, 
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50, 'espresso': 3.00,
}
earlybird = Menu("Early-bird", earlybird_items, "3pm", "6pm")

# Dinner Menu
dinner_items = {
    'crostini with eggplant caponata': 13.00, 
    'ceaser salad': 16.00, 
    'pizza with quattro formaggi': 11.00, 
    'duck ragu': 19.50, 
    'mushroom ravioli (vegan)': 13.50, 
    'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu("Dinner", dinner_items, "5pm", "11pm")

# Kids Menu
kids_items = {
    'chicken nuggets': 6.50, 
    'fusilli with wild mushrooms': 12.00, 
    'apple juice': 3.00
}
kids = Menu("Kids", kids_items, "11am", "9pm")

# Testing
brunch_order = ['pancakes', 'home fries', 'coffee']
brunch_bill = brunch.calculate_bill(brunch_order)
print(brunch_bill)

earlybird_order = ['salumeria plate', 'mushroom ravioli (vegan)']
earlybird_bill = earlybird.calculate_bill(earlybird_order)
print(earlybird_bill)

menus = [brunch, earlybird, dinner, kids]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

print(flagship_store)
print(new_installment)

print("\n Available Menus at 12pm:")
for menu in flagship_store.available_menus(12):
    print(menu)

print("\n Available Menus at 5pm:")
for menu in new_installment.available_menus(17):
    print(menu)

franchises = [flagship_store, new_installment]
first_business = Business("Basta Fazoolin' with my Heart", franchises)
print(f"\n {first_business}")

arepas_menu = {
'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa':
7.50
}

arepas_place = "189 Fitzgerald Avenue"

arepa_franchise = Franchise(arepas_place, [arepas_menu])

second_business = Business("Take a' Arepa", [arepas_place])
print(f"\n{second_business}")
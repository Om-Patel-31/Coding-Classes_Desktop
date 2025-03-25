print("Activity-1")
class Bin:
    pass
    class RecyclingBin:
        pass

print()
print("Activity-2")
class OutofStock(Exception):
    """
    Exception for when we run out of any color
    """
    pass

class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"
    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        if self.stock.get(color, 0) > 0:
            self.stock[color] = self.stock[color] - 1
        else:
            raise OutofStock('Sorry, ' + color + ' candles are out of stock.')

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

try:
    candle_shop.buy('green')
except OutofStock as e:
    print(e)

print()
print("Activity-3")
class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text

class User:
    def __init__(self, username):
        self.username = username
    def edit_message(self, message, new_text):
        if message.sender == self.username:
            message.text = new_text

class Admin(User):
    def edit_message(self, message, new_text):
        message.text = new_text

msg = Message(sender="user1", recipient="user2", text="Hello")
user = User(username="user1")
admin = Admin(username="admin")

print("Before user edited this: " + msg.text)
user.edit_message(msg, "Hi")
print(f"After the user edited the message: {msg.text}")

admin.edit_message(msg, "Admin edited")
print(f"After the admin edited: " +  msg.text)

print()
print("Activity-4")
class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions

class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions):
        super().__init__(potatoes, celery, onions)
        self.raisins = 40

special_salad = SpecialPotatoSalad(3,2,1)
print("Potatoes: " + str(special_salad.potatoes) + " Celery: " + str(special_salad.celery) + " Onions: " + str(special_salad.onions) + " Raisins: " + str(special_salad.raisins))

print()
print("Activity-5")
class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item

class VehicleInsurance(InsurancePolicy):
    def __init__(self, price_of_item):
        super().__init__(price_of_item)
    
    def get_rate(self):
        return 0.001 * self.price_of_insured_item

class HomeInsurance(InsurancePolicy):
    def __init__(self, price_of_item):
        super().__init__(price_of_item)

    def get_rate(self):
        return 0.0005 * self.price_of_insured_item
    
vehicle_policy = VehicleInsurance(20000)
home_policy = HomeInsurance(3000000)

print(f"Vehicle Insurance rate: {vehicle_policy.get_rate()}")
print(f"Home Insurance rate: {home_policy.get_rate()}")

print()
print("Activity-6")
a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

list_len = len(a_list)
dict_len = len(a_dict)
string_len = len(a_string)

print(f"Length of the list is {list_len}\n"
      f"Length of the dictionary is {dict_len}\n"
      f"Length of the string is {string_len}")

print()
print("Activity-7")
class Atom:
    def __init__(self, label):
        self.label = label
    
    def add(self, other):
        new_molecule = str(self.label) + str(other.label)
        return new_molecule

class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms

sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
# salt = sodium + chlorine
salt = sodium.add(chlorine)
print(salt)

print()
print("Activity-8")
class LawFirm:
    def __init__(self, practice, lawyers):
        self.practice = practice
        self.lawyers = lawyers
    
    def __len__(self):
        return len(self.lawyers)

    def __contains__(self, lawyer):
        return lawyer in self.lawyers

d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

print(len(d_and_p))

print("Donelli" in d_and_p)
print("Smith" in d_and_p)

print()
print("Activity-9")
class SortedList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.sort()
    
    def append(self, value):
        super().append(value)
        self.sort()
        
sorted_list = SortedList(4,1,5)
print(sorted_list)
sorted_list.append(3)
print(sorted_list)

print()
print("Additional Problem")
class FallbackDict(dict):
    def __init__(self, fallback_value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fallback_value = fallback_value
    
    def __getitem__(self, key):
        return super().get(key, self.fallback_value)

fallback_dict = FallbackDict("Not Found", {'a': 1, 'b': 2, 'c': 3})
print(fallback_dict['a'])
print(fallback_dict['c'])
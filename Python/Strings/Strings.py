print("Activity-1")
favorite_word = "failure"
print(favorite_word)

print()
print("Activity-2")
my_name = "Om"
first_initial = my_name[0]
print(first_initial)

print()
print("Activty-3")
first_name = "Rodrigo"
last_name = "Villanueva"
new_account = last_name[5]
temp_password = last_name[3:6]
print(new_account)
print(temp_password)

print()
print("Activty-4")
first_name = "Julie"
last_name = "Blevins"
def account_generator(first_name, last_name):
    new_account = first_name[:3] + last_name[:3]
    return new_account

print(account_generator("Julie", "Blevins"))

print()
print("Activity-5")
first_name = "Reiko"
last_name = "Matsuki"
def password_generator(first_name, last_name):
    temp_password = first_name[3:] + last_name[3:]
    return temp_password

print(account_generator("Reiko", "Matsuki"))

print()
print("Activity-6")
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]
print(second_to_last)
print(final_word)

print()
print("Activty-7")
first_name = "Bob"
last_name = "Daily"
fix = first_name[-2:]
fixed_first_name = "R" + fix
print(fixed_first_name)

print()
print("Activity-8")
password = "theycallme\"crazy\"91"
print(password)

print()
print("Activity-9")
def get_length(word):
    counter = 0
    for letters in word:
        counter+=1
    return counter

print(get_length("blue"))

print()
print("Activity-10")
def letter_check(word, letter):
    if letter in word:
        return True
    else:
        return False


print()
print("Activity-11")
def takestring(big_string, little_string):
    if little_string in big_string:
        return True
    else:
        return False

print(takestring("watermelon", "berry"))

print()
print("Activity-11.2")
def common_letters(string_one, string_two):
    common = []
    for letter in string_one:   
        if (letter in string_two) and not (letter in common):
            common.append(letter)
    return common
print(common_letters("banana", "cream"))

print()
print("Activity-12")
def username_generator(firstname, lastname):
    username = firstname[:3] + lastname[:4]
    if len(firstname) < 3:
        username = firstname + lastname[:4]
    elif len(last_name) < 4:
        username = firstname[:3] + lastname
    elif len(firstname) < 3 and len(lastname) < 4:
        username = firstname + lastname
    
    return username

print(username_generator("Abe", "Simpson"))

def password_generator(username):
    password = ""
    for i in range(0, len(username)):
        password += username[i - 1]
    return password

print(password_generator("AbeSimp"))
#Activity-1
print('Activity1')
print()
def sing_song():
    print("You may say I'm a dreamer")
    print("But I'm not the only one")
    print("I hope some day you'll join us")
    print("And the world will be as one")
    
sing_song()
sing_song()

print()
#Activity-2
print("Activity2")
print()
def loading_screen():
    print("The page is loading...")

loading_screen()

print()
print("Activity3")
print()
def about_this_computer():
    print("This computer is running on version Everest Puma")
    print("This is your desktop")
about_this_computer()

print()
def about_this_computer():
    print("This computer is running on version Everest Puma")
print("This is your desktop")
about_this_computer()

print()
#Activity-4
print("Activity4")
print()

def mult_two_add_three():
    number = 5
    print(number*2 + 3)

mult_two_add_three()

print()
def mult_two_add_three(number):
    print(number*2 + 3)

mult_two_add_three(1)

print()
def mult_two_add_three(number):
    print(number*2 + 3)
    
mult_two_add_three(5)

print()
def mult_two_add_three(number):
    print(number*2 + 3)

mult_two_add_three(-1)

print()
def mult_two_add_three(number):
    print(number*2 + 3)

mult_two_add_three(0)

print()
#Activity-5
print("Activity5")
print()
def mult_x_add_y(number,x,y):
    print(number*x+y)

mult_x_add_y(5,2,3)

print()
def mult_x_add_y(number,x,y):
    print(number*x+y)

mult_x_add_y(1,3,1)

print()
#Activity-6
print("Activity6")
print()
def create_spreadsheet(title):
    print("Creating a spreadsheet called "+title)

create_spreadsheet("Downloads")
print()
def create_spreadsheet(title, row_count):
    print("Creating a spreadsheet called "+title)

create_spreadsheet("Downloads",1000)
print()
def create_spreadsheet(title, row_count):
    print("Creating a spreadsheet called "+ title+ " with "+ str(row_count)+ " rows")

create_spreadsheet("Downloads",1000)
print()
def create_spreadsheet(title, row_count):
    print("Creating a spreadsheet called "+title+" with "+ str(row_count)+" rows")

create_spreadsheet("Applications",10)

print()
# Activity-7
print("Activity7")
print()
def calculate_age(current_year, birth_year):
    age = current_year-birth_year
    return age

my_age = calculate_age(2049, 1993)
print()
def calculate_age(current_year, birth_year):
    age = current_year-birth_year
    return age

dads_age= calculate_age(2049, 1953)
print()
my_age= 'X'
dads_age='Y'
print("I am "+my_age+ " years old and my dad is "+ dads_age+ " years old.")

print()
# Activity-8
print("Activity-8")
print()
def get_boundaries(target, margin):
    low_limit = target- margin
    high_limit = margin - target
    return low_limit, high_limit

low, high= get_boundaries(100, 20)
print(low)
print(high)
print()
# Activity-9
print('Activity9')
print()
current_year = 2048
def calculate_age(birth_year):
    age = current_year-birth_year
    return age

print(current_year)
print(calculate_age(1970))
print()
# Activity-10
print('Activity10')
print()
def repeat_stuff(stuff, num_repeats):
    return stuff*num_repeats

lyrics= repeat_stuff("Row", 3)+"Your Boat"
song = repeat_stuff(lyrics, 1)
print(song)
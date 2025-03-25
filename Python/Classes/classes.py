print("Activity-1")
#1
an_int = 5
print(type(an_int))
#2
my_dict = {}
print(type(my_dict))
#3
my_list = []
print(type(my_list))

print()
print("Activity-2")
class Facade:
    pass

print()
print("Activity-3")
facade_1 = Facade()

print()
print("Activity-4")
facade_1_type = type(facade_1)
print(facade_1_type)

print()
print("Activity-5")
class Grade:
    minimum_passing = 65
print(Grade.minimum_passing)

print()
print("Activity-6")
class Rules:
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."

rules = Rules()
print(rules.washing_brushes())

print()
print("Activity-7")
class Circle:
    pi = 3.14
    
    def calculate_area(self, radius):
        return radius*self.pi

circle = Circle()
area = circle.calculate_area(1)
print(area)

print()
print("Activity-8")
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        print(f"New circle with diameter: {self.diameter}")
    
    def calculate_area(self):
        radius = self.diameter / 2
        return Circle.pi * (radius ** 2)
    
teaching_table = Circle(36)
area = teaching_table.calculate_area()
print(area)

print()
print("Activity-9")
class Store:
    def __init__(self, store_name) -> None:
        self.store_name = store_name

alternative_rocks = Store("Alternative Rocks")
isabelles_ices = Store("Isabelle's Ice")

print(alternative_rocks.store_name)
print(isabelles_ices.store_name)

print()
print("Activity-10")
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for element in how_many_s:
    if hasattr(element, 'count'):
        s_count = element.count("s")
        print(s_count)

print()
print("Activity-11")
class Circle:
    pi = 3.14
    def __init__(self, diameter):
        self.radius = diameter / 2
        print("Creating circle with diameter {d}".format(d=diameter))
    
    def circumference(self):
        return 2 * Circle.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(f"Medium Pizza Circumference: {medium_pizza.circumference()}")
print(f"Teaching Table Circumference: {teaching_table.circumference()}")
print(f"Round Room Circumference: {round_room.circumference()}")

print()
print("Ativity-12")
def this_function_is_an_object(number):
    return number

print(this_function_is_an_object(5))

print()
print("Activity-13")
class Circle:
    pi = 3.14
    def __init__(self, diameter):
        self.radius = diameter / 2
    
    def area(self):
        return self.pi * self.radius ** 2
    
    def circumference(self):
        return self.pi * 2 * self.radius
    
    def __repr__(self) -> str:
        return f"Circle with radius {self.radius}"

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

print()
print("Activity-14")
class Student:
    def __init__(self, name, year) -> None:
        self.name = name
        self.year = year
        self.grades = []
    
    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)
    
    class Grade:
        minimum_passing = 65

    def __initsubclasses__(self, score):
        self.score = score

roger = Student("Roger van der  Weyden", 2009, 10)
print("Activity-1")
my_baby_bool= "true"
print(type(my_baby_bool))
my_baby_bool_two= True
print(type(my_baby_bool_two))

print()
print("Activity-2")
def dave_check(user_name):
    if user_name == "Dave":
        return "Get off my computer Dave!"
# Enter a user name here, make sure to make it a string
user_name = input("Enter your user name:")
print(dave_check(user_name))
print()
print("Improvised Version")
def dave_check(user_name):
    if user_name == "Dave":
        return "Get off my computer Dave!"
    if user_name == "angela_catlady_87" or "Angela Catlady":
        return "I know it is you Dave! Go away!"
# Enter a user name here, make sure to make it a string
user_name = input("Enter your user name:")
print(dave_check(user_name))

print()
print("Activity-3")
def greater_than(x, y):
    if x>y:
        return x
    elif x<y:
        return y
    elif x==y:
        return "These numbers are same."

print()
def graduation_reqs(credits):
    if credits>=120:
        return "You have enough credits to graduate."

print(graduation_reqs(120))
print()
print("Activity-4")
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
print(statement_one)
statement_two= (4 * 2 <= 8) and (7 - 1 == 6)
print(statement_two)

print()
def graduation_reqs(gpa, credits):
    if (gpa>=2) and (credits>= 120):
        return "You have enough credits to graduate."

print()
print("Activity-5")
statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
print(statement_one)
statement_two= (9 + 5 <= 15) or (7 != 4 + 3)
print(statement_two)

print()
def graduation_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"
print()
print("Activity-5")
statement_one = not (4 + 5 <= 9)
print(statement_one)
statement_two= not (8 * 2) != 20 - 4
print(statement_two)

print()
def graduation_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"
    if (gpa >= 2.0) and not (credits >= 120):
        return "You do not have enough credits to graduate."
    if not (gpa >= 2.0) and (credits >= 120):
        return "Your GPA is not high enough to graduate."
    else:
        return "You do not meet the GPA or the credit requirement for graduation."
print()
print("Activity-6")
def grade_converter(gpa):
    grade = ""
    if gpa == 4:
        grade = "A"
        return "Your grade is "+grade
    elif gpa == 3:
        grade= "B"
        return "Your grade is "+grade
    elif gpa == 2:
        grade = "C"
        return "Your grade is "+grade
    elif gpa == 1:
        grade = "D"
        return "Your grade is "+grade
    elif gpa == 0:
        grade = "F"
        return "Your grade is "+grade

print(grade_converter())
print()
print("Activity-7")
def raises_value_error():
    raise ValueError

try:
    raises_value_error()
except ValueError:
    print("You raised a ValueError")

print()
print("Activity-8")
def applicant_selector(gpa, ps_score, ec_count):
    if gpa>=3.0 and ps_score>=90 and ec_count>=3:
        return "This applicant should be selected."
    elif gpa>=3.0 and ps_score>=90 and ec_count<3:
        return "This spplicant should be given an in- person interview."    
    else:
        return "This applicant should be rejected."
print(applicant_selector(4.0, 95, 5))
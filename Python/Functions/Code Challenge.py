# Activity1
print("Activity-1")
print()
def average(num1, num2):
    average = (num1+ num2)/2
    return average
print(average(1,-1))
print()
# Activity2
print("Activity-2")
print()
def tenth_power(num):
    power = num**10
    return power
print(tenth_power(1))
print(tenth_power(0))
print(tenth_power(2))
print()
# Activity-3
print("Activity-3")
print()
def introduction(first_name, last_name):
    intro = last_name+ ", "+ first_name+" "+ last_name 
    return intro

print(introduction("James", "Bond"))
print(introduction("Maya", "Angelou"))
print()
# Activity-4
print("Activity-4")
print()
def square_root(num):
    root = num**0.5
    return root

print(square_root(16))
print(square_root(100))
print()
# Activity-5
print("Activity-5")
print()
def tip(total, percentage):
    amount = total*(percentage/100)
    return amount

print(tip(10, 25))
print(tip(0, 100))
print()
# Activity-6
print("Activity-6")
print()
def win_percentage(wins, losses):
    win= wins/ (wins+losses) * 100
    return win

print(win_percentage(5, 5))
print(win_percentage(10, 0))
print()
# Activity-7
print("Activity-7")
print()
def first_three_multiples(num):
    first = num*1
    second= num*2
    third = num*3
    return first, second, third

print(first_three_multiples(7))
print()
# Activity-8
print('Activity-8')
print()
def dog_years(name, age):
    dog_age= age*7
    return name+",you are "+str(dog_age)+" years old in dog years."
    

print(dog_years("Om", 14))

print()
# Activity-9
print("Activity-9")
print()
def remainder(num1, num2):
    rem= (2*num1)%(num2*(1/2))
    return rem

print(remainder(15, 14))
print(remainder(9, 6))

print()
# Activity-10
print("Activity-10")
print()
def lots_of_math(a,b,c,d):
    sum= a+b
    sub= c-d
    mul= sum*sub
    mod= mul%a
    print(sum)
    print(sub)
    print(mul)
    return mod

print(lots_of_math(1, 1, 1, 1))


print("Activity-1")
def divisible_by_ten(nums):
    count = 0
    for i in nums:
        if i % 10 == 0:
            count = count + 1
    return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

print()
print("Activity-2")
def add_greetings(names):
    greeting = []
    for name in names:
        greet = "Hello "+ name
        greeting.append(greet)
    return greeting

print(add_greetings(["Owen", "Max", "Sophie"]))

print()
print("Activity-3")
def delete_starting_evens(lst):
    while(len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return lst
            
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))

print()
print("Activity-4")
def odd_indices(lst):
    for i in range(len(lst)):
        if i % 2 != 0:
            print(lst[i])

print(odd_indices([4, 3, 7, 10, 11, -2]))

print()
print("Activity-5")
def exponents(bases, powers):
    a = []
    for i in bases:
        for j in powers: 
            a.append(i**j)         
    print(a)

exponents([2, 3, 4], [1, 2, 3])

print()
print("Acitivty-6")
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for num in lst1:
        sum1 = sum1 + num
    # do same for lst 2
    for num in lst2:
        sum2 = sum2 + num
    if sum1 > sum2:
        return lst1
    elif sum1 < sum2:
        return lst2
    else:
        return lst1

print(larger_sum([1, 9, 5], [2, 3, 7]))

print()
print("Activity-7")
def over_nine_thousand(lst):
    total_sum = 0
    for num in lst:
        total_sum +=  num
        if total_sum > 9000:
            return total_sum
    return 0 if total_sum > 9000 else 0

print(over_nine_thousand([8000, 900, 120, 5000]))

print()
print("Activity-8")
def max_num(nums):
    i = max(nums)
    return f"The largest number is {i}"

print(max_num([50, -10, 0, 75, 20]))

print()
print("Activity-9")
def same_values(lst1, lst2):
    a = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            a.append(i)
    return a

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

print()
print("Activity-10")
def reversed_list(lst1, lst2):
    a = []
    for i in range(len(lst1)):
        if lst1[i] != lst2[len(lst2)-1-i]:
            return False
    return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
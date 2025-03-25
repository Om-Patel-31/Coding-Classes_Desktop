import random # Activity-2
from datetime import datetime# Activity 1
from matplotlib import pyplot as plt # Activity-3
from decimal import Decimal #Activity-4
from library import always_three #Activity-5

print("Activity-1")
current_time = datetime.now()
print(current_time)

print()
print("Activity-2")
random_list = [random.randint(1,100) for _ in range(101)]

randomer_number = random.choice(random_list)

print(randomer_number)

print()
print("Activity-3")
numbers_a = range(1,13)
numbers_b = random.sample(range(1000), 12)
plt.plot(numbers_a, numbers_b)
plt.show()

print()
print("Activity-4")
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)
four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

print()
print("Activity-5")
result = always_three()
print(result)
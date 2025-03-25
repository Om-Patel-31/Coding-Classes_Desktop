def ground_shipping(weight):
    cost = weight*4+20
    return "The cost for ground shipping would be $"+ str(cost)

premium_ground_shipping = 125

def drone_shipping(weight):
    cost = weight*4.5+0
    return "The cost for drone shipping would be $"+ str(cost)

def shipping(weight):
    weight = weight
    print(ground_shipping(weight))
    print(drone_shipping(weight))
    return "The cost for premium ground shipping would be $" + str(premium_ground_shipping)

print(shipping(4.8))
print()
print(shipping(41.5))
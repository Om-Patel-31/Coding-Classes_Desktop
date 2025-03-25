# Sample test code

# Define a test function for each of the functions
def test_function(fn):
    if fn.__name__ == "calculate_shipping_cost":
        test_shipping(fn)
    elif fn.__name__ == "calculate_driver_cost":
        test_driver(fn)
    elif fn.__name__ == "calculate_money_made":
        test_money(fn)

# Define a test for calculate_shipping_cost
def test_shipping(f):
    try:
        costs = f((0, 0), (1, 1))
    except TypeError:
        print("calculate_shipping_cost() did not provide default argument for shipping_type")
        return
    if not isinstance(costs, str):
        print("calculate_shipping_cost() did not format the result in a string")
        return
    if costs != "$1.04":
        print(f"calculate_shipping_cost((0, 0), (1, 1)) returned {costs}. Expected result is $1.04")
        return
    print("OK! calculate_shipping_cost() passes tests")

# Define a driver class for testing
class Driver:
    def __init__(self, speed, salary):
        self.speed = speed
        self.salary = salary

    def __repr__(self):
        return f"Nile Driver speed {self.speed} salary {self.salary}"

driver1 = Driver(2, 10)
driver2 = Driver(7, 20)

# Define a test for calculate_driver_cost
def test_driver(f):
    try:
        price, driver = f(80, driver1, driver2)
    except TypeError:
        print("calculate_driver_cost() doesn't expect multiple driver arguments")
        return
    if not isinstance(driver, Driver):
        print("calculate_driver_cost() did not return driver")
        return
    if price != 1600:
        print(f"calculate_driver_cost() did not provide correct final price (expected {price}, received 1600)")
        return
    if driver is not driver1:
        print("calculate_driver_cost() did not provide least expensive driver")
        return
    print("OK! calculate_driver_cost() passes tests")

# Define a trip class for testing
class Trip:
    def __init__(self, cost, driver, driver_cost):
        self.cost = cost
        driver.cost = driver_cost
        self.driver = driver

trip1 = Trip(200, driver1, 15)
trip2 = Trip(300, driver2, 40)

# Define a test for calculate_money_made
def test_money(f):
    try:
        money = f(UEXODI=trip1, DEFZXIE=trip2)
    except TypeError:
        print("calculate_money_made() doesn't expect multiple trip keyword arguments")
        return
    if not isinstance(money, (int, float)):
        print("calculate_money_made() did not return a number")
        return
    if money != 445:
        print(f"calculate_money_made() did not provide correct final price (expected {money}, received 445)")
        return
    print("OK! calculate_money_made() passes tests")
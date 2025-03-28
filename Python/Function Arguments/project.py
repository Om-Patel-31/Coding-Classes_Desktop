from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Function to calculate shipping cost
def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
    from_lat, from_long = from_coords
    to_lat, to_long = to_coords
    distance = get_distance(from_lat, from_long, to_lat, to_long)
    shipping_rate = SHIPPING_PRICES.get(shipping_type, SHIPPING_PRICES['Overnight'])
    price = distance * shipping_rate
    return format_price(price)

# Function to calculate the cheapest driver cost
def calculate_driver_cost(distance, *drivers):
    cheapest_driver = None
    cheapest_driver_price = None
    for driver in drivers:
        driver_time = driver.speed * distance
        price_for_driver = driver.salary * driver_time
        if cheapest_driver is None or price_for_driver < cheapest_driver_price:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
    return cheapest_driver_price, cheapest_driver

# Function to calculate total money made
def calculate_money_made(**trips):
    total_money_made = 0
    for trip_id, trip in trips.items():
        trip_revenue = trip.cost - trip.driver.cost
        total_money_made += trip_revenue
    return total_money_made

# Run the tests
test_function(calculate_shipping_cost)
test_function(calculate_driver_cost)
test_function(calculate_money_made)
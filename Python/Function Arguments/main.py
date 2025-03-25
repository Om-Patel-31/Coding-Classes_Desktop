print("11.1.1")
print("The parameter is album.")

print()
print("11.1.2")
from review_lib import get_next_review, submit_review
review = get_next_review()
if not review is None:
    submit_review(review)

print()
print("11.1.3")
prints_return = print("Hi")
print(prints_return)
sort_this_list = [14, 631, 4, 51358, 50000000]
list_sort_return = sort_this_list.sort()
print(list_sort_return)
print(sort_this_list)

print()
print("11.1.4")
import os
def make_folders(folders_list=False, nest=False):
    if nest:
        """
        Nest all the folders, like
        ./Music/fun/parliament
        """
    path_to_new_folder = ""
    for folder in folders_list:
        path_to_new_folder += "/{}".format(folder)
        try:
            os.makedirs(path_to_new_folder)
        except FileExistsError:
            continue
    else:
        """
        Makes all different folders, like
        ./Music/ ./fun/ and ./parliament/
        """
        for folder in folders_list:
            try:
                os.makedirs(folder)
            except FileExistsError:
                continue
    make_folders()
    
# print()
# print("11.1.5")
# import requests
# from bs4 import BeautifulSoup
# def get_id(html_id, website="http://coolsite.com"):
#     request = requests.get(website)
#     parsed_html = BeautifulSoup(website.content, features="html.parser")
#     return parsed_html.find(id_=html_id)

# print()
# print("11.1.6")
# import shapes
# def draw_shape(shape_name="box", character="x", line_breaks=True):
#     shape = shapes.draw_shape(shape_name, character)
#     if not line_breaks:
#         print(shape[1:-1])
#     else:
#         print(shape)
        
print()
print("11.1.7")
def update_order(new_item, current_order=[]):
    current_order.append(new_item)
    return current_order

# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)
# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})
print(order2)

print()
print("11.1.8")
def update_order(new_item, current_order=None):
    if current_order is None:
        current_order = []
    current_order.append(new_item)
    return current_order

# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)
# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})
# What's in that second order again?
print(order2)

print()
print("11.1.9")
def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper

the_scream = scream_and_whisper("Hi")
the_whisper = scream_and_whisper("Salut")
print(the_scream)
print(the_whisper)

print()
print("11.1.10")
from os.path import join
path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

def myjoin(*args):
    for arguments in args:
        joined_strings = ','.join(arguments)
    print(joined_strings)
    
myjoin([path_segment_1,path_segment_2,path_segment_3])

# print()
# print("11.1.11")
# # Checkpoint 1
# print("My name is {name} and I'm feeling {feeling}.".format(
# # add your arguments to .format()
#       name="Om", feeling="Happy"
# ))
# # Checkpoint 2
# from products import create_product
# # Update create_products() to take arbitrary keyword arguments
# def create_products(**kwargs):
#     for name, price in kwargs.items():
#         create_product(name, price)
# # Checkpoint 3
# # Update the call to `create_products()` to pass in this dictionary as a series of keyword
# create_products({
# 'Baseball': '3',
# 'Shirt': '14',
# 'Guitar': '70',
# })

print()
print("11.1.12")
def remove(filename, *args, **kwargs):
    with open(filename,'r') as file_obj:
        text = file_obj.read()
    
    for arg in args:
        text = text.replace(arg, "")
    
    for kwarg, replacement in kwargs.items():
        text = text.replace(kwarg, replacement)
    
    return text

print(remove("C:\\Users\\om31d\\OneDrive\\Coding Classes\\Python\\Function Arguments\\text.txt","generous", "gallant", fond="amused by", Robin="Mr. Robin"))

# print()
# print("11.1.13")
# from products import create_product
# def create_products(**products_dict):
#     for name, price in products_dict.items():
#         create_product(name, price)
# new_product_dict = {
# 'Apple': 1,
# 'Ice Cream': 3,
# 'Chocolate': 5,
# }
# # Call create_product() by passing new_product_dict as kwargs!
# create_products(**new_product_dict)
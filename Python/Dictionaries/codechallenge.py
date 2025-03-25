print("Activity-1")
def sum_values(my_dictionary):
    x = 0
    for val in my_dictionary.values():
        x += val
    return x
    
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
print(sum_values({10:1, 100:2, 1000:3}))

print()
print("Activity-2")
def sum_even_keys(my_dictionary):
    x = 0
    for key, value in my_dictionary.items():
        if key % 2 == 0:
            x += value
    return x

print(sum_even_keys({1:5, 2:2, 3:3}))
print(sum_even_keys({10:1, 100:2, 1000:3}))

print()
print("Activity-3")
def add_ten(my_dictionary):
    for key, value in my_dictionary.items():
        value += 10
        my_dictionary[key] = value
    return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
print(add_ten({10:1, 100:2, 1000:3}))

print()
print("Activity-4")
def values_that_are_keys(my_dictionary):
    value_keys = []
    for value in my_dictionary.values():
        if value in my_dictionary:
            value_keys.append(value)
    return value_keys
        
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))

print()
print("Activity-5")
def max_key(my_dictionary):
    largest_key = float("-inf")
    largest_value = float("-inf")
    for key, value in my_dictionary.items():
        if value > largest_value:
            largest_value = value
            largest_key = key
    return largest_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
print(max_key({"a":100, "b":10, "c":1000}))

print()
print("Activity-6")
def word_length_dictionary(words):
    word_len_dict = {}
    for word in words:
        word_len_dict[word] = len(word)
    return word_len_dict
        
print(word_length_dictionary(["apple", "dog", "cat"]))
print(word_length_dictionary(["a", ""]))


print()
print("Activity-7")
def frequency_dictionary(words):
    dict = {}
    for word in words:
        if word in dict:
            dict[word] +=1
        else:
            dict[word] = 1
    return dict
    
print(frequency_dictionary(["apple", "apple", "cat", 1]))
print(frequency_dictionary([0,0,0,0,0]))

print()
print("Activity-8")
def unique_values(my_dictionary):
    unique_values_list = []
    for value in my_dictionary.values():
        if value not in unique_values_list:
            unique_values_list.append(value)
    return len(unique_values_list)

print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))

print()
print("Activity-9")
def count_first_letter(names):
    result={}
    for last_name, first_names in names.items():
        first_letter = last_name[0]
        if first_letter in result:
            result[first_letter] += len(first_names)
        else:
            result[first_letter] = len(first_names)
    return result
            
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
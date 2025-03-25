print("Activity-1")
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
    unique_letters = []

    for char in word:
        if char in letters and char not in unique_letters:
            unique_letters.append(char)
    
    return len(unique_letters)

print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))

print()
print("Activity-2")
def count_char_x(word, x):
    count = 0
    for y in word:
        if x == y:
            count +=1
    return count

print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))

print()
print("Activity-3")
def count_multi_char_x(word, x):
    y = word.split(x)
    return (len(y)-1)

print(count_multi_char_x("mississippi", "iss"))

print()
print("Activity-4")
def substring_between_letters(word, start, end):
    start_index = word.find(start)
    end_index = word.find(end)
    if start_index != -1 and end_index != -1:
        return word[start_index + 1:end_index]
    else:
        return word

print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))

print()
print("Activity-5")
def x_length_words(sentence, x):
    word = sentence.split()
    for char in word:
        if len(char) >= x:
            return True
        else:
            return False

print(x_length_words("i like apples", 2))
print(x_length_words("alex likes apples", 2))

print()
print("Activity-6")
def check_for_name(sentence, name):
    words = sentence.split()
    for word in words:
        if name.lower() in sentence.lower():
            return True
        if not name.lower() in sentence.lower():
            return False

print(check_for_name("My name is Jamie", "jamie"))
print(check_for_name("My name is jamie", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))

print()
print("Activity-7")
def every_other_letter(word):
    every_other=""
    for i in range(0,len(word),2):
        every_other += word[i]
        return every_other
    
print(every_other_letter("Coders"))

print()
print("Activity-8")
def reverse_string(word):
    # return word[::-1]
    reversed_string = ""
    for char in word:
        reversed_string = char + reversed_string
    return reversed_string

print(reverse_string("Ultimate"))
print(reverse_string("Hello world!"))
print(reverse_string(""))

print()
print("Activity-9")
def make_spoonerism(word1, word2):
    newword1 = word2[0] + word1[1:]
    newword2 = word1[0] + word2[1:]
    return newword1 + " " + newword2

print(make_spoonerism("Ultimate", "Coders"))
print(make_spoonerism("Hello", "world!"))
print(make_spoonerism("a", "b"))

print()
print("Activity-10")
def add_exclamation(word):
    while len(word) < 20:
        word += "!"
    return word

print(add_exclamation("UltimateCoders"))
print(add_exclamation("UltimateCoders is the best place to learn"))
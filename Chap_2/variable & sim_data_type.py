# variables

message = "Hello World!"
# print(message)

message = "Hello Py crash course"
# print(message)

#strings

nar = "naresh barua"
#print(nar.title()) #title
#print(nar.upper()) #uppercase
#print(nar.lower()) #lowercase

first_name = "naresh"
last_name = "barua"
full_name = f"{first_name} {last_name}"
# print(full_name)
# print(f"Hello, {full_name.title()}!") # f-string
# message = f"hello, {full_name.title()}!"
# print(message)

# print("Python")
# print("\tPython\tpython\tpython")
# print("Lang:\n\tPython\n\tC\n\tJava")

# String examples

# Concatenation
# greeting = "Hello" + " " + "World"
# print(greeting)

# String methods
# text = "python programming"
# print(text.capitalize())
# print(text.replace("python", "Java"))
# print(text.find("programming"))
# print(len(text))

# String slicing
# word = "Hello"
# print(word[0])
# print(word[1:4])
# print(word[-1])

# String formatting
# age = 25
# name = "Alice"
# print(f"{name} is {age} years old")
# print("{} is {} years old".format(name, age))

# rstrip() lstrip()

# txt = " hello "
# x = txt.rstrip()
# print(x)

# txt = "Hello,,,,,,,,,,ssiqq......"
# x = txt.rstrip(",.qis")
# print(x)

# url = 'https://naresh_barua.com'
# U = url.removeprefix('https://').removesuffix('.com')
# print(U)

# More variable examples

# Integer variables
age = 25
year = 2024
count = 0

# Float variables
price = 19.99
temperature = 98.6
pi = 3.14159

# Boolean variables
is_active = True
is_valid = False
has_error = True

# Multiple assignment
x, y, z = 10, 20, 30
# print(x, y, z)

# Swapping variables
a = 5
b = 10
a, b = b, a
# print(f"a = {a}, b = {b}")

# Type checking
# print(type(age))
# print(type(price))
# print(type(is_active))

# Constants (by convention, use uppercase)
MAX_ATTEMPTS = 3
MIN_PASSWORD_LENGTH = 8
PI_VALUE = 3.14159
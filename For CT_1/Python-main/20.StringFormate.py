# str.format() = optional method that gives user more control when displaying output
animal = 'cow'
item = 'moon'

print("The " + animal + " jump " + "over the " + item)  # normal way
print("The {} jump over the {}".format(animal, item))
print("The {1} jump over the {0}".format(animal, item))  # positional argument
print("The {animal} jump over the {road}".format(road="road", animal="dog"))

text = "I love the {} who is {}"
print(text.format("person", "good"))

num1 = 5
num2 = 5
print("Sum of {} and {} are 10".format(num1,num2))

# add padding
print("Hello, I'm {:^5} years old".format("23")) # middle padding
print("Hello, I'm {:<5} years old".format("23")) # right padding
print("Hello, I'm {:>5} years old".format("23")) # left padding
print("Hello, I'm {age:<5} years old".format(age = "23"))

# showing number
pi = 3.1415
print("The pi value is {:.2f}".format(pi)) # 2 digit in decimal
num = 1000
print("The value is {:,}".format(num)) # adding comma
print("The binary value is {:b}".format(num)) # binary
print("The octal value is {:o}".format(num)) # octal
print("The hexadecimal value is {:x}".format(num)) # hexadecimal
print("The number is {:e}".format(num)) # scientific notation

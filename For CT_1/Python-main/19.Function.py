# without parameter
def hello():
    print("Hello world")
    print("Have a nice day")

# hello()
# hello()
# hello()

# with parameter
def hello(name):
    print("Hello "+name)

# hello("Mahbub")

# with two different parameter
def hello(name, time):
    print("Hello "+name)
    print("I saw you " + str(time) + " times")


# name = "Riana"
# time = 5
# hello(name, time)

# return statement
def multiply(num1, num2):
    return num1 * num2

# x = multiply(7,8)
# print("The result:"+str(x))

# keyword argument = order of the argument does not matter
def info(animal, name):
    print("Hello " + name + " You love " + animal)

# info(name="Mahbub", animal="Dog")

# nested function call
# print(round(abs(float(input("Enter a number:")))))
    
# *args = parameter that will pack all argument into a tuple
# we can send multiple value to one parameter. it will make tuple of all argument
def sumNum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# print(sumNum(1, 2, 3, 4, 5))


# **kwargs = parameter that will pack all argument in to dictionary
def hello(**kwargs):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(first = "Mahbubur", middle = "and", last = "Rahman")

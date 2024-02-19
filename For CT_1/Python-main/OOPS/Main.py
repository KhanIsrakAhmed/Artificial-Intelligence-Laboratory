from car import Car

# basic of OOPS
car1 = Car("Chevy", "Corvette", 2021, "blue") # create object
print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)
car1.drive()
car1.buy()
print()

print(car1.wheel)
car1.wheel = 10  # change using object, this will change only for that object
print(car1.wheel)
Car.wheel = 20  # change using class name, this will change for whole object we will create
print(Car.wheel)

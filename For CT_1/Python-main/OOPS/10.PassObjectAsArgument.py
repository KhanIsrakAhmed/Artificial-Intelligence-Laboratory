class Car:
    color = None


class Bike:
    color = None

# we can change any attribute of class using function
def changeColor(object, color): # (object, parameter)
    object.color = color


car1 = Car()
car2 = Car()
car3 = Car()

bike1 = Bike()

changeColor(car1, "red")
changeColor(car2, "cream")
changeColor(bike1,"black")

print(car1.color)
print(car2.color)
print(car3.color)

print(bike1.color)

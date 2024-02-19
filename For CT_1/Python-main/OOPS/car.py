class Car:
    wheel = 4 # class variable

    def __init__(self, make, model, year, color): # this is constructor
        self.make = make # instance variable
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopped")

    def buy(self):
        print("I will buy {} {} oneday".format(self.make,self.model))

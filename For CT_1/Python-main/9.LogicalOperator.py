temp = int(input("what is the temperature today: "))

if temp >=0 and temp <= 30:
    print("Temperature is good")
    print("Go out side!")

elif temp <0 or temp > 30:
    print("Temperature is bad")
    print("Don't go outside")

# use of not operator
num = int(input("Enter a number: "))

if not (num == 100):
    print("You enter a wrong number")
else:
    print("Yeah! that's the right number")

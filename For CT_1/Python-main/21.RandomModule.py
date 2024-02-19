# random = pick a random thing
import random

x = random.randint(1, 6)  # integer (from, to)
print(x)
y = random.random()  # float from 0 to 1
print(y)

myList = ["Rock", "Paper", "Scissors"]
z = random.choice(myList)
print(z)

# shuffle something
cards = [1, 2, 3, 4, 5, 6, 8, 9, "K", "Q", "J", "A"]
random.shuffle(cards)
print(cards)

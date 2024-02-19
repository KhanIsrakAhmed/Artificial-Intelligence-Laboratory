food = ["pizza", "Hamburger", "Hotdog", "Spaghetti"]
food[0] = "sushi"

for i in food:
    print(i, end=" ")
print()

# some function in list
food.append("Ice cream")  # append in list
food.remove("sushi")  # remove element
food.pop()  # remove last element
food.insert(0, "Cake")  # insert value in using index
food.sort()  # sort the list
food.clear()

for i in food:
    print(i, end=" ")
print()

# take integer as input
num = []

for i in range(int(input("Enter size:"))):
    num.append(int(input()))

for i in range(0, len(num)):
    print(num[i], end=" ")

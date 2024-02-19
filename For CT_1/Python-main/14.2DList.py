drinks = ["coffee","soda", "tea"]
dinner = ["pizza", "hamburger","hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks,dinner,dessert]

print(food[1][2])

# take integer as input
raw = int(input())
col = int(input())

matrix = []

for i in range(raw):
    a = []
    for j in range(col):
        a.append(int(input()))
    matrix.append(a)

for i in range(raw):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()

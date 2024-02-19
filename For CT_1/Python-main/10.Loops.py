# while loop
name = ""
while len(name) == 0:
    name = input("Enter your name: ")
print("Hello " + name)

# For loop
for i in range(10):
    print(i+1)

for i in range(50,100+1):
    print(i)

for i in range(50, 100+1, 2):
    print(i)

for i in range(20, 12, -1):
  print(i, end=' ')

name = "Mahbubur Rahman"
for i in name:
    print(i)

# timer with for loop
import time
for second in range(10, 0, -1):
    print(second)
    time.sleep(1)
print("Hello mother fucker!")
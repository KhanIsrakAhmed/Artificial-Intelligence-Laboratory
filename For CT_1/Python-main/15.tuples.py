# we can store multiple value in one variable
student = ("Mahbub", 21, "Male", "Mahbub")
print(student)

# Function
print(student.count("Mahbub")) # find the frequency
print(student.index(21)) # find index of certain value

for x in student:
    print(x,end=" ")
print()

# /important
if "Mahbub" in student:
    print("Yes! He is here") 
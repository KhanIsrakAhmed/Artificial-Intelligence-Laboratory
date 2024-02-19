# set = collection which is unordered, un-indexed, no duplicate value
utensil = {"fork", "spoon", "knife", "spoon"}

for x in utensil:
    print(x , end= " ")
print()

# some useful function
utensil.add("napkin")
utensil.remove("fork")
utensil.clear()

dishes = {"bowl", "plate", "cup","fuck"}
utensil.update(dishes) # update the value with the existence value
dinnerTable = utensil.union(dishes) # this is union of two set

for x in utensil:
    print(x, end=" ")
print()

for x in dinnerTable:
    print(x, end=" ")
print()


num = {1,2,4,6,8}
prime = {2,3,5,7,13}

# More function
print(num.difference(prime)) # find the difference between tow sets
print(num.intersection(prime)) # find the common element
import shutil
import os

path = "S:\\Coding Arena\\Skills\\Python\\File.txt"
# path = "S:\\Coding Arena\\Skills\\Python\\Folder"

if os.path.exists(path): # path existence check
    print("Location exist and", end=" ")

    if os.path.isfile(path): # file check
        print("That is a file")

    if os.path.isdir(path): # folder check
        print("That is a folder/directory")
else:
    print("Location dest'nt exist")

# read from file
try:
    with open(path) as file:
        print(file.read())
except:
    print("File is not available")

# write into file
text = "Have a nice day.\nSee you!"
try:
    with open(path, 'a') as file:  # we can use 'w', 'r', 'a' according to our need
        file.write(text)
except Exception as e:
    print(e)

# copy, move, delete
source = path
destination = "S:\\Coding Arena\\Skills\\Python\\NewFile.txt"

# copy
shutil.copy(source, destination)
# move
os.replace(source,destination)
# delete
os.remove(destination)
os.rmdir("Location")  # delete directory which is empty
shutil.rmtree("Location") # delete directory Entirely

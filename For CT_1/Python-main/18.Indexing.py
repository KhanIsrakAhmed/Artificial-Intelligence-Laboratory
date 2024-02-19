# indexing operator [] = give access to sequence element (str,list,tuple)
name = "bro code!"

if name[0].islower():
    name = name.capitalize()

print(name)

firstName = name[0:3].upper()
lastName = name[4:].lower()
lastCharacter = name[-1]

print(firstName)
print(lastName)
print(lastCharacter)

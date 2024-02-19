# dictionary = A changeable, unordered, collection of unique key:value pairs, just like map in cpp

capitals = {"usa": "washington DC",
            "bangladesh": "dhaka",
            "india": "new delhi",
            'russia': 'moscow'}

# Some function
# print(capitals["india"])
# print(capitals.get('germany')) # if key does not have in dictionary
# print(capitals.keys()) # print only keys
# print(capitals.values()) # print only values
# print(capitals.items()) # print key along with value

# More function
capitals.update({"germany": "berlin"})  # add value
capitals.update({"usa": "los vegas"})  # update value
capitals.pop('india')

# print using for loop
for key,value in capitals.items():
    print(key,value)
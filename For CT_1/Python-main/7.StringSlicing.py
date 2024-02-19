# name[start: end: step]

name = "Mahbubur Rahman"
firstName = name[0:8]
# firstName = name[:8]

lastName = name[9:16]
# lastName = name[9:]

step = name[0:8:2]
# step = name[::2]

reverse = name[:: -1]  # reverse a string

# use of slice function
website = "http://google.com"
slice = slice(7, -4)

print(website[slice])
'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    17-02-2024     *************************  '''


def printInfo(name, age='N/A', cgpa='N/A'):
    print(f'Name: {name}, Age: {age}, CGPA: {cgpa}')


printInfo("Mr.Z", 35, 3.87)
printInfo("Mr.Z", 35)
printInfo("Mr.Z")


# Keyword/Named Arguments
def printInfo(name, age, cgpa='N/A'):
    print(f'Name: {name}, Age: {age}, CGPA: {cgpa}')


printInfo(age=35, cgpa=3.87, name="Mr.Z")
printInfo(age=35, name="Mr.Z")
# printInfo()

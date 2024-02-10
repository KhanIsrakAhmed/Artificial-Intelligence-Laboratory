'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    10-02-2024     *************************  '''

class Student:
  def __init__(self, fname, lname, cgpa, age):
    self.first_name = fname
    self.last_name = lname
    self.cgpa = cgpa
    self.age = age

  def printFullName(self):
    print(self.first_name + ' ' + self.last_name)

obj = Student("Mr.", "Z", 3.88, 45)
obj.printFullName()
print(obj.age)

obj.first_name = "Ms."
obj.printFullName()
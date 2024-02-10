'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    10-02-2024     *************************  '''

def squarefun(x):
    return x*x

y= int(input("Enter : "))

z= squarefun(y)
print("Square of ",y, "is",z)
print()

def isPrime(x):
    for i in range(2, x):
     if x%i==0:
      return False
     return True

a= isPrime(z)
if a==True:
    print(z,"is Prime")
else:
    print(z,"is not Prime")


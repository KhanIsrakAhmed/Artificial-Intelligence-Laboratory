'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    11-02-2024     *************************  '''

def factorial(num):
    ans = 1
    for i in range(1, num+1):
        ans *= i
    print(f'Fact of {num} is', ans)

num = int(input("Enter terms: "))
factorial(num)


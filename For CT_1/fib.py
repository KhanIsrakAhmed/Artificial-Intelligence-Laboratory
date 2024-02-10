'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    11-02-2024     *************************  '''

# def fibonacci(n):
#     if n <= 0:
#         return "Invalid input. Please provide a positive integer."
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib_sequence = [0, 1]
#         for i in range(2, n):
#             fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#         return fib_sequence

# n = int(input("Enter : "))
# print(fibonacci(n))


# def fibonacci_up_to_number(num):
#     a, b = 0, 1
#     fib_sequence = [a]
#     while b <= num:
#         fib_sequence.append(b)
#         a, b = b, a + b
#     return fib_sequence

# num =  int(input("Enter : "))
# print(fibonacci_up_to_number(num))

def fib(index):
    a = 0
    b = 1
    for i in range(0, index):
        if(i==0):
            print(a,end=' ')
        elif i==1:
            print(b,end=' ')
        else:
            print(a + b, end=' ')
            b = a+b
            a = b-a


index = int(input("Enter terms: "))

fib(index)

'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    10-02-2024     *************************  '''

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

n = int(input("Enter : "))
print(fibonacci(n))


def fibonacci_up_to_number(num):
    a, b = 0, 1
    fib_sequence = [a]
    while b <= num:
        fib_sequence.append(b)
        a, b = b, a + b
    return fib_sequence

num =  int(input("Enter : "))
print(fibonacci_up_to_number(num))

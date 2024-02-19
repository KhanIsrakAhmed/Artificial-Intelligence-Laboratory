'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    17-02-2024     *************************  '''


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


isPrime(73)
isPrime(86)

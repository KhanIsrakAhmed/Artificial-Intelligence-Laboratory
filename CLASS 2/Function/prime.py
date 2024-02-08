def isprime(x):
    if x <= 1:
        # print("Not prime")
        return False
    for i in range(2, x):
        if x % i == 0:
            # print("Not prime")
            return False
    # print("Is prime")
    return True

y = int(input("Enter a number: "))
isprime(y)

 
try:
    numerator = int(input("Enter numerator:"))
    denominator = int(input("Enter denominator:"))
    print(numerator/denominator)

except ZeroDivisionError:
    print("You can not divide number by zero")
except ValueError as e:
    print(e)
    print("Enter only number Please :)")

except Exception: # accept all the error
    print("Something went wrong :(")

else:
    print("We did'nt find any error")

finally:
    print("Operation successful")
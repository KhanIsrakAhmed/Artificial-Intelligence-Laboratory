'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    05-02-2024     *************************  '''

# take an integer and check whether that is a leap year or not


def is_leap_year(year):
    # Leap years are divisible by 4
    # Except for years divisible by 100, unless they are also divisible by 400

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year_to_check = int(input("Enter a year: "))

if is_leap_year(year_to_check):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")

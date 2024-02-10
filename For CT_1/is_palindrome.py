'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    11-02-2024     *************************  '''


word = input("Enter value: ")

is_palindrome = True
for i in range(0, len(word)//2):  #integer division 
    if word[i] != word[len(word) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("NOT Palindrome")



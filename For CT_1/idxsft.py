'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    10-02-2024     *************************  '''

def shift_ele(lst, i, shift):
    if shift == 0:
        return lst

    new_idx = (i + shift) % len(lst)
    lst.insert(new_idx, lst.pop(i))

    return lst


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)
idx = 0
shift_amount = 5
result = shift_ele(my_list, idx, shift_amount)
print(result) 

'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    10-02-2024     *************************  '''


list_int = [3, 4, 3, 0, 1, 3, 3, 4, 2, 7, 8, 7]

count_dict = {}


for v in list_int:
  if v in count_dict:
    count_dict[v] += 1
  else:
    count_dict[v] = 1

print(count_dict)

print(max(list_int))

print(min(list_int))
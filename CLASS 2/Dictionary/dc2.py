'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    17-02-2024     *************************  '''


name_dict = {
    "joseph": 3.85,
    "alex": 3.2,
    "john": 3.9,
    "jane": 3.5
}

for k in name_dict.keys():
    print(k, '->', name_dict[k])

for k, v in name_dict.items():
    print(k, '->', v)

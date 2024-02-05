'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    05-02-2024     *************************  '''

for i in range(1, 100):
  if i%3==0 and i%5!=0:
    print(i, end=' ')
    
for i in range(1, 100):
  if i%3==0:
    print(i, end=' ')

print()
for i in range(3, 100, 3):
  print(i, end=' ')
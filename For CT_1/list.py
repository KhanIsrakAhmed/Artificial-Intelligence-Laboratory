'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    05-02-2024     *************************  '''

list1 = [5,58,60,99,5,7]
print("LENGTH", len(list1))
print (list1)
for i in range (len(list1)):
    print (list1[i], end=' ')
print()
print("ex 2--------------------------------") 
list1.append(69)
print("LENGTH", len(list1))
print (list1)
for i in range (len(list1)):
    print (list1[i], end=' ')
print()

list1.insert(2,44)

print("LENGTH", len(list1))
print (list1)
list1.remove(99)
print("LENGTH", len(list1))
print (list1)

print("ex 3--------------------------------") 
sublist= list1[2:5]
print (sublist)
print (list1[2])
print (list1[5])
list1.remove(5)
list1.sort()
print (list1)
list1.sort(reverse= True)
print (list1)

print("ex 4--------------------------------") 
list2 = [10,11,-5]
list3 = [5, -6, 1]
# print(list2 + list3)
list2.extend(list3)
print(list2)

# use of break
for i in range(100):
    print(i)
    if i == 10:
        break

#use of continue
number = "017-441-77-620"
for i in number:
    if(i == "-"):
        continue
    else:
        print(i, end = "")

#use of pass
for i in range(1,11):
    if(i == 5):
        pass # it just pass the value
    else: 
        print(i, end = " ")

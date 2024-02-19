raw = int(input("Enter raw:"))
col = int(input("Enter column:"))
symbol = input("Enter symbol:")

for i in range(raw):
    for j in range(col):
        print(symbol, end="")  # prevent new line (end == "")
    print()


mahbub = "Mahbub"
tamanna = "Tamanna"
print(mahbub, end=" " + tamanna)

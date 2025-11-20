n = int(input("Enter any number : "))
list = []
for value in range(1, n+1):
    if(value % 2 == 0):
        list.append(value)

print(list)
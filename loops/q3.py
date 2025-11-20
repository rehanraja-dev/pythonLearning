n = int(input("Enter any number to print it's table : "))
for value in range(1, 11):
    if(value == 5):
        continue
    print(n*value)
print("Table is printed!!")
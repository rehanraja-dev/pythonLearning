# The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.

for i in range(1, 11):
    print(f"Multiplication table of: {i}")
    for j in range(1, 11):
        print(i*j, " ", end='')
    print("\r")
        

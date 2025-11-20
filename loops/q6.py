number = int(input("Enter any number to count factorial: "))
factorial = 1
for value in range(1, number+1):
    factorial = factorial * value 
print(f"Using for loop: {factorial}")

factorial1 = 1
i = 1
while i <= number:
    factorial1 = factorial1 * i
    i += 1
print(f"Using while loop: {factorial1}")
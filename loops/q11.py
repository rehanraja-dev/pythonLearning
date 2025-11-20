# Find the sum of a series of a number up to n terms

input_number = int(input("Enter any integer number: "))
input_terms = int(input("Enter number of terms: "))
current_term = input_number

sum = input_number


for i in range(1, input_terms):
    current_term = current_term * 10 + input_number
    sum += current_term
print(f"Sum is {sum}")

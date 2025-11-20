# Return multiple values from a function

def response(num1, num2):
    addition = num1 + num2
    if num1 > num2:
        subtraction = num1 - num2
    else:
        subtraction = num2 - num1
    return addition, subtraction
num1 = int(input("Enter value for first number: "))
num2 = int(input("Enter value for second number: "))

res = response(num1, num2)
print(type(res))
for value in res:
    print(value)
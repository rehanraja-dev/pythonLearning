def fac(num):
    value = 1
    if num == 0:
        return 1
    else:
        value = value * num * fac(num -1)
        return value
        

print(fac(5))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(5))
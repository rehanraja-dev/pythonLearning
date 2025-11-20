# Print the following pattern
for i in range(1, 5):
    for j in range(1, i+1):
        print("*", end = '')
    print("\r")
for i in range(4, 1, -1):
    for j in range(i, 1, -1):
        print("*", end = '')
    print("\r")
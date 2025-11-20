# name = input("Enter name: ")    # always returns string
# age = int(input("Enter age: ")) # convert manually

# print("Hello", name, age)
# print(f"Hello {name}, you are {age} years old")  # f-string (modern formatting)

# if age >= 18:
#     print(f"{name} is an adult")
# else:
#     print(f"{name} is a minor")


# nums = [1, 2, 3]
# nums.append(4)       # add element
# print(nums[0])       # indexing
# print(nums[-1])      # negative index → last element

#type casting
# a = '1'
# b = 2
# print(a + str(b))  # concatenation
# print(int(a) + b)  # addition

# a = "str"
# print(a[1:2])  # last character
# print(a[2:3])  # last character

# i = 0
# print(float(i))  # convert to float
# print(bool(i))   # convert to boolean (0 is False, non-zero is True)
# print(str(i))    # convert to string

# float_num = 5/2
# print(int(float_num))  

# name = input("Enter name: ")
# age = int(input("Enter age: "))

# print(f"Hello {name}, you are {age} years old")
# print(name[1:])  # last character
# print(name[2:3])  # last character

# str = "hello i am Rehan"
# print(str.capitalize())  # Capitalize first letter
# print(str.upper())       # Convert to uppercase
# print(str.lower())       # Convert to lowercase
# print(str.title())       # Convert to title case
# print(str.replace("Rehan", "John"))  # Replace substring
# print(str.split(" "))    # Split string into list
# print(str.find("Rehan")) # Find substring index
# print(str.startswith("hello"))  # Check if string starts with substring
# print(str.endswith("Rehan"))    # Check if string ends with substring
# print(len(str))          # Length of string
# print(str.count("a"))   # Count occurrences of substring
# print(str.isalpha())    # Check if all characters are alphabetic
# print(str.isdigit())    # Check if all characters are digits
# print(str.isalnum())    # Check if all characters are alphanumeric
# print(str.strip())      # Remove leading and trailing whitespace
# print(str.center(50))   # Center string with padding
# print(str.ljust(50))    # Left justify string with padding
# print(str.rjust(50))    # Right justify string with padding
# print(str.zfill(50))    # Pad string with zeros on the left

# list = [1, 2, 3, 4, 5]
# print(list)
# list.append(6)          # Add element to end
# print(list)
# list.insert(0, 0)      # Insert element at index
# print(list)
# list.remove(3)         # Remove first occurrence of value
# print(list)
# list.pop()             # Remove and return last element
# print(list)
# print(list.pop(0))      # Remove and return element at index
# print(list)
# print(list.index(4))    # Get index of first occurrence of value

list = []
print(type(list))
print(len(list))  # Length of list
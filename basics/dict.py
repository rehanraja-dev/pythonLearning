# dict = {
#     'name': 'Alice',
#     'age': 30,
#     'city': 'New York',
#     'country': 'USA',
#     'is_student': False
# }
# print(dict['age'])  # Access value by key
# dict['age'] = 20  # Update value
# dict['name'] = 'Rehan Raja'  # Update value
# print(dict['age'])
# print(dict.get('name'))  # Safe access
# print(dict.get('country', 'USA_default'))  # Default value if key not found
# print(len(dict))  # Number of key-value pairs
# dict['profession'] = 'Engineer'  # Add new key-value pair
# dict.pop('is_student')  # Remove key-value pair
# dict['is_student'] = True  # Re-add key-value pair
# print(dict)

# dict = {
#     "student1": {
#         'name': 'Alice',
#         'age': 30,
#         'city': 'New York'
#     },
#     "student2": {
#         'name': 'Bob',
#         'age': 25,
#         'city': 'Los Angeles'
#     }
# }
# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict.get('student3', 'Not Found'))  # Default value if key not found
# print(dict['student1']['name'])  # Access nested dictionary value
# print(dict.update({'student3': {'name': 'Charlie', 'age': 22, 'city': 'Chicago'}}))  # Add new nested dictionary
# print(dict)

collection = {}
print(type(collection))  # <class 'dict'>
collection = dict()
print(type(collection))  # <class 'dict'>
collection = set()
print(type(collection))  # <class 'set'>


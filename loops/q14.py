
# nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]
# flatted_list = []
# for value in nested_list:
#     if isinstance(value, list):
#         for item in value:
#             flatted_list.append(item)
#         else:
#             flatted_list.append(value)
# print(flatted_list)

def flatten_list(nested_list):
    
    flat_list = []  # Initialize an empty list to store the flattened elements

    # Iterate through each element in the list
    for element in nested_list:
        if isinstance(element, list):  # Check if the element is a list
            for item in element:  # If so, iterate through the inner list
                flat_list.append(item)
        else:
            flat_list.append(element)  # If not a list, add the element directly

    return flat_list

# Example usage
nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]
flattened = flatten_list(nested_list)
print("Flattened list:", flattened)

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
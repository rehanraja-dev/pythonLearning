string_input = input("enter your name : ")
nameLen = len(string_input)
reverseName = ""
for value in range(nameLen-1, -1, -1):
    reverseName += string_input[value]

print(reverseName)

reverseName = ""

for value in string_input:
    reverseName = value + reverseName

print(reverseName)
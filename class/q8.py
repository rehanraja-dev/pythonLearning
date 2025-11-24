# Incapsulation

class Person:
    def __init__(self,fName,lName):
        self.__fName = fName
        self.__lName = lName
    
    def fullName(self):
        print(f"{self.__fName} {self.__lName}")

person = Person("Rehan", "Raja")
person.fullName()

#  ----Following access is denied ----
# person.__fName
# person.__lName
        
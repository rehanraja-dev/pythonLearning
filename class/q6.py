# Inheritance

class Person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def printName(self):
        print(f"Hello {self.firstName} {self.lastName}")

class Student(Person):
    def __init__(self, firstName, lastName, year):
        super().__init__(firstName, lastName)
        self.graduationYear = year

student = Student("rehan", "raja","2019")
student.printName()
        
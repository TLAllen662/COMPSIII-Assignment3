class Person:
    # Delete pass and add your code here
    def __init__ (self, name, age, country):
        self.name = name
        self.age = age
        self.country = country 
    def __str__ (self):
        return f"{self.name} is {self.age} years old and lives in {self.country}."
    
person_1 = Person("Ava", 28, "USA")

class Student(Person):
    # Delete pass and add your code here
    def __init__ (self,name, age, country, major, gpa):
        super().__init__(name, age, country)
        self.major = major
        self.gpa = gpa
        def study(self):
            return f"{self.name} is studying {self.major} with a current GPA of {self.age}."
        
student_1 = Student("Jake", 19, "England", "Computer Science", 3.85)



class Staff(Person):
    # Delete pass and add your code here
    def __init__ (self, name, age, country, position, department):
        super().__init__(name, age, country)
        self.position = position
        self.department = department
        def work(self):
            return f"{self.name} works as a {self.position} in the {self.department} department."
        
staff_1 = Staff("Robert", 44, "USA", "Professor", "History")
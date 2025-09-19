from school import *

def test_can_create_person():
    '''Test that the person object is created correctly'''
    person_1 = Person("Billy", 17, "Canada")
    assert person_1.name == "Billy"
    assert person_1.age == 17
    assert person_1.country == "Canada"

def test_person_string():
    '''Test that the __str__ method returns the correct string'''
    def __init__ (self, name, age, country):
        self.name = name
        self.age = age
        self.country = country 
    def __str__ (self):
        return f"{self.name} is {self.age} years old and lives in {self.country}."

def test_student_inheritance():
    '''Test that the student class inherits from the person class'''
    student = Student("John", 17, "Canada", "Computer Science", 3.5)
    assert isinstance(student, Person) == True
    assert isinstance(student, Student) == True

def test_student_attributes():
    '''Test that the student object is created correctly'''
    student = Student("John", 17, "Canada", "Computer Science", 3.5)
    assert student.name == "John"
    assert student.age == 17
    assert student.country == "Canada"
    assert student.major == "Computer Science"
    assert student.gpa == 3.5

def test_student_study():
    '''Test that the study method returns the correct string'''
def __init__ (self,name, age, country, major, gpa):
        super().__init__(name, age, country)
        self.major = major
        self.gpa = gpa
        def study(self):
            return f"{self.name} is studying {self.major} with a current GPA of {self.age}."

def test_staff_inheritance():
    '''Test that the staff class inherits from the person class'''
    staff = Staff("Jane", 30, "USA", "Professor", "Computer Science")
    assert isinstance(staff, Person) == True
    assert isinstance(staff, Staff) == True

def test_staff_attributes():
    '''Test that the staff object is created correctly'''
    staff = Staff("Jane", 30, "USA", "Professor", "Computer Science")
    assert staff.name == "Jane"
    assert staff.age == 30
    assert staff.country == "USA"
    assert staff.position == "Professor"
    assert staff.department == "Computer Science"

def test_staff_work():
    '''Test that the work method returns the correct string'''
def __init__ (self, name, age, country, position, department):
        super().__init__(name, age, country)
        self.position = position
        self.department = department
        def work(self):
            return f"{self.name} works as a {self.position} in the {self.department} department."
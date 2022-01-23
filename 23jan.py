
class Student: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age
        print("Student's name is " + name + " and age is " + str(age)) 
    def performance(self, grades): 
        self.grades = grades 
        print("The grade of student is: " + grades) 
class Girl(Student): 
    def __init__(self, name, age): 
        super().__init__(name, age) 
        print("Girl class is ready") 
    
    def whichclass(self): 
        print("Class under student") 
stu1 = Student("Diwon", 18)
stu1.performance("Nice") 
stu2 = Student("LegalDiwon", 17)
stu2.performance("varynice ") 
print("\n")
girl1 = Girl("Orange", 12) 
girl1.whichclass() 
girl1.performance("BAD")

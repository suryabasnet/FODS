class Student:
 
    school_name = 'ABC School'


    def __init__(self, name, age):

        self.name = name
        self.age = age

s1 = Student("Harry", 12)

print('Student:', s1.name, s1.age)


print('School name:', Student.school_name)


s1.name = 'Jessa'
s1.age = 14
print('Student:', s1.name, s1.age)


Student.school_name = 'XYZ School'
print('School name:', Student.school_name)

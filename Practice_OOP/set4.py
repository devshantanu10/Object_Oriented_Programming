class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print("hello my name is" , self.name, "and i am " , self.age , "years old")

name = input("Enter your name")
age = input("Enter you age")

std1 = Student(name ,age)
std1.intro()
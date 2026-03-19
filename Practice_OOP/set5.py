class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def info(self):
        print("Name: " , self.name, " Marks: " , self.marks)


name = input("Enter name: ")
marks = int(input("Enter marks: "))


s1 = Student(name , marks)

s1.display()
       
       
    

        
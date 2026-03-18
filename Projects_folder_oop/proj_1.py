class Student:
    def __init__(self,name,age,marks,):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:" , self.name)
        print("Age: " , self.age)
        print("Marks: " , self.marks)

    def average(self):
        return sum(self.marks) / len(self.marks)
    

s1 = Student("Shantanu" , 18 , [80,90,85])
s2 = Student("Manish" , 19 , [70,80,68])

s1.display()
s2.display()

print("Average: " , s1.average())
print("Average: " , s1.average())

    


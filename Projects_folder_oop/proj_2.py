class Student:
    def __init__(self,name,age,marks):
         self.name = name
         self.age = age
         self.marks = marks
    
    def display(self):
         print("Name: " , self.name)
         print("Age: " , self.age)
         print("Marks: " , self.marks)

    def average(self):
         return sum(self.marks)/len(self.marks)
    


name = input("Enter name: ")
age = int(input("Enter age : "))

n = int(input("No of subjects: "))
marks = []


for i in range(n):
         
         m = int(input(f"Enter marks{i + 1}: "))
         marks.append(m)


s1 = Student(name,age,marks)
s1.display()
print("Average" , s1.average())
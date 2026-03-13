
class Student:
      college_name = "ABC college"
      
    #parameterize constructor
      def __init__(self, name, marks):    #constructor
        self.name = name
        self.marks = marks
        print("Adding new student in database")

s1 = Student("karan", 97)
print(s1.name , s1.marks) #karan

s2 = Student("Arjun" , 88)
print(s2.name, s2.marks)

print(s2.college_name)


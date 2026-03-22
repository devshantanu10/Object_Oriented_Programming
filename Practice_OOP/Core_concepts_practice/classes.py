# Create a Car class with attributes brand, model, and year. Create 3 car objects and print their details.
# Create a Student class with name and grade. Add a method is_passing() that returns True if grade ≥ 50.3



# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def show_info(self):
#          print("Brand" , self.brand)
#          print("Model" , self.model)
#          print("Year" , self.year)

# car1 = Car("Toyota" , "prius" , 17)
# car1.show_info()  



class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def info(self):
        print(f"Student Name:" , {self.name})
        print(f"Grade: " , {self.grade})
    
    def is_passing(self):

            return self.grade >= 50.3
    

s1 = Student("Shantanuy", 60.3)
s2 = Student("Ram" , 40.4)
s2.info()
s1.info()
print("Is passing" , s1.is_passing())
print("Is passing" , s2.is_passing())
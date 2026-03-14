class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name , "Your avg scorte is: " , sum/3)


s1 = Student("Tony stark", [99, 98,97])
s1.get_avg()


s1.name = "ironman"
s1.get_avg()
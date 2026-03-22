class Complex:
    def __init__(self , real , img):
         self.real = real
         self.img = img 

    def showNumber(self):
         print(self.real , "i" , self.img, "j")

num1 = complex(1,3)
num1.showNumber()


num2 = complex(2,3)
num2.showNumber()

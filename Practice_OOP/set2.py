class Car:
    def __init__(self, brand , model, color): #constructors
        self.brand = brand
        self.model = model
        self.color = color

    def show_info(self):#Method 
        print("Brand:" , self.brand)
        print("Model: " , self.model)
        print("Color: " , self.color)

car1 = Car("Toyota" , "Corolla" , "Red")

car1.show_info()




    
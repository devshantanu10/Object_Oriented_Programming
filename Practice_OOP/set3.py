class Car:
    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color

    def show_info(self):
        print("Brand:", self.brand)
        print("Model: " , self.model)
        print("Color: " , self.color)


brand = input("Enter Brand:")
color = input("Enter car color:")
Model = input("Enter model name: ")


car1 = Car(brand, color, Model)

car1.show_info()


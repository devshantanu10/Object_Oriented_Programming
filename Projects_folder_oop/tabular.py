class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("\nName:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

    def average(self):
        return sum(self.marks) / len(self.marks)


students = []

while True:
    print("\n1. Add student")
    print("2. View Student")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        n = int(input("How many subjects: "))
        marks = []

        for i in range(n):
            m = int(input(f"Enter mark {i+1}: "))
            marks.append(m)

        s = Student(name, age, marks)
        students.append(s)

        print("Student added successfully!!!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found")
        else:
            for s in students:
                s.display()
                print("Average:", s.average())

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)

    def display(self):
        return f"Student | {super().display()}, ID: {self.student_id}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        return f"Teacher | {super().display()}, Subject: {self.subject}"


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teacher = None

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def add_student(self, student):
        self.students.append(student)


class School:
    def __init__(self):
        self.students = {}
        self.teachers = {}
        self.courses = {}

    def add_student(self, name, age, student_id):
        self.students[student_id] = Student(name, age, student_id)
        print("Student added!")

    def add_teacher(self, name, age, subject):
        self.teachers[name] = Teacher(name, age, subject)
        print("Teacher added!")

    def add_course(self, course_name):
        self.courses[course_name] = Course(course_name)
        print("Course added!")

    def enroll_student(self, student_id, course_name):
        student = self.students.get(student_id)
        course = self.courses.get(course_name)

        if student and course:
            student.enroll_course(course_name)
            course.add_student(student)
            print("Student enrolled!")
        else:
            print("Invalid student or course!")

    def assign_teacher(self, teacher_name, course_name):
        teacher = self.teachers.get(teacher_name)
        course = self.courses.get(course_name)

        if teacher and course:
            course.assign_teacher(teacher)
            print("Teacher assigned!")
        else:
            print("Invalid teacher or course!")

    def show_students(self):
        for s in self.students.values():
            print(s.display())

    def show_teachers(self):
        for t in self.teachers.values():
            print(t.display())


def main():
    school = School()

    while True:
        print("\n1. Add Student")
        print("2. Add Teacher")
        print("3. Add Course")
        print("4. Enroll Student")
        print("5. Assign Teacher")
        print("6. Show Students")
        print("7. Show Teachers")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            sid = input("Student ID: ")
            school.add_student(name, age, sid)

        elif choice == "2":
            name = input("Name: ")
            age = int(input("Age: "))
            subject = input("Subject: ")
            school.add_teacher(name, age, subject)

        elif choice == "3":
            course = input("Course name: ")
            school.add_course(course)

        elif choice == "4":
            sid = input("Student ID: ")
            course = input("Course name: ")
            school.enroll_student(sid, course)

        elif choice == "5":
            tname = input("Teacher name: ")
            course = input("Course name: ")
            school.assign_teacher(tname, course)

        elif choice == "6":
            school.show_students()

        elif choice == "7":
            school.show_teachers()

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
class StudentManagementSystem:

    def __init__(self):
        self.students = {}

    def add_student(self):
        roll = input("Enter Roll Number: ")

        if roll in self.students:
            print("Student already exists!")
            return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        self.students[roll] = {
            "Name": name,
            "Age": age,
            "Course": course,
            "Marks": marks
        }

        print("Student Added Successfully.")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\n------ Student Records ------")

        for roll, details in self.students.items():
            print("------------------------------")
            print("Roll Number :", roll)
            print("Name        :", details["Name"])
            print("Age         :", details["Age"])
            print("Course      :", details["Course"])
            print("Marks       :", details["Marks"])

    def search_student(self):
        roll = input("Enter Roll Number to Search: ")

        if roll in self.students:
            print("\nStudent Found")
            print(self.students[roll])
        else:
            print("Student Not Found.")

    def update_student(self):
        roll = input("Enter Roll Number to Update: ")

        if roll not in self.students:
            print("Student Not Found.")
            return

        print("Leave blank to keep old value.")

        name = input("New Name: ")
        age = input("New Age: ")
        course = input("New Course: ")
        marks = input("New Marks: ")

        if name:
            self.students[roll]["Name"] = name

        if age:
            self.students[roll]["Age"] = int(age)

        if course:
            self.students[roll]["Course"] = course

        if marks:
            self.students[roll]["Marks"] = float(marks)

        print("Student Updated Successfully.")

    def delete_student(self):
        roll = input("Enter Roll Number to Delete: ")

        if roll in self.students:
            del self.students[roll]
            print("Student Deleted Successfully.")
        else:
            print("Student Not Found.")

    def menu(self):

        while True:

            print("\n==============================")
            print(" Student Management System")
            print("==============================")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                print("Thank You!")
                break

            else:
                print("Invalid Choice. Try Again.")


sms = StudentManagementSystem()
sms.menu()
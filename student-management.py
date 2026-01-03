students = []

def add_student():
    name = input("Enter student name: ")
    matric_number = input("Enter matric number: ")
    students.append({
        "name": name,
        "matric_number": matric_number
    })
    print("Student added successfully.\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    for index, student in enumerate(students, start=1):
        print(f"{index}. Name: {student['name']}, Matric Number: {student['matric_number']}")
    print()

def delete_student():
    view_students()
    if not students:
        return
    try:
        choice = int(input("Enter student number to delete: "))
        students.pop(choice - 1)
        print("Student deleted successfully.\n")
    except (ValueError, IndexError):
        print("Invalid selection.\n")

def main_menu():
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("Exiting system.")
            break
        else:
            print("Invalid option.\n")

main_menu()

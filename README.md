 STUDENT MANAGEMENT SYSTEM 

Project Description
The Student Management System is a simple command-line application written in Python.
It allows users to add, view, and delete student records.


Software Development Life Cycle (SDLC)

 1. Requirement Analysis
The system is designed to manage student records efficiently.

* Functional Requirements:
- Add a student
- View all students
- Delete a student
- Exit the system

* Non-Functional Requirements:
- Easy to use
- Command-line based
- Implemented in Python

 2. System Design

Architecture: Command Line Application  
Programming Language: Python  

* Data Structure:
- A list named `students`
- Each student is stored as a dictionary with:
  - `name`
  - `matric_number`

* Modules and Functions:

- `student_management.py`
  - `add_student()`
  - `view_students()`
  - `delete_student()`
  - `main_menu()`


 3. Implementation
The project was implemented using Python following the design specifications.
All function names and variables used in the design are exactly the same in the implementation.



 4. Testing
The system was tested manually using the following test cases:
- Adding a student record
- Viewing student records
- Deleting a student record
- Exiting the application

All test cases passed successfully.



 5. Deployment
The project was deployed by uploading it to a public GitHub repository.


 6. Maintenance
Future improvements may include:
- File storage
- Database integration
- Graphical user interface



## How to Run the Program
Run the command below in the project folder:

```bash
python student_management.py

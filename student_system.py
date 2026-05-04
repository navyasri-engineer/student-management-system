import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table with ID
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

# Add student
def add_student():
    name = input("Enter name: ")

    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Invalid age. Please enter a number.\n")
        return

    course = input("Enter course: ")

    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    conn.commit()
    print("Student added successfully!\n")


# View students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No records found.\n")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Course: {student[3]}")


# Search student
def search_student():
    name = input("Enter name to search: ")

    cursor.execute("SELECT * FROM students WHERE name=?", (name,))
    students = cursor.fetchall()

    if students:
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Course: {student[3]}")
    else:
        print("Student not found.\n")


# Update student
def update_student():
    try:
        student_id = int(input("Enter student ID to update: "))
    except ValueError:
        print("Invalid ID.\n")
        return

    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    student = cursor.fetchone()

    if student:
        new_name = input("Enter new name: ")

        try:
            new_age = int(input("Enter new age: "))
        except ValueError:
            print("Invalid age.\n")
            return

        new_course = input("Enter new course: ")

        cursor.execute(
            "UPDATE students SET name=?, age=?, course=? WHERE id=?",
            (new_name, new_age, new_course, student_id)
        )
        conn.commit()

        print("Student updated successfully!\n")
    else:
        print("Student not found.\n")


# Delete student
def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))
    except ValueError:
        print("Invalid ID.\n")
        return

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")


# Menu
def menu():
    while True:
        print("\n1.Add  2.View  3.Search  4.Update  5.Delete  6.Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


menu()
conn.close()

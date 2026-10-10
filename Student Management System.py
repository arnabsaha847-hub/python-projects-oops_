
import csv
import os

FILE = "students.csv"


def initialize_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Roll Number", "Name", "Marks"])


def add_student():
    roll = input("Enter roll number: ")

    students = read_students()

    for student in students:
        if student["Roll Number"] == roll:
            print("Roll number already exists!")
            return

    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    try:
        marks = float(marks)
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter valid marks.")
        return

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll, name, marks])

    print("Student added successfully!")


def read_students():
    with open(FILE, "r", newline="") as f:
        return list(csv.DictReader(f))


def search_student():
    roll = input("Enter roll number to search: ")

    for student in read_students():
        if student["Roll Number"] == roll:
            print("Student Details:", student)
            return

    print("Student not found!")


def delete_student():
    roll = input("Enter roll number to delete: ")
    students = read_students()

    updated = [
        s for s in students if s["Roll Number"] != roll
    ]

    if len(updated) == len(students):
        print("Student not found!")
        return

    with open(FILE, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["Roll Number", "Name", "Marks"]
        )
        writer.writeheader()
        writer.writerows(updated)

    print("Student deleted successfully!")


def display_students():
    students = read_students()

    if not students:
        print("No student records found.")
    else:
        for student in students:
            print(student)


initialize_file()

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")

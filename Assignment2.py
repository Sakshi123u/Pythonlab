#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


def add_student(students):
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    num_subjects = int(input("Enter the number of subjects: "))

    grades = []
    total = 0
    for i in range(num_subjects):
        grade = float(input(f"Enter grade for subject {i+1}: "))
        grades.append(grade)
        total += grade

    average_grade = total / num_subjects

    student = [roll_no, name, total, average_grade, grades]
    students.append(student)
    print(f"\nStudent {name} added successfully.\n")


def get_average(student):
    return student[3]  # student[3] is the average grade


def sort_students_by_average(students):
    students.sort(key=get_average, reverse=True)
    print("\nStudents sorted by average grade:")
    for student in students:
        print(f"Roll Number: {student[0]}, Name: {student[1]}, Average Grade: {student[3]:.2f}")


def delete_student(students):
    roll_no = input("Enter Roll Number to delete: ")

    for student in students:
        if student[0] == roll_no:
            if student[3] < 40:
                print(f"\nStudent {student[1]} with Roll Number {roll_no} has failed the exam with an average grade of {student[3]:.2f}. Record will not be deleted.\n")
            else:
                print(f"\nStudent with Roll Number {roll_no} has an average grade of {student[3]:.2f}, which is not less than 40. Deletion not allowed.\n")
            return
    print(f"\nNo student found with Roll Number {roll_no}.\n")



def display_students(students):
    print("\nCurrent Student Records:")
    for student in students:
        print(f"Roll Number: {student[0]}, Name: {student[1]}, Total: {student[2]}, Average Grade: {student[3]:.2f}")


def manage_students():
    students = []

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Sort Students by Average Grade")
        print("4. Display All Students")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student(students)
        elif choice == 2:
            delete_student(students)
        elif choice == 3:
            sort_students_by_average(students)
        elif choice == 4:
            display_students(students)
        elif choice == 5:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


manage_students()


# In[ ]:





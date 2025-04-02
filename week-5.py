def student_names():
    # Student names and grades (Dictionary)
    return [
        {"name": "John Doe", "grade": 85},
        {"name": "Jane Smith", "grade": 92},
        {"name": "Alice Johnson", "grade": 78},
        {"name": "Bob Brown", "grade": 88}
    ]

def update_grade(students, name, new_grade):
    # Update a student's grade
    name = name.lower()
    for student in students:
        if student["name"].lower() == name:
            student["grade"] = new_grade
            print(f"Updated {name}'s grade to {new_grade}.")
            return
    print(f"Student {name} not found.")

def highest_grade(students):
    # Finding the highest grade
    highest = max(student["grade"] for student in students)
    print(f"Highest grade: {highest}")
    return highest

def lowest_grade(students):
    # Finding the lowest grade
    lowest = min(student["grade"] for student in students)
    print(f"Lowest grade: {lowest}")
    return lowest

def class_average(students):
    # Calculate the class average
    total = sum(student["grade"] for student in students)
    average = total / len(students)
    print(f"Class average: {average:.2f}")
    return average

def display_grade_report(students):
    # Display a full grade report
    print("\nGrade Report:")
    for student in students:
        print(f"{student['name']}: {student['grade']}")

def save_grade_report(students):
    # Save the grade report to a text file
    with open("grade_report.txt", "w") as file:
        file.write("Grade Report:\n")
        for student in students:
            file.write(f"{student['name']}: {student['grade']}\n")
    print("Grade report saved to 'grade_report.txt'.")

def main():
    students = student_names()

    while True:
        print("\n--- Student Grade Management ---")
        print("1. Display Grade Report")
        print("2. Update a Student's Grade")
        print("3. Find Highest Grade")
        print("4. Find Lowest Grade")
        print("5. Calculate Class Average")
        print("6. Save Grade Report to File")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            display_grade_report(students)
        elif choice == "2":
            name = input("Enter student name: ")
            try:
                new_grade = int(input("Enter new grade: "))
                update_grade(students, name, new_grade)
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")
        elif choice == "3":
            highest_grade(students)
        elif choice == "4":
            lowest_grade(students)
        elif choice == "5":
            class_average(students)
        elif choice == "6":
            save_grade_report(students)
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()

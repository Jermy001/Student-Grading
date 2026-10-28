
def validate_student_details(name, department, semester):
    """Validate student name, department, and semester."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Student name cannot be empty.")

    if not isinstance(department, str) or not department.strip():
        raise ValueError("Department cannot be empty.")

    if isinstance(semester, bool):
        raise ValueError("Semester must be a positive integer.")

    try:
        semester_value = int(semester)
    except (ValueError, TypeError):
        raise ValueError("Semester must be a positive integer.")

    if str(semester_value) != str(semester).strip() or semester_value <= 0:
        raise ValueError("Semester must be a positive integer.")

    return name.strip(), department.strip(), semester_value


def validate_marks(marks):
    """Validate that marks are numeric and between 0 and 100."""
    if isinstance(marks, bool):
        raise ValueError("Marks must be numeric.")

    try:
        value = float(marks)
    except (ValueError, TypeError):
        raise ValueError("Marks must be numeric.")

    if not 0 <= value <= 100:
        raise ValueError("Marks must be between 0 and 100.")

    return value


def calculate_total(marks):
    """Calculate the total of three subject marks."""
    if len(marks) != 3:
        raise ValueError("Exactly three subject marks are required.")

    validated_marks = [validate_marks(mark) for mark in marks]
    return sum(validated_marks)


def calculate_average(marks):
    """Calculate the average percentage for three subjects."""
    total = calculate_total(marks)
    return total / 3


def calculate_grade(average):
    """Assign a grade using the unrounded average."""
    if isinstance(average, bool):
        raise ValueError("Average must be numeric.")

    try:
        value = float(average)
    except (ValueError, TypeError):
        raise ValueError("Average must be numeric.")

    if not 0 <= value <= 100:
        raise ValueError("Average must be between 0 and 100.")

    if value >= 90:
        return "S"
    elif value >= 80:
        return "A"
    elif value >= 65:
        return "B"
    elif value >= 50:
        return "C"
    elif value >= 40:
        return "D"
    else:
        return "F"


def read_marks(subject_number):
    """Read and validate marks, retrying after invalid input."""
    while True:
        raw_marks = input(
            f"Enter marks for Subject {subject_number} (0-100): "
        )

        try:
            return validate_marks(raw_marks)
        except ValueError as error:
            print(f"Invalid input: {error} Please try again.")


def evaluate_student():
    """Collect details, calculate results, and print the report."""
    while True:
        name = input("Enter student name: ")
        department = input("Enter department: ")
        semester_input = input("Enter semester: ")

        try:
            name, department, semester = validate_student_details(
                name, department, semester_input
            )
            break
        except ValueError as error:
            print(f"Invalid student details: {error}")
            print("Please enter the student details again.\n")

    marks = [read_marks(i) for i in range(1, 4)]
    total = calculate_total(marks)
    average = total / 3
    grade = calculate_grade(average)

    print("\n" + "=" * 40)
    print("       STUDENT RESULT REPORT")
    print("=" * 40)
    print(f"Student Name : {name}")
    print(f"Department   : {department}")
    print(f"Semester     : {semester}")
    print("-" * 40)
    print(f"Total Marks  : {total:.2f} / 300")
    print(f"Average      : {average:.2f}%")
    print(f"Grade        : {grade}")
    print("=" * 40)


def main():
    """Display the application menu."""
    print("Welcome to the Student Grade Evaluation System!")

    while True:
        print("\n1. Evaluate a student")
        print("2. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            evaluate_student()
        elif choice == "2":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()

"""Run the student management demo."""

from students import list_students


def main():
    students = ["Asha", "Ravi", "Meera"]
    print("Student Management Demo")
    print("------------------------")
    for number, name in enumerate(list_students(students), start=1):
        print(f"{number}. {name}")


if __name__ == "__main__":
    main()

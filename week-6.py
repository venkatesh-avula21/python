import json
from pathlib import Path


class Student:
    def __init__(self, student_id, name, course, marks):
        self.__student_id = student_id
        self.__name = name
        self.__course = course
        self.__marks = marks

    def to_dict(self):
        return {
            "student_id": self.__student_id,
            "name": self.__name,
            "course": self.__course,
            "marks": self.__marks
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["name"],
            data["course"],
            data["marks"]
        )

    def display(self):
        print(
            f"ID: {self.__student_id} | "
            f"Name: {self.__name} | "
            f"Course: {self.__course} | "
            f"Marks: {self.__marks}"
        )


class StudentManager:
    def __init__(self, filename="data/students.json"):
        self.filename = Path(filename)
        self.students = []
        self.load()

    def load(self):
        try:
            if self.filename.exists():
                data = json.loads(
                    self.filename.read_text(encoding="utf-8")
                )
                self.students = [
                    Student.from_dict(item) for item in data
                ]
        except (OSError, json.JSONDecodeError,
                KeyError, TypeError) as error:
            print("Could not load saved records:", error)
            self.students = []

    def save(self):
        try:
            self.filename.parent.mkdir(
                parents=True, exist_ok=True
            )
            data = [
                student.to_dict()
                for student in self.students
            ]
            self.filename.write_text(
                json.dumps(data, indent=4),
                encoding="utf-8"
            )
        except OSError as error:
            print("Could not save records:", error)

    def add_student(self):
        student_id = input("Enter student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            return

        if any(
            s.to_dict()["student_id"] == student_id
            for s in self.students
        ):
            print("That student ID already exists.")
            return

        name = input("Enter name: ").strip()
        course = input("Enter course: ").strip()

        if not name or not course:
            print("Name and course cannot be empty.")
            return

        try:
            marks = float(input("Enter marks (0-100): "))
            if not 0 <= marks <= 100:
                raise ValueError
        except ValueError:
            print("Enter a valid mark from 0 to 100.")
            return

        self.students.append(
            Student(student_id, name, course, marks)
        )
        self.save()
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        for student in self.students:
            student.display()

    def search_student(self):
        student_id = input(
            "Enter student ID to search: "
        ).strip()

        for student in self.students:
            if student.to_dict()["student_id"] == student_id:
                student.display()
                return

        print("Student not found.")

    def delete_student(self):
        student_id = input(
            "Enter student ID to delete: "
        ).strip()

        for student in self.students:
            if student.to_dict()["student_id"] == student_id:
                self.students.remove(student)
                self.save()
                print("Student deleted successfully.")
                return

        print("Student not found.")


def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod

# Abstraction
class School(ABC):
    def __init__(self, name, students):
        self._name = name            # Encapsulation
        self._students = students    # Encapsulation

    @abstractmethod
    def display_results(self):  # Polymorphism
        pass

    def get_average(self):  # Instance Method
        total = sum(self._students.values())
        return total / len(self._students)

    @classmethod
    def from_list(cls, name, student_list):
        students = {name: grade for name, grade in student_list}
        return cls(name, students)

# Inheritance for School 1
class SchoolOne(School):
    def display_results(self):  # Polymorphism
        print(f"--- {self._name} ---")
        for student, grade in self._students.items():
            print(f"{student}: {grade}")
        print("Average Grade:", self.get_average())
        print("GPA:", round(self.get_average() / 25, 2))

# Inheritance for school 2
class SchoolTwo(School):
    def display_results(self):  # Polymorphism
        print(f"--- {self._name} ---")
        for student, grade in self._students.items():
            print(f"{student}: {grade}")
        print("Average Grade:", self.get_average())
        print("GPA:", round(self.get_average() / 25, 2))


def main():
    # Using class method constructor
    list_one = [("Anna", 90), ("Ben", 85), ("Cathy", 88)]
    list_two = [("Dan", 80), ("Ella", 75), ("Frank", 78)]

    school1 = SchoolOne.from_list("School One", list_one)
    school2 = SchoolTwo.from_list("School Two", list_two)

    school1.display_results()
    print("")
    school2.display_results()

if __name__ == "__main__":
    main()

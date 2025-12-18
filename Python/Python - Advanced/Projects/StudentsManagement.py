class Students:
    def __init__(self, name, student_id, age):
        self.name = name
        self.student_id = student_id
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.student_id}, Age: {self.age}")

class CSEStudent(Students):
    def __init__(self, name, student_id, age, programming_language):
        super().__init__(name, student_id, age)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Branch: CSE, Programming Language: {self.programming_language}")

class ECEStudent(Students):
    def __init__(self, name, student_id, age, circuit_design_tool):
        super().__init__(name, student_id, age)
        self.circuit_design_tool = circuit_design_tool

    def display_info(self):
        super().display_info()
        print(f"Branch: ECE, Circuit Design Tool: {self.circuit_design_tool}")

class MechanicalStudent(Students):
    def __init__(self, name, student_id, age, cad_software):
        super().__init__(name, student_id, age)
        self.cad_software = cad_software

    def display_info(self):
        super().display_info()
        print(f"Branch: Mechanical, CAD Software: {self.cad_software}")

class EEEStudent(Students):
    def __init__(self, name, student_id, age, power_system_focus):
        super().__init__(name, student_id, age)
        self.power_system_focus = power_system_focus

    def display_info(self):
        super().display_info()
        print(f"Branch: EEE, Power System Focus: {self.power_system_focus}")

# Example usage
if __name__ == "__main__":
    cse_student = CSEStudent("Alice", "CSE001", 20, "Python")
    ece_student = ECEStudent("Bob", "ECE001", 21, "Altium")
    mech_student = MechanicalStudent("Charlie", "MECH001", 22, "AutoCAD")
    eee_student = EEEStudent("David", "EEE001", 23, "Power Electronics")

    students = [cse_student, ece_student, mech_student, eee_student]
    for student in students:
        student.display_info()
        print("---")
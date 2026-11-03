"""
YUVA INTERN - Task 2: Core Concepts and Skills
Name: Injarapu Sailaja
Domain: Python Developer
Date: 03-Nov-2026
GitHub: https://github.com/injarapusailaja123-blip/yuva-task2-core-concepts
"""

print("=== YUVA TASK 2: CORE CONCEPTS AND SKILLS ===")

# === OBJECTIVE 1: Deep Expertise in Core Concepts ===
# Reasoning: List mutable for changing data, Tuple immutable for fixed config - performance + safety
student_name = "Sailaja"
student_marks = [85, 90, 78, 92]  # list - can add more marks later
student_id_config = (101, "CSE")  # tuple - ID fixed, immutable
student_dict = {"name": student_name, "marks": student_marks, "id": student_id_config}
print(f"1. Core Concepts: {student_dict}")

# === OBJECTIVE 2: WHY Behind Best Practices ===
# WHY PEP8? Team readability. WHY try-except? App crash avoid. WHY with open? Auto-close avoids memory leak.
try:
    with open("student_data.txt", "w") as f:  # Best practice - auto close
        f.write(f"Student: {student_name}, Avg: {sum(student_marks)/len(student_marks)}")
    print("2. Best Practice: File written safely with 'with open' + specific exception")
except FileNotFoundError as e:  # Specific exception, not bare except - Best Practice
    print(f"Error: {e}")
except ValueError as e:
    print(f"Value Error: {e}")

# === OBJECTIVE 3: Hands-on Exercises After Each Concept ===
def calculate_average(marks_list):
    """Reusable function - DRY Principle - Avoids repeated code"""
    # Reasoning: Function created because average calculation needed many times
    return sum(marks_list) / len(marks_list) if marks_list else 0

def is_pass(marks_list):
    """Check pass - exercise after conditions"""
    avg = calculate_average(marks_list)
    return avg >= 35

print(f"3. Hands-on: Average={calculate_average(student_marks)}, Pass={is_pass(student_marks)}")

# === OBJECTIVE 4: Guided Tutorials Simple to Complex ===
# Level1: Variables -> Level2: Functions -> Level3: OOPs (Simple to Complex progression)
class Student:
    """
    OOPs Concept - Class groups data + behavior
    Reasoning: OOPs used because industry uses OOPs for large projects - easy maintenance
    """
    def __init__(self, name, marks):
        self.name = name  # instance variable
        self.marks = marks

    def get_average(self):
        return calculate_average(self.marks)

    def get_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        else:
            return "B"

    def display(self):
        print(f"Student: {self.name}, Avg: {self.get_average()}, Grade: {self.get_grade()}")

# === OBJECTIVE 5: Small Projects - Stepping Stones ===
# Project is Student Management - combines 4 concepts - stepping stone to large app
s1 = Student("Sailaja", student_marks)
s1.display()
print("5. Small Project: Student class - proves mastery, stepping stone to web app")

# === OBJECTIVE 6: Best Practices & Industry Standards ===
# Followed: Meaningful names (student_name not s), Docstrings, PEP8, Git commits with message, Reusable functions
# Industry Structure: src/main.py, README, .gitignore, requirements.txt - matches company repo
print("6. Best Practices: PEP8, meaningful names, docstrings, DRY, Git commits")

# === OBJECTIVE 7: Common Pitfalls & How to Avoid ===
# Pitfall 1: Mutable default arg def func(a=[]): - Dangerous, shares list
# Avoided: Use None
def safe_add_student(name, marks=None):
    if marks is None:
        marks = []
    marks.append(90)
    return marks

# Pitfall 2: IndentationError - Avoided: VS Code auto-format 4 spaces
# Pitfall 3: File not closed - Avoided: with open()
# Pitfall 4: Bare except: - Avoided: specific exceptions
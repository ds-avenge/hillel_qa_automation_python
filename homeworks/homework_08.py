# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
# який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_average_grade):
        self.average_grade = new_average_grade

student1 = Student("Dmytro", "Semkov", 28, 50)

print(
    "Студент 1:\n"
    f"Ім'я: {student1.first_name}\n"
    f"Прізвище: {student1.last_name}\n"
    f"Вік: {student1.age}\n"
    f"Середній бал: {student1.average_grade}"
)

student1.change_average_grade(100)

print(f"Новий середній бал: {student1.average_grade}")

student2 = Student("Denys", "Merezhkin", 32, 70)
print("-" * 30)
print(
    "Студент 2:\n"
    f"Ім'я: {student2.first_name}\n"
    f"Прізвище: {student2.last_name}\n"
    f"Вік: {student2.age}\n"
    f"Середній бал: {student2.average_grade}"
)

student2.change_average_grade(100)
print(f"Новий середній бал: {student2.average_grade}")

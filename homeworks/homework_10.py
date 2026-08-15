# Завдання 1
# Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer,
# які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ),
# а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
import abc
import math

print("--- Task 01 ---")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

teamLead = TeamLead("Dmytro", 1000, "QA", "Python", 5)
print(
    f"TeamLead:\n"
    f"  Name: {teamLead.name}\n"
    f"  Salary: {teamLead.salary}\n"
    f"  Department: {teamLead.department}\n"
    f"  Programming language: {teamLead.programming_language}\n"
    f"  Team size: {teamLead.team_size}\n"
)
assert hasattr(teamLead, 'department'), "TeamLead should have department attribute"
assert hasattr(teamLead, 'programming_language'), "TeamLead should have programming_language attribute"
print("All TeamLead attribute tests passed.")

# Завдання 2
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
print("\n--- Task 02 ---")
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return 4 * self.__side

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

rectangle = Rectangle(4, 6)
square = Square(5)
circle = Circle(3)

shapes = [rectangle, square, circle]
for shape in shapes:
    print(
        f"{shape.__class__.__name__}:\n"
        f"  Area: {shape.area():.2f}\n"
        f"  Perimeter: {shape.perimeter():.2f}\n"
    )

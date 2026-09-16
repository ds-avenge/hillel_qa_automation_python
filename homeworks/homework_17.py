# Генератори:
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

print("=== Even numbers ===")
print(*even_numbers(10), sep=", ")

# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

print("\n=== Fibonacci sequence ===")
print(*fibonacci(50), sep=", ")

# Ітератори:
# Реалізуйте ітератор для зворотного виведення елементів списку.
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

numbers = [10, 20, 30, 40]
print("\n=== Reverse iterator ===")
print(*ReverseIterator(numbers), sep=", ")

# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

print("\n=== Even iterator ===")
print(*EvenIterator(10), sep=", ")

# Декоратори:
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper

@log_decorator
def add(a, b):
    return a + b

print("\n=== Logging decorator ===")
add(5, 3)

def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error occurred in {func.__name__}: {e}")

    return wrapper

@exception_decorator
def divide(a, b):
    return a / b

print("\n=== Exception decorator ===")
divide(10, 0)

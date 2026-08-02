# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print("--- Task 01 ---")
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print("\n--- Task 02 ---")
def calculate_sum(num1, num2):
    return num1 + num2

result = calculate_sum(5, 7)
print(f"Sum of 5 and 7 is: {result}")

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("\n--- Task 03 ---")
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

numbers = [10, 20, 30]
result1 = calculate_average(numbers)
print(f"Average of {numbers} is: {result1}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("\n--- Task 04 ---")
def reverse_string(text):
    return text[::-1]

text = "Python"
print(f"Reverse of {text} is: {reverse_string(text)}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("\n--- Task 05 ---")
def find_longest_word(words):
    return max(words, key=len) if words else None

words = ["Dmytro", "Denys", "Python", "Automation", "QA", "Hillel", "Summer"]
longest_word = find_longest_word(words)
print(f"The longest word in {words} is: {longest_word}")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("\n--- Task 06 ---")
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""
print("\n--- Task 07 ---")
# Task 6.1
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()
def has_more_than_ten_unique_characters(text):
    """
    Return True if the text contains more than 10 unique characters.
    :param text: Text to check.
    """
    return len(set(text)) > 10

user_text = input("Enter a string: ")
result2 = has_more_than_ten_unique_characters(user_text)
print(result2)

print("\n--- Task 08 ---")
# Task 6.2
# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
def contains_letter_h(word: str) -> bool:
    """
    Check if the word contains the letter 'h' (case-insensitive).
    :param word: Word to check.
    """
    return 'h' in word.lower()

while True:
    user_text1 = input("Enter a word containing the letter 'h': ")
    if contains_letter_h(user_text1):
        print("The word contains the letter 'h'.")
        break
    else:
        print("Word does not contain the letter 'h'. Please try again.")

print("\n--- Task 09 ---")
# Task 6.3
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Дані в лісті можуть бути будь-якими
def get_string_items(items: list) -> list:
    """
    Return a list containing only string items from the input list.
    :param items: List to filter.
    """
    return [item for item in items if isinstance(item, str)]

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = get_string_items(lst1)
print(lst2)

print("\n--- Task 10 ---")
# Task 6.4
# Є ліст з числами, порахуйте суму усіх ПАРНИХ чисел в цьому лісті
def sum_of_even_numbers(numbers: list[int]) -> int:
    """
    Return the sum of all even numbers in the input list.
    :param numbers: List of numbers to sum.
    """
    return sum(item for item in numbers if item % 2 == 0)

lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result3 = sum_of_even_numbers(lst3)
print(result3)

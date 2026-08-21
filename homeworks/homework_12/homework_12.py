# Task 3 from homework_07.py
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Task 5 from homework_07.py
def find_longest_word(words):
    return max(words, key=len) if words else None

# Task 6 from homework_07.py
def find_substring(str1, str2):
    return str1.find(str2)

# Task 9 from homework_07.py
def get_string_items(items: list) -> list:
    """
    Return a list containing only string items from the input list.
    :param items: List to filter.
    """
    return [item for item in items if isinstance(item, str)]

# Task 10 from homework_07.py
def sum_of_even_numbers(numbers: list[int]) -> int:
    """
    Return the sum of all even numbers in the input list.
    :param numbers: List of numbers to sum.
    """
    return sum(item for item in numbers if item % 2 == 0)

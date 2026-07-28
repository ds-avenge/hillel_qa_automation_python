# Task 6.1
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()
print("--- Task 01 ---")
print(len(set(input("Enter a string: "))) > 10)

# Task 6.2
# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
print("\n--- Task 02 ---")
while True:
    input_word = input("Enter a word containing the letter 'h': ")
    if "h" in input_word or "H" in input_word:
        break
    else:
        print("Word does not contain the letter 'h'. Please try again.")

# Task 6.3
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Дані в лісті можуть бути будь-якими
print("\n--- Task 03 ---")
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [item for item in lst1 if isinstance(item, str)]
print(lst2)

# Task 6.4
# Є ліст з числами, порахуйте суму усіх ПАРНИХ чисел в цьому лісті
print("\n--- Task 04 ---")
lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(item for item in lst3 if item % 2 == 0))

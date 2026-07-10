# task 01 == Виправте синтаксичні помилки
print("--- Task 01 ---")
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
print("\n--- Task 02 ---")
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
print("\n--- Task 03 ---")
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
print("\n--- Task 04 ---")
apples = 2
banana = apples * 4
print("Кількість яблук: ", apples, "\nКількість бананів: ", banana)

# task 05 == виправте назви змінних
print("\n--- Task 05 ---")
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
print("\n--- Task 06 ---")
perimeter = storona_1 + storona_2 + storona_3 + storona_4
print("Периметр фігури: ", perimeter)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
print("\n--- Task 07 ---")
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
total_trees = apple_trees + pear_trees + plum_trees
print("У саду посадили: ", apple_trees, " яблуні.", sep="")
print("Груш посадили ", pear_trees, ", на 5 більше, ніж яблунь.", sep="")
print(f"Слив посадили {plum_trees}, на 2 менше, ніж яблунь.")
print(f"Усього в саду посадили: {total_trees} дерев.")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
print("\n--- Task 08 ---")
morning_temperature = 5
afternoon_temperature = morning_temperature - 10
evening_temperature = afternoon_temperature + 4
print(f"Температура до обіду: {morning_temperature} градусів.")
print(f"Температура після обіду: {afternoon_temperature} градусів. Опустилася на 10 градусів.")
print(f"Температура надвечір: {evening_temperature} градус. Потепліло на 4 градуси.")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
print("\n--- Task 09 ---")
boys = 24
girls = boys // 2
sick_boys = 1
missing_girls = 2
boys_present = boys - sick_boys
girls_present = girls - missing_girls
total_children = boys_present + girls_present
print(f"У театральному гуртку загалом {boys} хлопчиків і {girls} дівчаток.")
print(f"Захворів {sick_boys} хлопчик, а {missing_girls} дівчинки не прийшли на заняття.")
print(f"Сьогодні у театральному гуртку: {total_children} дітей.")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
print("\n--- Task 10 ---")
first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) // 2
total_price_book = first_book + second_book + third_book
print(f"Перша книжка коштує {first_book} грн., друга - {second_book} грн., а третя - {third_book} грн.")
print(f"Усього книги будуть коштувати: {total_price_book} грн.")

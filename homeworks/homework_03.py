# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
for symbol in alice_in_wonderland:
    if symbol == "'":
        print(symbol)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436_402
azov_sea_area = 37_800
total_sea_area = black_sea_area + azov_sea_area
print(f"Площа Чорного Моря становить {black_sea_area:,} км²")
print(f"Площа Азовського Моря становить {azov_sea_area:,} км²")
print("Щоб знайти загальну площу, потрібно додати площу Чорного Моря до площі Азовського Моря.")
print(f"{black_sea_area:,} + {azov_sea_area:,} = {total_sea_area:,} км²")
print(f"Загальна площа становить {total_sea_area:,} км²")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_products = 375291
first_and_second_warehouses = 250449
second_and_third_warehouses = 222950

first_warehouse = total_products - second_and_third_warehouses
second_warehouse = first_and_second_warehouses - first_warehouse
third_warehouse = total_products - first_and_second_warehouses
total_warehouse = third_warehouse + second_warehouse + first_warehouse

print(f"Мережа супермаркетів має 3 склади, де всього розміщено {total_products:,} товарів.")
print(f"На першому та другому складах перебуває {first_and_second_warehouses:,} товарів.")
print(f"На другому та третьому – {second_and_third_warehouses:,} товарів.")
print("Щоб знайти кількість товарів на кожному складі, потрібно виконати наступні обчислення:")
print(f"Кількість товарів на першому складі: {total_products:,} - {second_and_third_warehouses:,} = {first_warehouse:,}")
print(f"Кількість товарів на другому складі: {first_and_second_warehouses:,} - {first_warehouse:,} = {second_warehouse:,}")
print(f"Кількість товарів на третьому складі: {total_products:,} - {first_and_second_warehouses:,} = {third_warehouse:,}")
print(f"Перевірка: {first_warehouse:,} + {second_warehouse:,} + {third_warehouse:,} = {total_warehouse:,} (повинно дорівнювати {total_products:,})")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
months_in_year = 12
half_year_months = 6
payment_months = months_in_year + half_year_months
monthly_payment = 1179
computer_price = payment_months * monthly_payment
print("Михайло разом з батьками вирішили купити комп’ютер, скориставшись послугою «Оплата частинами».")
print(f"Відомо, що сплачувати необхідно буде півтора року по {monthly_payment:,} грн/місяць.")
print("Щоб знайти вартість комп’ютера, потрібно помножити кількість місяців на щомісячну плату.")
print(f"Півтора року = {payment_months} місяців")
print(f"Вартість комп’ютера = {payment_months} * {monthly_payment:,} = {computer_price:,} грн")
print(f"Вартість комп’ютера становить {computer_price:,} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
remainder_a = 8019 % 8
remainder_b = 9907 % 9
remainder_c = 2789 % 5
remainder_d = 7248 % 6
remainder_e = 7128 % 5
remainder_f = 19224 % 9
print("Остача від ділення чисел:")
print(f"a) 8019 : 8 = {remainder_a}")
print(f"b) 9907 : 9 = {remainder_b}")
print(f"c) 2789 : 5 = {remainder_c}")
print(f"d) 7248 : 6 = {remainder_d}")
print(f"e) 7128 : 5 = {remainder_e}")
print(f"f) 19224 : 9 = {remainder_f}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
large_pizza_quantity = 4
medium_pizza_quantity = 2
juice_quantity = 4
cake_quantity = 1
water_quantity = 3

large_pizza_price = 274
medium_pizza_price = 218
juice_price = 35
cake_price = 350
water_price = 21

large_pizza_total = large_pizza_quantity * large_pizza_price
medium_pizza_total = medium_pizza_quantity * medium_pizza_price
juice_total = juice_quantity * juice_price
cake_total = cake_quantity * cake_price
water_total = water_quantity * water_price
total_order_price = large_pizza_total + medium_pizza_total + juice_total + cake_total + water_total
print("Іринка, готуючись до свого дня народження, склала список того, що їй потрібно замовити. Обчисліть, скільки грошей знадобиться для даного її замовлення.")
print(f"Піца велика: {large_pizza_quantity} шт. * {large_pizza_price} грн. = {large_pizza_total} грн")
print(f"Піца середня: {medium_pizza_quantity} шт. * {medium_pizza_price} грн. = {medium_pizza_total} грн")
print(f"Сік: {juice_quantity} шт. * {juice_price} грн. = {juice_total} грн")
print(f"Торт: {cake_quantity} шт. * {cake_price} грн. = {cake_total} грн")
print(f"Вода: {water_quantity} шт. * {water_price} грн. = {water_total} грн")
print(f"Загальна сума замовлення: {large_pizza_total} + {medium_pizza_total} + {juice_total} + {cake_total} + {water_total} = {total_order_price} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
photos_per_page = 8
full_pages = total_photos // photos_per_page
remaining_photos = total_photos % photos_per_page
total_pages = full_pages + (1 if remaining_photos > 0 else 0)
print(f"Ігор займається фотографією. Він вирішив зібрати всі свої {total_photos} фотографії та вклеїти в альбом.")
print(f"На одній сторінці може бути розміщено щонайбільше {photos_per_page} фото.")
print("Щоб знайти кількість сторінок, потрібно поділити загальну кількість фотографій на кількість фотографій на одній сторінці.")
print(f"{total_photos} : {photos_per_page} = {full_pages} повних сторінок")
if remaining_photos > 0:
    print(f"Залишилося {remaining_photos} фотографій, які не вмістилися на повних сторінках, тому потрібно додати ще одну сторінку.")
print(f"Загальна кількість сторінок: {total_pages}")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance_km = 1600
fuel_per_100_km = 9
tank_capacity = 48

hundred_km_segments = distance_km // 100
total_fuel_needed = hundred_km_segments * fuel_per_100_km

total_tanks_needed = total_fuel_needed // tank_capacity

if total_fuel_needed % tank_capacity != 0:
    total_tanks_needed += 1

refueling_stops = total_tanks_needed - 1

print(f"Відстань від Харкова до Будапешта становить {distance_km} км.")
print(f"{distance_km} км — це {hundred_km_segments} ділянок по 100 км.")
print(f"На кожні 100 км потрібно {fuel_per_100_km} літрів бензину.")
print(
    f"Для всієї подорожі потрібно: "
    f"{hundred_km_segments} × {fuel_per_100_km} = "
    f"{total_fuel_needed} літри бензину."
)
print(f"Один повний бак вміщує {tank_capacity} літрів.")
print(f"Для подорожі потрібно {total_tanks_needed} повні баки.")
print(
    "Один бак уже заправлений перед початком подорожі, "
    f"тому під час подорожі потрібно заїхати на заправку "
    f"{refueling_stops} рази."
)

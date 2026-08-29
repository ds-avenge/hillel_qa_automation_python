import pytest
import allure

# Task 1
# def is_palindrome(text: str) -> bool:
#   return text == text[::-1]

# class TestIsPalindrome:

#   @pytest.mark.parametrize("text, expected",
#   [
#     ("denys", False),
#     ("dmytro", False),
#     ("python", False),
#     ("QA", False),
#     ("", True),
#   ],
#   ids=[
#     "denys_is_not_palindrome",
#     "dmytro_is_not_palindrome",
#     "python_is_not_palindrome",
#     "QA_is_not_palindrome",
#     "empty_is_palindrome",
#       ]
#   )
#   def test_is_palindrome(self, text, expected):
#     actual_result = is_palindrome(text)

#     assert actual_result == expected, (
#       f"Expected {expected}, but got {actual_result} for text: {text}"
#     )

# Task 2
# Список містить словники - дані про ціну і тираж кожного з журналів. Скласти програму, яка визначає середню вартість журналів, тираж яких більше 10 000 примірників.

# journal_list = [
#     {"name": "National Geographic", "volume": 15000, "price": 7.99},
#     {"name": "Time", "volume": 20000, "price": 5.99},
#     {"name": "Vogue", "volume": 18000, "price": 6.99},
#     {"name": "Forbes", "volume": 10000, "price": 6.99},
#     {"name": "Scientific American", "volume": 9000, "price": 9.99},
#     {"name": "Sports Illustrated", "volume": 12000, "price": 4.99},
#     {"name": "The New Yorker", "volume": 11000, "price": 8.99},
#     {"name": "Cosmopolitan", "volume": 17000, "price": 5.99},
#     {"name": "Wired", "volume": 6000, "price": 7.99},
#     {"name": "Rolling Stone", "volume": 9000, "price": 6.99}
# ]

# def calculate_average_price(journals: list) -> float:
#   prices = [
#     journal["price"]
#     for journal in journals
#     if journal["volume"] > 10000
#   ]

#   return sum(prices) / len(prices) if prices else 0

# class TestCalculateAveragePrice:
#   def test_average_price_for_journals_with_volume_over_10000(self):
#     expected  = 6.82
#     actual_result = calculate_average_price(journal_list)
#     assert round(actual_result, 2) == expected, (
#       f"Expected average price: {expected}, but got {round(actual_result, 2)}"
#     )

#   def test_average_price_when_no_journals_match_condition(self):
#     journals = [
#       {"name": "Journal A", "volume": 5000, "price": 10.99},
#       {"name": "Journal B", "volume": 8000, "price": 7.99},
#     ]

#     expected = 0
#     actual_result = calculate_average_price(journals)
#     assert actual_result == expected, (
#       f"Expected average price: {expected}, but got {actual_result}"
#     )


# Task 3
# Біометрична авторизація. Функція виконує авторизацію на підставі отриманого списку словників даних та словника, отриманого з іншої функції від користувача.

# Параметри користувача: id - int, name - str, second_name - str, age - int
# Якщо дані від користувача співпадають з еталонними даними - користувач отримує повний доступ. Якщо відрізняється одне поле - доступ read-only, якщо більше - доступ заборонено.
# Функція повертає рівень доступу: full, read-only, forbidden

# варіант вхідних значень
database_users = [
    {"id": 1, "name": "John", "second_name": "Doe", "age": 30},
    {"id": 2, "name": "Jane", "second_name": "Joi", "age": 25},
]


def biometric_authorization(database_users: list[dict], user_input: dict) -> str:
    user_from_database = None
    for user in database_users:
        if user["id"] == user_input["id"]:
            user_from_database = user
            break

    if user_from_database is None:
        return "forbidden"

    mismatches = 0
    for key in ["id", "name", "second_name", "age"]:
        if user_from_database[key] != user_input[key]:
            mismatches += 1

    if mismatches == 0:
        return "full"
    elif mismatches == 1:
        return "read-only"
    else:
        return "forbidden"


class TestBiometricAuthorization:
    @pytest.mark.parametrize(
        "user_input, expected",
        [
            ({"id": 1, "name": "John", "second_name": "Doe", "age": 30}, "full"),
            ({"id": 1, "name": "John", "second_name": "Joi", "age": 30}, "read-only"),
            ({"id": 1, "name": "John", "second_name": "Joi", "age": 25}, "forbidden"),
            ({"id": 989, "name": "John", "second_name": "Doe", "age": 30}, "forbidden")
        ],
        ids=[
            "all_fields_match_full_access",
            "one_field_mismatch_read_only_access",
            "two_fields_mismatch_forbidden_access",
            "user_not_found_forbidden_access",
        ]
    )
    def test_biometric_authorization(self, user_input, expected):
        # actual_result = biometric_authorization(database_users, user_input)

        # assert actual_result == expected, (
        #   f"Expected access level: {expected}, but got {actual_result} for user input: {user_input}"
        # )
        with allure.step(f"Authorize user with input: {user_input}"):
            actual_result = biometric_authorization(
                database_users,
                user_input
            )

        with allure.step(
                f"Verify access level is {expected}"
        ):
            assert actual_result == expected, (
                f"Expected access level: {expected}, "
                f"but got {actual_result} for user input: {user_input}"
            )



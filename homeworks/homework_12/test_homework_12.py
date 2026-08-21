import pytest
from homework_12 import calculate_average,find_longest_word,find_substring,get_string_items,sum_of_even_numbers

class TestCalculateAverage:
    @pytest.mark.parametrize(
        "numbers, expected",
        [
            ([10, 20, 30], 20),
            ([1, 2, 3, 4, 5], 3),
            ([], 0),
        ],
        ids=[
            "average_of_10_20_30_is_20",
            "average_of_1_to_5_is_3",
            "empty_list_returns_0",
        ]
    )
    def test_calculate_average(self, numbers, expected):
        assert calculate_average(numbers) == expected
        # result = calculate_average(numbers)
        # print(f"\nAverage result: {result}")
        # assert result == expected


class TestFindLongestWord:
    def test_longest_word_in_list(self):
        assert find_longest_word(
            ["apple", "automation", "cherry"]
        ) == "automation"

    def test_longest_word_in_empty_list(self):
        assert find_longest_word([]) is None


class TestFindSubstring:
    @pytest.mark.parametrize(
        "text, substring, expected",
        [
            ("hello world", "world", 6),
            ("hello world", "python", -1),
            ("Python automation", "Python", 0),
        ],
        ids=[
            "substring_world_found_at_index_6",
            "substring_python_not_found",
            "substring_python_found_at_index_0",
        ]
    )
    def test_find_substring(self, text, substring, expected):
        assert find_substring(text, substring) == expected


class TestGetStringItems:
    def test_get_string_items_from_mixed_list(self):
        assert get_string_items(
            [1, "hello", 3.14, "world"]
        ) == ["hello", "world"]

    def test_get_string_items_from_empty_list(self):
        assert get_string_items([]) == []


class TestSumOfEvenNumbers:
    @pytest.mark.parametrize(
        "numbers, expected",
        [
            ([1, 2, 3, 4, 5], 6),
            ([1, 3, 5, 7], 0),
            ([2, 4, 6, 8], 20),
        ],
        ids=[
            "mixed_numbers_even_sum_is_6",
            "only_odd_numbers_sum_is_0",
            "only_even_numbers_sum_is_20",
        ]
    )
    def test_sum_of_even_numbers(self, numbers, expected):
        assert sum_of_even_numbers(numbers) == expected

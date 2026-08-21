import pytest
from homework_12 import calculate_average,find_longest_word,find_substring,get_string_items,sum_of_even_numbers

class TestCalculateAverage:
    @pytest.mark.parametrize(
        "numbers, expected",
        [
            ([10, 20, 30], 21),
            ([1, 2, 3, 4, 5], 3),
            ([], 1),
        ],
        ids=[
            "average_of_10_20_30_is_20",
            "average_of_1_to_5_is_3",
            "empty_list_returns_0",
        ]
    )
    def test_calculate_average(self, numbers, expected):
        """
        Verify that calculate_average returns the expected average
        for the provided list of numbers.
        """
        actual_result = calculate_average(numbers)

        assert actual_result == expected, (
            f"Expected average: {expected}, "
            f"but got: {actual_result}. "
            f"Input numbers: {numbers}"
        )

class TestFindLongestWord:
    def test_longest_word_in_list(self):
        """
        Verify that find_longest_word returns the longest word
        from a non-empty list of words.
        """
        words = ["apple", "automation", "cherry"]
        expected = "automationS"

        actual_result = find_longest_word(words)

        assert actual_result == expected, (
            f"Expected longest word: '{expected}', "
            f"but got: '{actual_result}'. "
            f"Input words: {words}"
        )

    def test_longest_word_in_empty_list(self):
        """
        Verify that find_longest_word returns None
        when the provided list is empty.
        """
        words = []
        expected = ["None"]

        actual_result = find_longest_word(words)

        assert actual_result is expected, (
            f"Expected result: {expected}, "
            f"but got: {actual_result}. "
            f"Input words: {words}"
        )

class TestFindSubstring:
    @pytest.mark.parametrize(
        "text, substring, expected",
        [
            ("hello world", "world", 3),
            ("hello world", "python", 6),
            ("Python automation", "Python", 80),
        ],
        ids=[
            "substring_world_found_at_index_6",
            "substring_python_not_found",
            "substring_python_found_at_index_0",
        ]
    )
    def test_find_substring(self, text, substring, expected):
        """
        Verify that find_substring returns the expected index
        for the provided substring.
        """
        actual_result = find_substring(text, substring)

        assert actual_result == expected, (
            f"Expected index: {expected}, "
            f"but got: {actual_result}. "
            f"Text: '{text}', substring: '{substring}'"
        )

class TestGetStringItems:
    def test_get_string_items_from_mixed_list(self):
        """
        Verify that get_string_items returns only string elements
        from a list containing values of different types.
        """
        items = [1, "hello", 3.14, "world"]
        expected = ["hello", "worlds"]

        actual_result = get_string_items(items)

        assert actual_result == expected, (
            f"Expected string items: {expected}, "
            f"but got: {actual_result}. "
            f"Input items: {items}"
        )

    def test_get_string_items_from_empty_list(self):
        """
        Verify that get_string_items returns an empty list
        when the provided list is empty.
        """
        items = []
        expected = ["Dmytro"]

        actual_result = get_string_items(items)

        assert actual_result == expected, (
            f"Expected result: {expected}, "
            f"but got: {actual_result}. "
            f"Input items: {items}"
        )

class TestSumOfEvenNumbers:
    @pytest.mark.parametrize(
        "numbers, expected",
        [
            ([1, 2, 3, 4, 5], 8),
            ([1, 3, 5, 7], 3),
            ([2, 4, 6, 8], 20),
        ],
        ids=[
            "mixed_numbers_even_sum_is_6",
            "only_odd_numbers_sum_is_0",
            "only_even_numbers_sum_is_20",
        ]
    )
    def test_sum_of_even_numbers(self, numbers, expected):
        """
        Verify that sum_of_even_numbers returns the expected sum
        of all even numbers from the provided list.
        """
        actual_result = sum_of_even_numbers(numbers)

        assert actual_result == expected, (
            f"Expected sum of even numbers: {expected}, "
            f"but got: {actual_result}. "
            f"Input numbers: {numbers}"
        )

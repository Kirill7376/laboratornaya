import pytest
from funcshun import factorial


def test_factorial_positive1():
    assert factorial(5) == 120


def test_factorial_positive2():
    assert factorial(6) == 720


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_large():
    assert factorial(10) == 3628800


def test_factorial_negative():
    assert factorial(-1) == "Факториал не определен"


def test_factorial_float():
    assert factorial(5.5) == "вводимое должно быть целым числом"


def test_factorial_string():
    assert factorial("abc") == "вводимое должно быть целым числом"


def test_factorial_very_large():
    assert factorial(15) == 1307674368000


def test_factorial_edge():
    assert factorial(2) == 2


from funcshun import is_prime


def test_is_prime_positive1():
    assert is_prime(7) == True


def test_is_prime_positive2():
    assert is_prime(13) == True


def test_is_prime_negative():
    assert is_prime(4) == False


def test_is_prime_one():
    assert is_prime(1) == False


def test_is_prime_large_prime():
    assert is_prime(7919) == True


def test_is_prime_large_not_prime():
    assert is_prime(7920) == False


def test_is_prime_zero():
    assert is_prime(0) == False


def test_is_prime_negative_number():
    assert is_prime(-5) == False


def test_is_prime_float():
    assert is_prime(5.5) == False


def test_is_prime_two():
    assert is_prime(2) == True

    from funcshun import find_unique

    def test_find_unique_positive1():
        assert find_unique([1, 2, 2, 2, 2]) == 1

    def test_find_unique_positive2():
        assert find_unique([4, 4, 4, 7, 4]) == 7

    def test_find_unique_string():
        assert find_unique(["asd", "asd", "asd", "asdf"]) == "asdf"

    def test_find_unique_mix():
        assert find_unique([7, "abc", 7, 7]) == "abc"

    def test_find_unique_float():
        assert find_unique([7.0, 7.0, 7.0, 8.0]) == 8.0

    def test_find_unique_empty():
        assert find_unique([]) is None

    def test_find_unique_no_unique():
        assert find_unique([5, 5, 5, 5]) is None

    def test_find_unique_multiple_unique():
        assert find_unique([1, 2, 3, 1, 1, 1]) == 2

    def test_find_unique_large_list():
        assert find_unique([1] * 1000 + [2]) == 2

    def test_find_unique_complex_objects():
        assert find_unique([[1, 2], [1, 2], [3, 4]]) == [3, 4]


 from funcshun import group_by_length


def test_group_by_length_positive1():
    assert group_by_length(["one", "two", "three", "four"]) == {3: ['one', 'two'], 5: ['three'], 4: ['four']}


def test_group_by_length_positive2():
    assert group_by_length(["cat", "dog", "elephant", "mouse"]) == {3: ['cat', 'dog'], 8: ['elephant'], 5: ['mouse']}


def test_group_by_length_empty():
    assert group_by_length([]) == {}


def test_group_by_length_same_length():
    assert group_by_length(["one", "two", "six"]) == {3: ['one', 'two', 'six']}


def test_group_by_length_mix():
    assert group_by_length(["one", "two", "threes", "four"]) == {3: ['one', 'two'], 6: ['threes'], 4: ['four']}


def test_group_by_length_numbers():
    assert group_by_length(["1", "22", "333", "4444"]) == {1: ['1'], 2: ['22'], 3: ['333'], 4: ['4444']}


def test_group_by_length_duplicates():
    assert group_by_length(["one", "one", "two"]) == {3: ['one', 'one', 'two']}


def test_group_by_length_with_empty_string():
    assert group_by_length(["", "one", "two"]) == {0: [''], 3: ['one', 'two']}


def test_group_by_length_long_words():
    assert group_by_length(["verylongword", "short"]) == {12: ['verylongword'], 5: ['short']}


def test_group_by_length_special_chars():
    assert group_by_length(["!@#", "$%^"]) == {3: ['!@#', '$%^']}

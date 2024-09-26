import pytest
from StringUtils import *

utils = StringUtils()


@pytest.mark.positive_test # Позитивные тесты для метода capitilize
@pytest.mark.parametrize('string, result', [
    ("skypro", "Skypro"),
    ("Skypro", "Skypro"),
    ("", ""),
    ("123", "123")
])
def test_capitilize(string, result):
    res = utils.capitilize(string)
    assert res == result


@pytest.mark.positive_test # Позитивные тесты для метода trim
@pytest.mark.parametrize('string, result', [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("   ", ""),
    ("", "")
])
def test_trim(string, result):
    res = utils.trim(string)
    assert res == result


@pytest.mark.positive_test # Тест для метода to_list
@pytest.mark.parametrize('string, delimiter, result', [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", ",", []),
    ("a,b,c", "|", ["a,b,c"])
])
def test_to_list(string, delimiter, result):
    res = utils.to_list(string, delimiter)
    assert res == result


@pytest.mark.positive_test # Тест на метод contains
@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "S", False),
    ("SkyPro", "", False)
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result


@pytest.mark.skip(reason="Функция требует доработки") # Тест с маркером пропуска для метода delete_symbol
def test_delete_symbol():
    res = utils.delete_symbol("SkyPro", "k")
    assert res == "SyPro"


@pytest.mark.parametrize('string, symbol, result', [  # Тест на метод starts_with
    ("SkyPro", "S", True),
    ("SkyPro", "P", False),
    ("", "S", False),
    ("SkyPro", "", False)
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


@pytest.mark.positive_test # Тест на метод end_with
@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "o", True),
    ("SkyPro", "y", False),
    ("", "o", False),
    ("SkyPro", "", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, result', [  # Тест на метод is_empty
    ("", True),
    ("   ", True),
    ("SkyPro", False),
    ("S", False)
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


@pytest.mark.positive_test # Тест на метод list_to_string
@pytest.mark.parametrize('lst, joiner, result', [
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    ([], ", ", "")
])
def test_list_to_string(lst, joiner, result):
    res = utils.list_to_string(lst, joiner)
    assert res == result


# Негативные сценарии:

# Пустая строка: ""
# Строка с пробелом: " "
# Значение None
# Пустой список: [] (если метод работает с массивами)

# Позитивные сценарии:

# Не пустая строка: "Тест"
# Числа как строка: "123"
# Строка с пробелами: "04 апреля 2023"


@pytest.mark.negative_test #для метода contains
@pytest.mark.parametrize('string, symbol, result', [
    ("", "T", False),         # Пустая строка
    (" ", " ", True),         # Строка с пробелом
    (None, "T", False),       # None значение
    ("SkyPro", None, False)   # None как символ
])
def test_contains_negative(string, symbol, result):
    if string is None or symbol is None:
        pytest.skip("None is not valid input")
    res = utils.contains(string, symbol)
    assert res == result

@pytest.mark.negative_test #для метода trim
@pytest.mark.parametrize('string, result', [
    ("", ""),        # Пустая строка
    ("   ", ""),     # Строка с пробелом
    (None, "")       # None значение
])
def test_trim_negative(string, result):
    if string is None:
        pytest.skip("None is not valid input")
    res = utils.trim(string)
    assert res == result

@pytest.mark.negative_test #для метода list_to_string
@pytest.mark.parametrize('lst, joiner, result', [
    ([], ", ", ""),          # Пустой список
    (None, ", ", ""),        # None значение
])
def test_list_to_string_negative(lst, joiner, result):
    if lst is None:
        pytest.skip("None is not valid input")
    res = utils.list_to_string(lst, joiner)
    assert res == result

### Позитивные тесты ###

@pytest.mark.positive_test #для метода contains
@pytest.mark.parametrize('string, symbol, result', [
    ("Тест", "Т", True),               # Обычная строка
    ("123", "2", True),                # Числа как строка
    ("04 апреля 2023", "апреля", True) # Строка с пробелами
])
def test_contains_positive(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

@pytest.mark.positive_test #для метода trim
@pytest.mark.parametrize('string, result', [
    ("Тест", "Тест"),                # Обычная строка
    ("   123", "123"),               # Числа с пробелами
    ("  04 апреля 2023", "04 апреля 2023")  # Строка с пробелами в начале
])
def test_trim_positive(string, result):
    res = utils.trim(string)
    assert res == result

@pytest.mark.positive_test #для метода list_to_string
@pytest.mark.parametrize('lst, joiner, result', [
    (["Тест", "123"], ", ", "Тест, 123"),    # Обычная строка и числа
    (["04", "апреля", "2023"], " ", "04 апреля 2023")  # Строка с пробелами
])
def test_list_to_string_positive(lst, joiner, result):
    res = utils.list_to_string(lst, joiner)
    assert res == result
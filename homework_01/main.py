"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return print([n**2 for n in nums])




# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers():
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    numbers_filtered = []

        if filter_type == ODD:
            numbers_filtered = filter(lambda number: (number % 2 != 0), numbers)
        elif filter_type == EVEN:
            numbers_filtered = filter(lambda number: (number % 2 == 0), numbers)
        elif filter_type == PRIME:

        numbers_filtered = filter(is_prime, numbers)

        return list(numbers_filtered)
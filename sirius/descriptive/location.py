import math


def mean(array: list[int | float]) -> float:
    return sum(array) / len(array)


def median(array: list[int | float]) -> int | float:
    array.sort()
    n = len(array)
    if n % 2 == 0:
        return (array[n // 2 - 1] + array[n // 2]) / 2
    else:
        return array[n // 2]


def mode(array: list[int | float]) -> list:
    frequencies: dict[int | float, int] = dict()
    for value in array:
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1

    max_frequency = max(frequencies.values())
    modes = list()
    for value, frequency in frequencies.items():
        if frequency == max_frequency:
            modes.append(value)
    return modes


def geometric_mean(array: list[int | float]) -> float:
    product = 1.0
    for value in array:
        product *= value
    return math.sqrt(product)


def root_mean_square(array: list[int | float]) -> float:
    sum_of_squares = 0.0
    for value in array:
        sum_of_squares += value ** 2
    return math.sqrt(sum_of_squares / len(array))

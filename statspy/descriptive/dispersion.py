import math

import statspy as sp


def pvariance(array: list[int | float]) -> float:
    mean = sp.mean(array)
    sum_of_squares = 0.0
    for i in array:
        sum_of_squares += (i - mean) ** 2
    return sum_of_squares / len(array)


def variance(array: list[int | float]) -> float:
    mean = sp.mean(array)
    sum_of_squares = 0.0
    for i in array:
        sum_of_squares += (i - mean) ** 2
    return sum_of_squares / (len(array) - 1)


def pstdev(array: list[int | float]) -> float:
    return math.sqrt(pvariance(array=array))


def stdev(array: list[int | float]) -> float:
    return math.sqrt(variance(array=array))


def range(array: list[int | float]) -> float:
    return max(array) - min(array)


def quartiles(array: list[int | float]) -> tuple[float, float, float]:
    raise NotImplementedError


def percentiles(array: list[int | float], percentiles: list[float]) -> list[float]:
    raise NotImplementedError


def interquartile_range(array: list[int | float]) -> float:
    raise NotImplementedError

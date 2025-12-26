import math

import statspy as sp


def variance(array: list[int | float], ddof: int = 0) -> float:
    mean = sp.mean(array)
    sum_of_squares = sum([(i - mean) ** 2 for i in array])
    return sum_of_squares / (len(array) - ddof)


def stdev(array: list[int | float], ddof: int = 0) -> float:
    return math.sqrt(variance(array=array, ddof=ddof))


def standard_error(array: list[int | float], ddof: int = 0) -> float:
    return stdev(array=array, ddof=ddof) / math.sqrt(len(array))


def range(array: list[int | float]) -> float:
    return max(array) - min(array)


def quartiles(array: list[int | float]) -> tuple[float, float, float]:
    raise NotImplementedError


def percentiles(array: list[int | float], percentiles: list[float]) -> list[float]:
    raise NotImplementedError


def interquartile_range(array: list[int | float]) -> float:
    raise NotImplementedError

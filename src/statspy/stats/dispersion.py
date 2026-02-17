import math

import statspy as sp


def variance(array: list[float], ddof: int = 0) -> float:
    mean = sp.stats.location.mean(array)
    sum_of_squares = sum([(i - mean) ** 2 for i in array])
    return sum_of_squares / (len(array) - ddof)


def stdev(array: list[float], ddof: int = 0) -> float:
    return math.sqrt(variance(array=array, ddof=ddof))


def standard_error(array: list[float], ddof: int = 0) -> float:
    return stdev(array=array, ddof=ddof) / math.sqrt(len(array))


def range(array: list[float]) -> float:
    return max(array) - min(array)


def quartiles(array: list[float]) -> tuple[float, float, float]:
    raise NotImplementedError


def percentiles(array: list[float], percentiles: list[float]) -> list[float]:
    raise NotImplementedError


def interquartile_range(array: list[float]) -> float:
    raise NotImplementedError

from statspy.descriptive.dispersion import stdev
from statspy.descriptive.location import mean

__all__ = ["correlation", "covariance"]


def covariance(x: list, y: list) -> float:
    if len(x) != len(y):
        raise ValueError("Lists x and y must have the same length.")
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    cov = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / n
    return cov


def correlation(x: list, y: list) -> float:
    if len(x) != len(y):
        raise ValueError("Lists x and y must have the same length.")

    covariance_xy = covariance(x, y)
    stdev_x = stdev(x)
    stdev_y = stdev(y)

    if stdev_x == 0 or stdev_y == 0:
        raise ValueError("Standard deviation of x or y is zero, correlation is undefined.")

    return covariance_xy / (stdev_x * stdev_y)

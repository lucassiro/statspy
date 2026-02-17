import statspy as sp


def covariance(x: list[float], y: list[float]) -> float:
    if len(x) != len(y):
        raise ValueError("Lists x and y must have the same length.")
    n = len(x)
    mean_x = sp.stats.location.mean(x)
    mean_y = sp.stats.location.mean(y)
    cov = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / n
    return cov


def correlation(x: list[float], y: list[float]) -> float:
    if len(x) != len(y):
        raise ValueError("Lists x and y must have the same length.")

    covariance_xy = covariance(x, y)
    stdev_x = sp.stats.dispersion.stdev(x)
    stdev_y = sp.stats.dispersion.stdev(y)

    if stdev_x == 0 or stdev_y == 0:
        raise ValueError("Standard deviation of x or y is zero, correlation is undefined.")

    return covariance_xy / (stdev_x * stdev_y)

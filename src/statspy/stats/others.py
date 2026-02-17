import statspy as sp


def confidence_interval_95(array: list) -> tuple[float, float]:
    mean_ = sp.stats.location.mean(array)
    std_ = sp.stats.dispersion.stdev(array)
    n = len(array)
    n_root = n**0.5

    a = mean_ - (1.96 * (std_ / n_root))
    b = mean_ + (1.96 * (std_ / n_root))

    return a, b

from statspy import mean, stdev

__all__ = ["confidence_interval_95"]


def confidence_interval_95(array: list) -> tuple[float, float]:
    mean_ = mean(array)
    std_ = stdev(array)
    n = len(array)
    n_root: float = n**0.5

    a = mean_ - (1.96 * (std_ / n_root))
    b = mean_ + (1.96 * (std_ / n_root))

    return a, b

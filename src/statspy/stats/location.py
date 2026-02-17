def mean(array: list[float]) -> float:
    return sum(array) / len(array)


def weighted_mean(samples: list[float], weights: list[float]) -> float:
    return sum([s * w for s, w in zip(samples, weights)]) / sum(weights)


def median(array: list[float]) -> float:
    array.sort()
    n = len(array)
    if n % 2 == 0:
        return (array[n // 2 - 1] + array[n // 2]) / 2
    else:
        return array[n // 2]


def mode(array: list[float]) -> list[float]:
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


def geometric_mean(array: list[float]) -> float:
    product = 1.0
    for value in array:
        product *= value
    return (product) ** 0.5


def root_mean_square(array: list[float]) -> float:
    sum_of_squares = sum([i**2 for i in array])
    return (sum_of_squares / len(array)) ** 0.5

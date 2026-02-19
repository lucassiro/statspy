import statspy as sp


class SimpleLinearRegression:
    def __init__(self) -> None:
        self.params = None
        self.intercept = None
        self.fitted = False

    def fit(self, x: list[float], y: list[float]) -> None:
        x_mean = sp.stats.location.mean(x)
        y_mean = sp.stats.location.mean(y)
        numerator = sum([(x_i - x_mean) * (y_i - y_mean) for x_i, y_i in zip(x, y)])
        denominator = sum([(x_i - x_mean) ** 2 for x_i in x])

        self.params = numerator / denominator
        self.intercept = y_mean - (self.params * x_mean)
        self.fitted = True

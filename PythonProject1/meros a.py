import math

class Statistics:
    def __init__(self, X, Y):
        if len(X) != len(Y):
            raise ValueError("Δείγματα πρέπει να είναι ίσου μεγέθους.")
        self.X = X
        self.Y = Y
        self.n = len(X)
        self.mean_X = self.calculate_mean(X)
        self.mean_Y = self.calculate_mean(Y)
        self.variance_X = self.calculate_variance(X, self.mean_X)
        self.variance_Y = self.calculate_variance(Y, self.mean_Y)
        self.std_X = math.sqrt(self.variance_X)
        self.std_Y = math.sqrt(self.variance_Y)
        self.covariance_X_Y = self.calculate_covariance(X, Y, self.mean_X, self.mean_Y)

    def calculate_mean(self, data):
        return sum(data) / len(data)

    def calculate_variance(self, data, mean):
        return sum((data[i] - mean) ** 2 for i in range(self.n)) / (self.n - 1)

    def calculate_covariance(self, X, Y, mean_X, mean_Y):
        return sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(self.n)) / self.n

    def get_statistics(self):
        return {
            "basic_statistics_X": {
                "mean": self.mean_X,
                "variance": self.variance_X,
                "std": self.std_X
            },
            "basic_statistics_Y": {
                "mean": self.mean_Y,
                "variance": self.variance_Y,
                "std": self.std_Y
            },
            "covariance_X_Y": self.covariance_X_Y
        }
try:
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 6, 8, 10]
    stats = Statistics(X, Y)
    print(stats.get_statistics())

    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 6, 8]
    stats = Statistics(X, Y)
    print(stats.get_statistics())

except ValueError as e:
    print(e)
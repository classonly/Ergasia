import numpy as np

class MatrixMultiplier:
    def __init__(self, A, B):
        self.A = np.array(A)
        self.B = np.array(B)

    def validate_dimensions(self):
        if self.A.shape[1] != self.B.shape[0]:
            raise ValueError("Δεν γίνεται πολλαπλασιασμός με τις διαστάσεις αυτών των πινάκων.")

    def multiply(self):
        try:
            self.validate_dimensions()
            return np.dot(self.A, self.B)
        except ValueError as e:
            print(e)
            return None

A = [[2, 1, 3],
     [3, 9, 4],
     [5, 10, 7]]

B = [[3, 4],
     [2, 5],
     [1, 6]]

try:
    multiplier = MatrixMultiplier(A, B)
    result = multiplier.multiply()
    if result is not None:
        print("Matrix Product:\n", result)
except Exception as e:
    print(e)


A = [[2, 1, 3],
     [3, 9, 4],
     [5, 10, 7]]

B = [[3, 4],
     [2, 5],
     [1]]

try:
    multiplier = MatrixMultiplier(A, B)
    result = multiplier.multiply()
    if result is not None:
        print("Matrix Product:\n", result)
except Exception as e:
    print(e)
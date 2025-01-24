class ListOperations:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def validate_lengths(self):
        if len(self.A) != len(self.B):
            raise ValueError("Οι λίστες A και B πρέπει να έχουν το ίδιο μήκος.")

    def perform_operations(self):
        try:
            self.validate_lengths()
            sum_of_lists = [a + b for a, b in zip(self.A, self.B)]
            prod_of_lists = [(a * b) ** 2 for a, b in zip(self.A, self.B)]
            return {
                "sum_of_lists": sum_of_lists,
                "prod_of_lists": prod_of_lists,
                "length_of_list_A": len(self.A),
                "length_of_list_B": len(self.B)
            }
        except ValueError:
            return {
                "sum_of_lists": False,
                "prod_of_lists": False,
                "length_of_list_A": len(self.A),
                "length_of_list_B": len(self.B)
            }

A = [2, 2, 2, 2, 2, 2]
B = [3, 3, 3, 3, 3, 3]

list_ops = ListOperations(A, B)
print(list_ops.perform_operations())


A = [2, 2, 2, 2, 2, 2]
B = [3, 3]

list_ops = ListOperations(A, B)
print(list_ops.perform_operations())
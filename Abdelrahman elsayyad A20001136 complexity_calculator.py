
import numpy as np

# Utility class for complexity calculations
class ComplexityCalculator:
    def __init__(self, matrix, neighbors):
        self.matrix = matrix
        self.rows, self.columns = matrix.shape
        self.neighbors = neighbors

    def calculate_user_based_time(self):
        similarity_time = self.rows ** 2 * self.columns
        prediction_time = self.rows * self.neighbors * self.columns
        return similarity_time + prediction_time

    def calculate_item_based_time(self):
        similarity_time = self.columns ** 2 * self.rows
        prediction_time = self.rows * self.neighbors * self.columns
        return similarity_time + prediction_time

    def calculate_user_based_space(self):
        matrix_space = self.rows * self.columns
        similarity_space = self.rows ** 2
        return matrix_space + similarity_space

    def calculate_item_based_space(self):
        matrix_space = self.rows * self.columns
        similarity_space = self.columns ** 2
        return matrix_space + similarity_space

# Function to compute sparsity
def compute_sparsity(matrix):
    total_elements = matrix.size
    non_zero_elements = np.count_nonzero(matrix)
    return 1 - (non_zero_elements / total_elements)

# Example matrix and neighbors
matrix = np.array([
    [8, 2, 0, 1],
    [4, 0, 0, 4],
    [1, 4, 0, 0],
    [0, 1, 5, 4],
    [2, 0, 6, 8]
])
neighbors = 2

# Instantiate the calculator and compute results
calculator = ComplexityCalculator(matrix, neighbors)

user_time = calculator.calculate_user_based_time()
item_time = calculator.calculate_item_based_time()
user_space = calculator.calculate_user_based_space()
item_space = calculator.calculate_item_based_space()
sparsity = compute_sparsity(matrix)

# Print results
print(f"Sparsity of the matrix: {sparsity:.2f}")
print(f"User-Based Time Complexity: {user_time} operations")
print(f"Item-Based Time Complexity: {item_time} operations")
print(f"User-Based Space Complexity: {user_space} units of memory")
print(f"Item-Based Space Complexity: {item_space} units of memory")

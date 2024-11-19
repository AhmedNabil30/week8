# -*- coding: utf-8 -*-
"""lab_irs_task.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d0PAFDluUAVNaFkVjDjqJPgEQbP6z8Zo
"""

def time_complexity_ubcf(n, m, k):

    # Time for calculating similarities: O(n^2 * m)
    similarity_time = n ** 2 * m

    # Time for generating predictions: O(n * k * m)
    prediction_time = n * k * m

    total_time = similarity_time + prediction_time
    return total_time

def time_complexity_ibcf(n, m, k):

    # Time for calculating similarities: O(m^2 * n)
    similarity_time = m ** 2 * n

    # Time for generating predictions: O(n * k * m)
    prediction_time = n * k * m

    total_time = similarity_time + prediction_time
    return total_time

def space_complexity_ubcf(n, m):

    # Space for user-item matrix: O(n * m)
    user_item_space = n * m

    # Space for similarity matrix: O(n^2)
    similarity_space = n ** 2

    total_space = user_item_space + similarity_space
    return total_space

def space_complexity_ibcf(n, m):

    # Space for user-item matrix: O(n * m)
    user_item_space = n * m

    # Space for similarity matrix: O(m^2)
    similarity_space = m ** 2

    total_space = user_item_space + similarity_space
    return total_space

def calculate_sparsity(user_item_matrix):

    # Total number of entries (n * m)
    total_entries = user_item_matrix.size

    # Count the number of non-zero entries in the matrix
    non_zero_entries = np.count_nonzero(user_item_matrix)

    # Calculate sparsity
    sparsity = 1 - (non_zero_entries / total_entries)

    return sparsity

# Example user-item matrix (rows: users, columns: items)
import numpy as np
user_item_matrix = np.array([
    [5, 0, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 1, 5, 4],
    [0, 0, 5, 4]
])

n_users, n_items = user_item_matrix.shape
k_neighbors = 2  # Number of nearest neighbors to consider for predictions

# Calculate Sparsity
sparsity = calculate_sparsity(user_item_matrix)
print(f"Sparsity of the user-item matrix: {sparsity:.2f}")

# Calculate Time Complexity for User-Based Collaborative Filtering (UBCF)
ubcf_time = time_complexity_ubcf(n_users, n_items, k_neighbors)
print(f"User-Based CF Time Complexity: {ubcf_time} operations")

# Calculate Time Complexity for Item-Based Collaborative Filtering (IBCF)
ibcf_time = time_complexity_ibcf(n_users, n_items, k_neighbors)
print(f"Item-Based CF Time Complexity: {ibcf_time} operations")

# Calculate Space Complexity for User-Based Collaborative Filtering (UBCF)
ubcf_space = space_complexity_ubcf(n_users, n_items)
print(f"User-Based CF Space Complexity: {ubcf_space} units of memory")

# Calculate Space Complexity for Item-Based Collaborative Filtering (IBCF)
ibcf_space = space_complexity_ibcf(n_users, n_items)
print(f"Item-Based CF Space Complexity: {ibcf_space} units of memory")
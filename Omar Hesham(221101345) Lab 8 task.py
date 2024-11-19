
def calculate_time_complexity_ubcf(num_users, num_items, num_neighbors):
    
    
    similarity_time = num_users ** 2 * num_items

    
    prediction_time = num_users * num_neighbors * num_items

    return similarity_time + prediction_time

def calculate_time_complexity_ibcf(num_users, num_items, num_neighbors):
    
    
    similarity_time = num_items ** 2 * num_users

    
    prediction_time = num_users * num_neighbors * num_items

    return similarity_time + prediction_time

def calculate_space_complexity_ubcf(num_users, num_items):
    
    
    user_item_space = num_users * num_items

    
    similarity_space = num_users ** 2

    return user_item_space + similarity_space

def calculate_space_complexity_ibcf(num_users, num_items):
    
    
    user_item_space = num_users * num_items

    
    similarity_space = num_items ** 2

    return user_item_space + similarity_space

def calculate_sparsity(matrix):
    
    total_elements = matrix.size
    non_zero_elements = np.count_nonzero(matrix)
    sparsity = 1 - (non_zero_elements / total_elements)
    return sparsity


import numpy as np
user_item_matrix = np.array([
    [4, 0, 1, 0],
    [0, 3, 0, 2],
    [1, 5, 0, 0],
    [0, 0, 2, 4],
    [0, 4, 0, 3]
])


num_users, num_items = user_item_matrix.shape
num_neighbors = 3  


matrix_sparsity = calculate_sparsity(user_item_matrix)
print(f"Sparsity of the user-item matrix: {matrix_sparsity:.2f}")


ubcf_time_complexity = calculate_time_complexity_ubcf(num_users, num_items, num_neighbors)
print(f"User-Based CF Time Complexity: {ubcf_time_complexity} operations")


ibcf_time_complexity = calculate_time_complexity_ibcf(num_users, num_items, num_neighbors)
print(f"Item-Based CF Time Complexity: {ibcf_time_complexity} operations")


ubcf_space_complexity = calculate_space_complexity_ubcf(num_users, num_items)
print(f"User-Based CF Space Complexity: {ubcf_space_complexity} units of memory")

ibcf_space_complexity = calculate_space_complexity_ibcf(num_users, num_items)
print(f"Item-Based CF Space Complexity: {ibcf_space_complexity} units of memory")
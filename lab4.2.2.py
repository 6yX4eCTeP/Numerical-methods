import numpy as np

N = 5  
M = 4  

matrix = np.random.randint(1, 11, size=(N, M))
print("Матриця A:")
print(matrix)
total_sum = np.sum(matrix)
row_sums = np.sum(matrix, axis=1)
row_fractions = row_sums / total_sum
print("\nСума всіх елементів матриці: ", total_sum)
print("\nСуми елементів кожного рядка:")
print(row_sums)
print("\nДолі сум кожного рядка відносно загальної суми:")
print(row_fractions)
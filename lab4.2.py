# №2
import numpy as np
matrix2 = np.array([[-1, 0, 2],
                   [0, 1, 0],
                   [1, 2, -1]])

matrix_squared = np.dot(matrix2, matrix2)

print("Матриця після піднесення до квадрату:")
print(matrix_squared)
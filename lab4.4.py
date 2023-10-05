# №4
import numpy as np
matrix3 = np.array([[2, 3, 4],
                   [1, 0, 6],
                   [7, 8, 9]])

determinant = np.linalg.det(matrix3)
print("Визначник матриці:")
print(determinant)
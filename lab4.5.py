# №5
import numpy as np
def calculate_determinant(matrix5):
    determinant = np.linalg.det(matrix5)
    return determinant

matrix5 = np.array([[1, 2, 3, 4],
                   [-2, 1, -4, 3],
                   [3, -4, -1, 2],
                   [4, 3, -2, -1]])

determinant = calculate_determinant(matrix5)

print("Визначник матриці:")
print(determinant)
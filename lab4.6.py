# №6
import numpy as np
def calculate_inverse_matrix(matrix6):
    try:
        inverse_matrix = np.linalg.inv(matrix6)
        return inverse_matrix
    except np.linalg.LinAlgError:
        return None

matrix6 = np.array([[1, 2, -3],
                   [0, 1, 2],
                   [0, 0, 1]])

inverse_matrix = calculate_inverse_matrix(matrix6)
if inverse_matrix is not None:
    print("Обернена матриця:")
    print(inverse_matrix)
else:
    print("Матриця є сингулярною і не має оберненої матриці.")
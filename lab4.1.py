import numpy as np

def calculate_matrix_C(A, B):
    AB = np.dot(A, B)
    BA = np.dot(B, A)
    C = AB - BA
    return C
A = np.array([[1, 2], [4, -1]])
B = np.array([[2, -3], [-4, 1]])
C = calculate_matrix_C(A, B)

print("Матриця C:")
print(C)
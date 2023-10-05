# №8
import numpy as np

A = np.array([[1, -2, 1], [2, -1, 1], [3, 2, 2]])

B = np.array([4, 3, 2])

X = np.linalg.solve(A, B)

print("Розв'язок з solve():", X)
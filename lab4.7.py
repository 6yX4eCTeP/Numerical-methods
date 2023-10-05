# №7
import numpy as np
matrix7 = np.array([[1, 2, 3, 4],
                   [3, -1, 2, 5],
                   [1, 2, 3, 4],
                   [1, 3, 4, 5]])

rank = np.linalg.matrix_rank(matrix7)

print("Ранг матриці:", rank)
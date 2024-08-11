import numpy as np

A = np.array([[1,2,3], [4, 51, 6], [7, 8, 9]])
B = A + A.T
# Rango de una matriz
print("\nnp.linalg.matrix_rank(A) =", np.linalg.matrix_rank(B))
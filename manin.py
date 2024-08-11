import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

#Matriz resultante de la operación $ (2A + B^T)

C = (2*A) + B.transpose((1, 0))

print(C)
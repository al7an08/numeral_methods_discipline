from math import sqrt
import numpy as np
from numpy import array
 
A = np.array([4,-1,1,1,6,2,-1,-2,5], dtype=float).reshape(3,-1)
b = np.array([4,9,2], dtype=float)

def method_of_zeidel(A, b):
    m = len(A)
    x = [.0 for i in range(m)]
    Iteration = 0
    converge = False
    pogr = 0.
    while not converge:
        x_new = np.copy(x)
        for i in range(m):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, m))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        pogr = sum(abs(x_new[i] - x[i])  for i in range(m))
        converge =  pogr < 1e-6
        Iteration += 1
        x = x_new

    return [Iteration, x, pogr]


print(method_of_zeidel(A,b))
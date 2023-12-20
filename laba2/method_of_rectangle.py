import numpy as np


#Метод прямоугольника

def rectangle_method(A, b):
    n = len(b)
    augmented_matrix = np.column_stack((A, b))

    for k in range(n):
        for i in range(k+1, n):
            factor = augmented_matrix[i, k] / augmented_matrix[k, k]
            augmented_matrix[i, k:] -= factor * augmented_matrix[k, k:]

    x = np.zeros(n)
    x[n-1] = augmented_matrix[n-1, n] / augmented_matrix[n-1, n-1]

    for i in range(n-2, -1, -1):
        x[i] = (augmented_matrix[i, n] - np.dot(augmented_matrix[i, i+1:n], x[i+1:])) / augmented_matrix[i, i]

    return x



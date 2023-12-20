import numpy as np

def gaussian_elimination(A, b):
    n = len(b)
    
    # Прямой ход метода Гаусса
    for i in range(n-1):
        # Находим максимальный элемент в столбце
        max_index = np.argmax(np.abs(A[i:, i])) + i
        if max_index != i:
            A[[i, max_index]] = A[[max_index, i]]
            b[[i, max_index]] = b[[max_index, i]]
        
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
    
    # Обратный ход метода Гаусса
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    return x

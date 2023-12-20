import numpy as np

def jacobi_rotation(matrix, tolerance=1e-6, max_iterations=1000):
    n = matrix.shape[0]
    eigenvectors = np.eye(n)

    for _ in range(max_iterations):
        max_value = -np.inf
        p, q = 0, 0

        for i in range(n):
            for j in range(i + 1, n):
                if abs(matrix[i, j]) > max_value:
                    max_value = abs(matrix[i, j])
                    p, q = i, j

        if max_value < tolerance:
            break

        d = np.sqrt((matrix[p, p] - matrix[q, q])**2 + 4 * matrix[p, q]**2)
        c = np.sqrt(0.5 * (1 + abs(matrix[p, p] - matrix[q, q]) / d))
        s = np.sign(matrix[p, q] * (matrix[p, p] - matrix[q, q])) * np.sqrt(0.5 * (1 - abs(matrix[p, p] - matrix[q, q]) / d))

        rotation_matrix = np.eye(n)
        rotation_matrix[p, p] = c
        rotation_matrix[q, q] = c
        rotation_matrix[p, q] = s
        rotation_matrix[q, p] = -s

        matrix = rotation_matrix.T @ matrix @ rotation_matrix
        eigenvectors = eigenvectors @ rotation_matrix

    eigenvalues = np.diag(matrix)
    eigenvectors = eigenvectors

    return eigenvalues, eigenvectors

A = np.array([[5, 1, 2], [1, 4, 1], [2, 1, 3]])

eigenvalues, eigenvectors = jacobi_rotation(A)
print("Eigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)
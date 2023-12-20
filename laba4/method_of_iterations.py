import numpy as np

def power_iteration(A, num_simulations: int):
    x = np.random.rand(A.shape[1])

    for _ in range(num_simulations):
        y = np.dot(A, x)
        x_new = y / np.linalg.norm(y)

        if np.linalg.norm(x_new - x) < 1e-6:
            break

        x = x_new

    eigenvalue = np.dot(x_new, np.dot(A, x_new)) / np.dot(x_new, x_new)

    return x_new, eigenvalue


A = np.array([[2,-1,1],
              [-1,2,-1],
              [0,0,1]])
eigenvalue, eigenvector = power_iteration(A, 1000)
print(f"Собственное число: {eigenvector}")
print(f"Собственный вектор: {eigenvalue}")
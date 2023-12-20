import numpy as np



def method_of_simple_iterations(A, B, eps = 1e-4):
    a = np.array(A)
    diag = (1/np.diag(a)).reshape(-1,1)
    a[np.diag_indices_from(a)] = 0.
    a = np.hstack((-a, np.array(B).reshape(-1, 1))) * diag
    x = a[:,-1].ravel()
    x = np.append(x, 1)
    
    tmp = x.copy() + eps
    cnt = 0
    while abs(x-tmp).sum() > eps:
        tmp = x.copy()
        x = a.dot(x)
        x = np.append(x, 1)
        cnt += 1

    return x[:-1].round()

    

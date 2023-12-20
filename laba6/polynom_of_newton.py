# Многочлен Ньютона для неравномерной сетки

def split_diff(X, Y):
    if len(X) == 2:
        r = (Y[-1] - Y[0])/(X[-1] - X[0])
        return r
    elif len(X) > 2:
        r = (split_diff(X[1:], Y[1:]) - split_diff(X[0:-1], Y[0:-1]))/(X[-1] - X[0])
        return r
def construct_polynom(X, Y, x):
    res = Y[0]
    mult = 1
    for i in range(len(X)-1):
        mult*=(x-X[i])
        diff = split_diff(X[:i+2], Y[:i+2])
        res += mult*diff
    return res

# Многочлен Ньютона для равномерной сетки

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def newton_interpolation(x_values, y_values, x):
    n = len(x_values) - 1
    result = 0
    for i in range(n+1):
        if(i > 0):
            term = pow((y_values[i] - y_values[i-1]), i+1)
        else:
            term = 1
        for j in range(i):
            term *= (x - x_values[j])
            term /= factorial(j + 1) 
        result += term

    return result
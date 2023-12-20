# Фукнция, с которой мы будем работать
def func(x):
    return ((x - 3) ** 3) * (x - 2) * (x + 7)


# Производная этой фунцкии
def func_derivative(x):
    return 3 * ((x - 3) ** 2) * (x - 2) * (x + 7) + ((x - 3) ** 3) * (x + 7) + ((x - 3) ** 3) * (x - 2)


def init_approx_deriv(x0, q, func):
    return (func(x0) - func(x0-q))/q

def k_approx_deriv(xk, xk_0, func):
    return (func(xk) - func(xk_0))/(xk - xk_0 + 1e-3)

#Метод секущих

def secant_method(func, q=1e-6, x0=-10, e=1e-6):
    a = func(x0)
    start_x1 = x0 - a/(init_approx_deriv(x0, q, func))
    roots = set()
    while x0 <= 10:
        x1 = start_x1 - func(start_x1)/k_approx_deriv(start_x1, x0, func)
        if abs(x1 - start_x1) < e:
            roots.add(round(x1,2))
        x0 = start_x1
        start_x1 = x1
    return roots


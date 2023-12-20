# Фукнция, с которой мы будем работать
def func(x):
    return ((x - 3) ** 3) * (x - 2) * (x + 7)


# Производная этой фунцкии
def func_derivative(x):
    return 3 * ((x - 3) ** 2) * (x - 2) * (x + 7) + ((x - 3) ** 3) * (x + 7) + ((x - 3) ** 3) * (x - 2)

#Метод Ньютона

def newton_method(func, func_derivative, initial, e=1e-6, max_iter=100):
    roots = set()
    
    for x0 in initial:
        x = x0
        iteration = 0

        while abs(func(x)) > e and iteration < max_iter:
            x = x - func(x) / func_derivative(x)
            iteration += 1

        if abs(func(x)) <= e:
            roots.add(round(x,2))
    
    return roots


import random

# Фукнция, с которой мы будем работать
def func(x):
    return ((x - 3) ** 3) * (x - 2) * (x + 7)


# Производная этой фунцкии
def func_derivative(x):
    return 3 * ((x - 3) ** 2) * (x - 2) * (x + 7) + ((x - 3) ** 3) * (x + 7) + ((x - 3) ** 3) * (x - 2)

# Метод Ньютона-Бройдена

def newton_broyden_method(func, func_derivative, x0, c=0.5, e=1e-6, max_iterations=100):
    x = x0
    iteration = 0
    while iteration < max_iterations:
        x_next = x - c * func(x) / func_derivative(x)
        if abs(func(x_next)) < e:
            return x_next
        x = x_next
        iteration += 1

x0 = -10
roots = set()
for _ in range(100):
    x0 = random.uniform(-10, 10)
    try:
        root = newton_broyden_method(func, func_derivative, x0)
        roots.add(round(root,2))
    except Exception as e:
        break


print("Найденные корни:", roots)

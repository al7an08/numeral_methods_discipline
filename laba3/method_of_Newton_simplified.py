import random

# Фукнция, с которой мы будем работать
def func(x):
    return ((x - 3) ** 3) * (x - 2) * (x + 7)


# Производная этой фунцкии
def func_derivative(x):
    return 3 * ((x - 3) ** 2) * (x - 2) * (x + 7) + ((x - 3) ** 3) * (x + 7) + ((x - 3) ** 3) * (x - 2)

#Упрощенный метод Ньютона

def simplified_newton_method(x0, e=1e-6, max_iter=1000):
    iteration = 0
    once_dir = func_derivative(x0)
    while iteration < max_iter:
        x1 = x0 - func(x0) / once_dir

        if abs(x1 - x0) < e:
            return x1
        
        x0 = x1 
        iteration += 1

    raise Exception("Упрощенный метод Ньютона не сошелся после максимального числа итераций.")

max_iterations = 10000
roots = set()
while True:
    initial = random.uniform(-5, 5)
    
    try:
        root = simplified_newton_method(initial,  max_iter=max_iterations)
        roots.add(round(root,2))
    except Exception as e:
        break

print("Найденные корни:", roots)
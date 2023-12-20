# Метод половинного деления


def f(x):
    return (x-2)*((x-1)**3)*((x-3)**2)


def method_of_half_dividing(func, x0, x1, e):
    for i in range(20):
        x2 = (x0 + x1) / 2
        if func(x2) == 0:
            return x2
        if abs(func(x0) - func(x1)) < e:
            return x2
        if func(x0) * func(x2) < 0:
            x1 = x2
            continue
        if func(x2) * func(x1) < 0:
            x0 = x2
    return x2


# print(f(0))
# print(f(1.5))
# print(f(1.5/2))
ans = method_of_half_dividing(f, 0, 1.5, 0.01)

print(ans)

print(f(ans))


ans = method_of_half_dividing(f, 1.5, 5, 0.01)

print(ans)

print(f(ans))

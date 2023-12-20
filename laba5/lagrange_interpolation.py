def lagrange_interpolation(x, x_values, y_values) -> int:
    """
    Вычисляет значение интерполяционного многочлена Лагранжа в заданной точке.

    :param x: Точка, в которой нужно вычислить значение многочлена.
    :param x_values: Список значений аргумента.
    :param y_values: Список значений функции.
    :return: Значение интерполяционного многочлена Лагранжа в точке x.
    """

    result = 0

    for i in range(len(x_values)):
        term = y_values[i]
        for j in range(len(x_values)):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result


# Пример использования:

# Задаем таблицу аргумент-значение (пример)
x_values_arr = [2, 3, 4, 5]
y_values_arr = [7, 5, 8, 7]

# Вычисляем значение интерполяционного многочлена Лагранжа в точке x
x_to_evaluate = 2.5
interpolated_value = lagrange_interpolation(
    x_to_evaluate, x_values_arr, y_values_arr)

print(
    f"Значение интерполяционного многочлена в точке {x_to_evaluate}: {interpolated_value}")
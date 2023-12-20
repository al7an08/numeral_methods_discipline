def find_two_nearest_points(x_values, x):

    """
    Находит ближайшую левую и ближайшую правую точки из массива x_values для x.

    :param x_values: Список значений сеточной функции.
    :param x: Точка, для которой надо найти ближайшие точки из x_values.
    :return: (l, l_val, r, r_val) - (индекс в x_values левой ближайшей точки, значение левой ближайшей точки, индекс в x_values правой ближайшей точки, значение правой ближайшей точки)
    """

    min_r_dist = float('inf')
    min_l_dist = float('inf')
    l_val = r_val = 0
    l = r = 0
    for i, x_i in enumerate(x_values):
        d = abs(x_i - x)
        if d < min_l_dist and x_i < x:
            l_val = x_i
            min_l_dist = d
            l = i
        elif d < min_r_dist and x_i > x:
            min_r_dist = d
            r_val = x_i
            r = i
    return (l, l_val, r, r_val)

def linear_inperpolation(x_values, y_values, x):
    """
    Выполняет линейную интерполяцию. 

    :param x_values: Список значений x (узлов интерполяции).
    :param y_values: Список значений y (значений функции в узлах интерполяции).
    :param x: Точка, в которой производится интерполяция.
    :return: Значение интерполянта в точке x.
    """
    
    if len(x_values) != len(y_values):
        raise ValueError("Длины x_values и y_values должны совпадать.")
        
    if len(x_values) == 0 or len(y_values) == 0:
        return 0

    for i,x_i in enumerate(x_values):
        if  x_i == x:
            return y_values[i]

    l, l_val, r, r_val = find_two_nearest_points(x_values, x)
        
    result = y_values[l]*(x - r_val)/(l_val - r_val) + y_values[r]*(x - l_val)/(r_val - l_val)

    return result
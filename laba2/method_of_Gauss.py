#Метод Гаусса (Единичного деления)

n = int(input('Введите количество уравнений\n'))

a = []

j = 0

print('Введите коэффициенты уравнений\n')

for i in range(n):
    a.append([float(j) for j in input().split()])

k = 1

x=[0]*n
while k < n:
    j = k
    while j < n:
        m = a[j][k - 1] / a[k - 1][k - 1]
        i = 0
        while i < n + 1:
            a[j][i] = a[j][i] - m * a[k - 1][i]
            i += 1
        j += 1
    k += 1

i = n - 1

if a[i][i] == 0:
    print('Система не имеет решений или имеет бесконечно множество решений')
else:
    while i >= 0:
        x[i] = a[i][n] / a[i][i]
        c = n - 1
        while c > i:
            x[i] = x[i] - (a[i][c] * x[c] / a[i][i])
            c -= 1
        i -= 1
    print('Корни СЛАУ:\n', x)
input()
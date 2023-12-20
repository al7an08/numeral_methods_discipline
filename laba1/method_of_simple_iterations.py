# Метод простых итераций

def square_root_iter(a, eps = 0.001):
  x = a/2
  while (x ** 2 - a > eps):
    x = (x + a/x)/2

  return x


print(square_root_iter(9))
print(square_root_iter(16))
print(square_root_iter(25))
print(square_root_iter(5))
from scipy import integrate
import numpy as np

def f(x):
    return np.cos(x**2) / (x + 1)

a = 0.4
b = 1.2
n = 8
dx = (b - a) / n

result_simpson = 0
for i in range(n):
    x0 = a + i * dx
    x1 = x0 + dx / 2
    x2 = x0 + dx
    result_simpson += (dx / 6) * (f(x0) + 4*f(x1) + f(x2))

result_quad, _ = integrate.quad(f, a, b)

print("Метод Сімпсона:", round(result_simpson, 4))
print("Вбудований метод (quad):", round(result_quad, 4))

# Перевірка за допомогою scipy
tolerance = 0.0001
assert np.abs(result_simpson - result_quad) < tolerance, "Результати не збігаються з необхідною точністю."
print("Перевірка пройшла успішно.")

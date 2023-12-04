from scipy import integrate
import numpy as np

def f(x):
    return 1 / np.sqrt(x**2 + 2.5)

a = 1.6
b = 2.2
n = 20
dx = (b - a) / n

result_trapezoidal = 0.5 * (f(a) + f(b)) + sum(f(a + i * dx) for i in range(1, n))
result_trapezoidal *= dx

result_quad, _ = integrate.quad(f, a, b)

print("Метод трапецій:", round(result_trapezoidal, 4))
print("Вбудований метод (quad):", round(result_quad,4))

# Перевірка за допомогою scipy
tolerance = 0.0001
assert np.abs(result_trapezoidal - result_quad) < tolerance, "Результати не збігаються з необхідною точністю."
print("Перевірка пройшла успішно.")
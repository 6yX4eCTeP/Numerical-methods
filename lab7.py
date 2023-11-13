import numpy as np
import matplotlib.pyplot as plt


xi = np.array([3.50, 3.55, 3.60, 3.65, 3.70, 3.75, 3.80, 3.85, 3.90, 3.95, 4.00])
yi = np.array([33.1154, 34.8133, 36.5982, 38.4747, 40.4473, 42.5211, 44.7012, 46.9931, 49.4024, 51.9354, 54.5982])

x_values = [3.522, 3.905, 3.643, 4.005, 3.675, 3.852]


def divided_differences(xi, yi):
    n = len(xi)
    table = np.zeros((n, n))
    table[:, 0] = yi

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (xi[i + j] - xi[i])

    return table[0]

coefficients = divided_differences(xi, yi)

def interpolate(x, xi, coefficients):
    n = len(xi)
    result = coefficients[0]
    for i in range(1, n):
        term = coefficients[i]
        for j in range(i):
            term *= (x - xi[j])
        result += term
    return result

f_x_values = [interpolate(x, xi, coefficients) for x in x_values]

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(xi, yi, 'ro', label='Таблиця точок')
plt.plot(x_values, f_x_values, 'bs', label='Значення f(x)')
x_range = np.linspace(min(xi), max(xi), 400)
y_range = [interpolate(x, xi, coefficients) for x in x_range]
plt.plot(x_range, y_range, 'g-', label='Інтерполяційна функція')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.title('Графік інтерполяційної функції')
plt.show()

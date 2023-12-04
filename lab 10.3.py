import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return math.cos(2 * x) + 2

# Задані значення xi та відповідних значень f(xi)
xi_values = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
yi_values = np.array([f(xi) for xi in xi_values])

# Метод найменших квадратів для параболи (квадратичної апроксимації)
A_quadratic = np.vstack([xi_values**2, xi_values, np.ones(len(xi_values))]).T
a_quadratic, b_quadratic, c_quadratic = np.linalg.lstsq(A_quadratic, yi_values, rcond=None)[0]

# Генерування точок для графіку параболи
x_points = np.linspace(0, 1, 100)
y_quadratic = a_quadratic * x_points**2 + b_quadratic * x_points + c_quadratic

# Побудова графіку параболи
plt.scatter(xi_values, yi_values, label='Точки')
plt.plot(x_points, y_quadratic, label=f'Парабола: y = {a_quadratic:.4f}x^2 + {b_quadratic:.4f}x + {c_quadratic:.4f}', color='green')

# Додаткові параметри графіку
plt.title('Найменший квадрат: парабола')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
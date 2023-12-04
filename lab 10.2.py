import numpy as np
import matplotlib.pyplot as plt
import math
def f(x):
    return math.cos(2 * x) + 2
xi_values = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
yi_values = np.array([f(xi) for xi in xi_values])

A_linear = np.vstack([xi_values, np.ones(len(xi_values))]).T
m_linear, c_linear = np.linalg.lstsq(A_linear, yi_values, rcond=None)[0]

A_quadratic = np.vstack([xi_values**2, xi_values, np.ones(len(xi_values))]).T
a_quadratic, b_quadratic, c_quadratic = np.linalg.lstsq(A_quadratic, yi_values, rcond=None)[0]

x_points = np.linspace(0, 1, 100)
y_linear = m_linear * x_points + c_linear
y_quadratic = a_quadratic * x_points**2 + b_quadratic * x_points + c_quadratic

plt.scatter(xi_values, yi_values, label='Точки')
plt.plot(x_points, y_linear, label=f'Пряма: y = {m_linear:.4f}x + {c_linear:.4f}', color='red')
plt.plot(x_points, y_quadratic, label=f'Парабола: y = {a_quadratic:.4f}x^2 + {b_quadratic:.4f}x + {c_quadratic:.4f}', color='green')

plt.title('Найменші квадрати: пряма та парабола')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

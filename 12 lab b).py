import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + np.cos(y / np.sqrt(2))

def euler_cromer_method(f, x0, y0, h, n):
    x_values = [x0 + i * h for i in range(n+1)]
    y_values = [y0]

    for i in range(n):
        y_next = y_values[-1] + h * f(x_values[i] + h/2, y_values[-1] + (h/2) * f(x_values[i], y_values[-1]))
        y_values.append(y_next)

    return x_values, y_values

x0 = 0.8
y0 = 1.4
h = 0.1
n = int((1.8 - 0.8) / h)

x_values, y_values = euler_cromer_method(f, x0, y0, h, n)

plt.plot(x_values, y_values, label='Розв\'язок методом Ейлера-Коші')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ламана Ейлера для розв\'язку')
plt.scatter(x_values, y_values, color='red')  
plt.plot(x_values, y_values, linestyle='dashed', color='gray')  
plt.legend()
plt.grid(True)
plt.show()

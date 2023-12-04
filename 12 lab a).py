import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + np.sin(y/3.14)

def euler_method(x0, y0, h, x_target):
    x_values = [x0]
    y_values = [y0]

    while x_values[-1] < x_target:
        x_n = x_values[-1]
        y_n = y_values[-1]
        y_n1 = y_n + h * f(x_n, y_n)

        x_values.append(x_n + h)
        y_values.append(y_n1)

    return x_values, y_values

x0 = 1.7
y0 = 5.3
h = 0.1
x_target = 2.7

x_values, y_values = euler_method(x0, y0, h, x_target)

plt.plot(x_values, y_values, label='Euler Method')
plt.title('Euler Method for y\' = x + sin(y/3.14)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

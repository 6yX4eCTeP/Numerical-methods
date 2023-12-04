import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Система диференціальних рівнянь
def system1(y, x):
    dydx = x + np.sin(y/3.14)
    return dydx

# Система диференціальних рівнянь
def system2(y, x):
    dydx = x + np.cos(y/np.sqrt(2))
    return dydx

# Вхідні дані
x_span = np.linspace(0.8, 1.8, 100)
y0 = 1.4

# Розв'язок для системи 1
y1 = odeint(system1, y0, x_span)
# Розв'язок для системи 2
y2 = odeint(system2, y0, x_span)

# Побудова графіків
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(x_span, y1, label='y\'=x+sin(y/3.14)')
plt.title('Розв\'язок для y\'=x+sin(y/3.14)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x_span, y2, label='y\'=x+cos(y/sqrt(2))')
plt.title('Розв\'язок для y\'=x+cos(y/sqrt(2))')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

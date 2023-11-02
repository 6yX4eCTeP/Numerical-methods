import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


x = np.array([0.9, 1.2, 1.6, 2.1, 2.8])
y = np.array([3.47, 4.53, 2.86, 1.64, 2.25])


cs = CubicSpline(x, y, bc_type='natural')


x_new = np.linspace(x[0], x[-1], 100)
y_new = cs(x_new)

print("Коефіцієнти сплайну для кожного полінома:")
for i in range(len(cs.c[0])):
    print(f"Відрізок {i+1}: a={cs.c[3][i]}, b={cs.c[2][i]}, c={cs.c[1][i]}, d={cs.c[0][i]}")

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Вузлові точки')
plt.plot(x_new, y_new, label='Кубічний сплайн')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Кубічний сплайн апроксимації')
plt.legend()
plt.grid(True)
plt.show()
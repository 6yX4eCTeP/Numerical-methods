from scipy import integrate
import numpy as np

# Вираз для f(x)
def f(x):
    return 1 / np.sqrt(x + 4)

# Межі інтегрування
a = 0.8
b = 1.8

# Визначений інтеграл за допомогою вбудованої функції quad
result_quad, _ = integrate.quad(f, a, b)

# Кількість підінтервалів
n = 10

# Ширина кожного підінтервалу
dx = (b - a) / n

# Метод лівих прямокутників
left_rectangular = dx * sum(f(a + i * dx) for i in range(n))

# Метод правих прямокутників
right_rectangular = dx * sum(f(a + (i + 1) * dx) for i in range(n))

# Метод середніх прямокутників
midpoint_rectangular = dx * sum(f(a + (i + 0.5) * dx) for i in range(n))

# Виведення результатів
print("Метод лівих прямокутників:", left_rectangular)
print("Метод правих прямокутників:", right_rectangular)
print("Метод середніх прямокутників:", midpoint_rectangular)
print("Вбудований метод (quad):", result_quad)

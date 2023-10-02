def f(x):
    return 3*x**4 - 10*x**3 + x**2 - 5 - 3

def f_prime(x):
    return 12*x**3 - 30*x**2 + 2*x

def bisection_method(a, b, tolerance=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Початкові значення a та b мають однаковий знак, оберіть інші значення")

    iteration = 0
    while (b - a) / 2 > tolerance and iteration < max_iterations:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iteration += 1

    return (a + b) / 2

def combined_method(initial_guess, tolerance=1e-6, max_iterations=100):
    x = initial_guess

    iteration = 0
    while abs(f(x)) > tolerance and iteration < max_iterations:
        x = x - f(x) / f_prime(x)
        iteration += 1

    if abs(f(x)) <= tolerance:
        return x
    else:
        raise ValueError("Комбінований метод не зійшовся")

# Початкове наближення для кореня
initial_guess = 1.0

# Виклик комбінованого методу
result = combined_method(initial_guess)
print(f"Результат комбінованого методу: x = {result}")
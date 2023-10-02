def f(x):
    return 3*x**4 - 10*x**3 + x**2 - 5 - 3

def f_prime(x):
    return 12*x**3 - 30*x**2 + 2*x

def bisection_method(a, b, t=1e-6, max=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Початкові значення a та b мають однаковий знак, оберіть інші значення")

    iteration = 0
    while (b - a) / 2 > t and iteration < max:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iteration += 1

    return (a + b) / 2

def combined_method(initial_guess, t=1e-6, max=100):
    x = initial_guess

    iteration = 0
    while abs(f(x)) > t and iteration < max:
        x = x - f(x) / f_prime(x)
        iteration += 1

    if abs(f(x)) <= t:
        return x
    else:
        raise ValueError("Комбінований метод не зійшовся")

initial_guess = 1.0

result = combined_method(initial_guess)
print(f"Результат комбінованого методу: x = {result}")
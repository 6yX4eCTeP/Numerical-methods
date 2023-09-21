import math

def f(x):
    return 9 * x**4 + 12 * x**3 - x**2 - 5 * x - 3

def bisection_method(a, b, eps):
    if f(a) * f(b) > 0:
        return None
    
    while abs(a - b) > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2

def chord_method(a, b, eps):
    if f(a) * f(b) > 0:
        return None
    
    x0 = a
    x1 = b
    
    while abs(x1 - x0) > eps:
        x2 = x1 - (x1 - x0) * f(x1) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
    
    return x1

def find_segments(): 
    search_range = list(range(-10, 11))
    
    a = None
    previous_x = None
    current_x  = None
    segments = []

    for x in search_range:
        x = round(x, 4)
        current_x = f(x)
        if previous_x is not None and previous_x * current_x < 0:
            segments.append((a, x))
        a = x
        previous_x = current_x
    return segments

segments = find_segments()
eps = 0.0001

for a, b in segments:
    root_bisection = bisection_method(a, b, eps)
    root_chord = chord_method(a, b, eps)
    
    if root_bisection is not None:
        print(f"Метод половинного ділення: Корінь на відрізку [{a}, {b}]: {root_bisection:.4f}")
    
    if root_chord is not None:
        print(f"Метод хорд: Корінь на відрізку [{a}, {b}]: {root_chord:.4f}")
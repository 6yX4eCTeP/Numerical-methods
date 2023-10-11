import math

def f_x(x, y):
    return math.sin(y + 0.5) - 1

def f_y(x, y):
    return -math.cos(x - 2)

# Початкові наближення
x = 0
y = 0
tolerance = 0.001

iteration = 0
while True:
    x_new = f_x(x, y)
    y_new = f_y(x, y)
    
    print(f'Ітерація {iteration + 1}:')
    print(f'x ≈ {x_new:.3f}')
    print(f'y ≈ {y_new:.3f}')
    
    if abs(x_new - x) < tolerance and abs(y_new - y) < tolerance:
        break
    
    x = x_new
    y = y_new
    iteration += 1

print(f'Після {iteration} ітерацій:')
print(f'x ≈ {x_new:.3f}')
print(f'y ≈ {y_new:.3f}')
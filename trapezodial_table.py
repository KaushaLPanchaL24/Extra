# Trapezoidal Rule for integral of 1/(1+x^2)

import math

# Given values
a = 0          # lower limit
b = 6          # upper limit
n = 6          # number of intervals

h = (b - a) / n   # step size

# Function definition
def f(x):
    return 1 / (1 + x**2)

# Table header
print("i\t x\t\t f(x)")
print("-" * 30)

# Trapezoidal calculation
sum_fx = 0

for i in range(n + 1):
    x = a + i * h
    fx = f(x)
    print(f"{i}\t {x:.2f}\t {fx:.6f}")
    
    if i == 0 or i == n:
        sum_fx += fx
    else:
        sum_fx += 2 * fx

# Final result
result = (h / 2) * sum_fx

print("\nStep size h =", h)
print("Approximate value of integral =", result)

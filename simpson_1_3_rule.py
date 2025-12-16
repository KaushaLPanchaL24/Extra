# Simpson's One-Third Rule for integral of 1/(1 + x^2)

# Given values
a = 0      # lower limit
b = 6      # upper limit
n = 6      # number of sub-intervals (must be even)

h = (b - a) / n   # step size

# Function definition
def f(x):
    return 1 / (1 + x**2)

# Table header
print("i\t x\t\t f(x)")
print("-" * 30)

sum_odd = 0
sum_even = 0

# Generating table and sums
for i in range(n + 1):
    x = a + i * h
    fx = f(x)
    print(f"{i}\t {x:.2f}\t {fx:.6f}")
    
    if i != 0 and i != n:
        if i % 2 == 0:
            sum_even += fx
        else:
            sum_odd += fx

# Simpson's formula
result = (h / 3) * (f(a) + f(b) + 4 * sum_odd + 2 * sum_even)

print("\nStep size h =", h)
print("Approximate value of integral =", result)

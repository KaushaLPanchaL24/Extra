import random

def linear_regression(x, y, lr=0.01, epochs=1000):

    n = len(x)

    # Initialize m and c with random values
    m = random.random()
    c = random.random()

    # Gradient Descent
    for _ in range(epochs):
        y_pred = [m * xi + c for xi in x]

        # Compute gradients
        dm = (-2 / n) * sum(x[i] * (y[i] - y_pred[i]) for i in range(n))
        dc = (-2 / n) * sum(y[i] - y_pred[i] for i in range(n))

        # Update m and c
        m = m - lr * dm
        c = c - lr * dc

    return m, c

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

m, c = linear_regression(x, y)

print("Slope (m):", m)
print("Intercept (c):", c)

#Slope (m): 0.6176503948354776
#Intercept (c): 2.136276474203972

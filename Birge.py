def birge_vieta():
    import math

    # Input degree of the polynomial
    n = int(input("Enter the highest exponent (degree) of the polynomial: "))

    # Input coefficients
    a = [0] * (n + 1)
    for j in range(n, -1, -1):
        a[j] = float(input(f"Enter the coefficient of x^{j}: "))

    # Initial guess
    x0 = float(input("Enter initial guess: "))

    err = 0.1
    error = 1
    iteration = 0

    while error > err:
        b = [0] * (n + 1)
        c = [0] * (n + 1)

        print("\n\n i\t ai\t\t bi\t\t ci")
        for j in range(n, -1, -1):
            if j == n:
                b[j] = a[j]
                c[j] = a[j]
            else:
                b[j] = a[j] + x0 * b[j + 1]
                c[j] = b[j] + x0 * c[j + 1]
            print(f"{j}\t {a[j]:.6f}\t {b[j]:.6f}\t {c[j]:.6f}")

        # Prevent division by zero
        if c[1] == 0:
            print("Derivative is zero. Method fails.")
            return

        x1 = x0 - b[0] / c[1]
        print(f"\nIteration {iteration + 1}: x1 = {x1:.8f}")
        error = abs(x1 - x0)
        x0 = x1
        iteration += 1

    print(f"\nDesired root is: {x1:.6f}")


# Run the method
birge_vieta()

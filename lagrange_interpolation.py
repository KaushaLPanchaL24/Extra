def lagrange_interpolation(x, points):
    total = 0
    n = len(points)
    for i in range(n):
        xi, yi = points[i]
        Li = 1
        for j in range(n):
            if j != i:
                xj, _ = points[j]
                Li *= (x - xj) / (xi - xj)
        total += yi * Li
    return total

# Example usage with any number of points:
# 2 points
points_2 = [(0.1, 0.09983), (0.2, 0.19867)]
print(f"f(0.15) ≈ {lagrange_interpolation(0.15, points_2):.5f}")

# 3 points
points_3 = [(0, 1), (1, 3), (3, 55)]
print(f"f(2) ≈ {lagrange_interpolation(2, points_3):.5f}")

# 4 points
points_4 = [(-1, -2), (1, 0), (4, 63), (7, 342)]
print(f"f(5) ≈ {lagrange_interpolation(5, points_4):.5f}")

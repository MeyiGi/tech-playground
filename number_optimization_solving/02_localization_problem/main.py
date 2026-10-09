
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Надо три метода как в прошлом и как монта карла и метод градиента 

# Настройки
points = np.array([[0, 0], [10, 0], [5, 8]])
weights = [3, 3, 1]
tariff = 10
levels = 50
method = "Nelder-Mead"

def cost(p):
    return tariff * np.dot(weights, np.linalg.norm(points - p, axis=1))

result = minimize(cost, [5, 3], method=method)
best = min([result.x, *points], key=cost)

print(f"Завод: {best.round(2)}, затраты: {cost(best):.2f} сом")

x, y = np.meshgrid(np.linspace(-2, 12, 150), np.linspace(-2, 10, 150))
z = sum(tariff * w * np.hypot(x-a, y-b) for (a, b), w in zip(points, weights))

plt.contourf(x, y, z, levels=levels, cmap="viridis")
plt.colorbar(label="Затраты (сом)")
plt.plot(*np.vstack([points, points[0]]).T, "w--")

for name, (a, b), w in zip("ABC", points, weights):
    plt.scatter(a, b, color="white")
    plt.text(a+.2, b+.2, f"{name}: {w} т", color="white")

plt.scatter(*best, color="red", marker="*", s=250, label="Завод")
plt.axis("equal")
plt.legend()
plt.show()

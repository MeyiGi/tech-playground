import math
import matplotlib.pyplot as plt

points = [(0, 0), (10, 0), (5, 8)]
weights = [3, 3.5, 1]
tariff = 10

learning_rate = 0.01
iterations = 1000


def derivative(f, x, h=1e-5) -> callable:
    return (f(x + h) - f(x - h)) / (2 * h)

def loss(x, y):
    return tariff * sum(
        w * math.hypot(x - a, y - b)
        for (a, b), w in zip(points, weights)
    )

x, y = 5.0, 3.0 # random value but center is best option

for i in range(iterations):
    dx = derivative(lambda v: loss(v, y), x)
    dy = derivative(lambda v: loss(x, v), y)
    
    step = learning_rate / math.sqrt(i + 1)

    x -= step * dx
    y -= step * dy

print(f"Завод: ({x:.4f}, {y:.4f})")
print(f"Минимальные затраты: {loss(x, y):.2f} сом")



triangle = points + [points[0]]

plt.plot(*zip(*triangle), "b--", label="Треугольник")
plt.scatter(*zip(*points), color="blue")
plt.scatter(x, y, color="red", marker="*", s=250, label="Завод")

for name, (a, b) in zip("ABC", points):
    plt.annotate(name, (a, b), xytext=(5, 5),
                 textcoords="offset points")

plt.axis("equal")
plt.grid()
plt.legend()
plt.show()  
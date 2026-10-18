"""Графический метод: линии -> вершины -> самая прибыльная точка
Рисуем две переменные: X = Dash в Ош, Y = Avro в Ош.
Рейсы в другие города пока фиксированы (см. ниже).
"""
from itertools import combinations
from math import atan2, floor
import matplotlib.pyplot as plt

# ДАНО: 2 Dash, 1 Avro; билет $45, загрузка 80%, топливо $1.1/кг.
# Маршруты: Ош, Джалал-Абад, Баткен. Спрос: 45000 / 9000 / 6000.
# Полет: 200 часов на борт; рабочее окно: 14 ч * 30 дней.
# Dash 8, Avro
seats = [78, 96]
fuel = [1000, 2400]      # кг/час
repair = [600, 1100]     # $/час
wear = [320, 200]        # амортизация $/час
airport = [400, 700]     # $ за оборотный рейс
ground = [0.5, 0.75]     # наземное обслуживание, часов
flight = [[.75, .7, 1], [.6, .55, .8]]

# Чтобы построить 2D-график, закрепляем остальные четыре переменные
dash_jalal, dash_batken = 10, 0
avro_jalal, avro_batken = 109, 0

# Полет + земля, только полет, спрос на Ош: a*x + b*y <= c.
lines = [
    (1.25, 0, 840 - 1.2*dash_jalal - 1.5*dash_batken, 'Dash: полет + земля'),
    (.75, 0, 400 - .7*dash_jalal - dash_batken, 'Dash: полет'),
    (0, 1.35, 420 - 1.3*avro_jalal - 1.55*avro_batken, 'Avro: полет + земля'),
    (0, .6, 200 - .55*avro_jalal - .8*avro_batken, 'Avro: полет'),
    (62.4, 76.8, 45000, 'Спрос на Ош'),
]
# x>=0 и y>=0 — тоже границы.
borders = lines + [(-1, 0, 0, ''), (0, -1, 0, '')]

# Находим пересечения ПРЯМЫХ (не перебираем все рейсы).
points = []
for (a, b, c, _), (d, e, f, _) in combinations(borders, 2):
    det = a*e - b*d
    if abs(det) < 1e-9:
        continue
    x, y = (c*e-b*f)/det, (a*f-c*d)/det
    if all(A*x+B*y <= C+1e-6 for A, B, C, _ in borders):
        if not any(abs(x-u)+abs(y-v) < 1e-6 for u, v in points):
            points.append((x, y))

# Считаем реальную прибыль: билеты минус топливо, ТОиР, износ и сборы.
profit = [[round(.8*seats[i]*45 - (flight[i][j] *
           (fuel[i]*1.1 + repair[i] + wear[i]) + airport[i]/2))
           for j in range(3)] for i in range(2)]
base = (dash_jalal*profit[0][1] + dash_batken*profit[0][2] +
        avro_jalal*profit[1][1] + avro_batken*profit[1][2])
cost = lambda p: base + profit[0][0]*p[0] + profit[1][0]*p[1]
best = max(points, key=cost)

# Сортировка углов для закраски области.
cx = sum(p[0] for p in points) / len(points)
cy = sum(p[1] for p in points) / len(points)
points.sort(key=lambda p: atan2(p[1]-cy, p[0]-cx))

# Рисуем ограничения ПО ОДНОМУ.
plt.ion()
fig, ax = plt.subplots(figsize=(10, 6))
ax.set(xlim=(0, 740), ylim=(0, 350), xlabel='X: Dash -> Ош (рейсы)',
       ylabel='Y: Avro -> Ош (рейсы)',
       title='Графический метод оптимизации авиарейсов')
ax.grid(alpha=.2)
colors = ['orange', 'red', 'teal', 'royalblue', 'purple']
for (a, b, c, name), color in zip(lines, colors):
    if b == 0:
        ax.axvline(c/a, color=color, lw=2, label=name)
    elif a == 0:
        ax.axhline(c/b, color=color, lw=2, label=name)
    else:
        ax.plot([0, 740], [c/b, (c-a*740)/b], color=color, lw=2, label=name)
    ax.legend(loc='upper right', fontsize=8)
    plt.pause(1.2)  # следующая линия появляется через 1.2 секунды

# Показываем допустимую область и выбираем лучшую ВЕРШИНУ.
ax.fill(*zip(*points), color='green', alpha=.2)
for x, y in points:
    ax.plot(x, y, 'ko', ms=5)
ax.plot(*best, 'go', ms=11)
ax.annotate(f'Лучшая точка ({best[0]:.1f}, {best[1]:.1f})',
            best, xytext=(-210, -30), textcoords='offset points',
            arrowprops={'arrowstyle': '->'}, color='green')

whole = (floor(best[0]+1e-8), floor(best[1]+1e-8))
print('Лучшая непрерывная вершина:', best)
print('Целый допустимый план для Оша:', whole)
print('Все рейсы:', [whole[0], dash_jalal, dash_batken,
                     whole[1], avro_jalal, avro_batken])
print('Прибыль:', round(cost(whole)), '$')
plt.ioff()
plt.show()

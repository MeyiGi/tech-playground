"""Анализ рисков и учебная оптимизация перевозки перебором целых тонн.

Запуск: python3 main.py. Внешние библиотеки не требуются.
"""

TOTAL_TONS = 100
RAIL_LIMIT = 60
BARGE_LIMIT = 50

TRANSPORTS = [
    {
        "name": "Железная дорога",
        "rate": 200,
        "days": 5,
        "risk_percent": 20,
        "extra_rate": 0,
        "fine": 20_000,
        "emergency_days": 7,
    },
    {
        "name": "Автофуры",
        "rate": 250,
        "days": 3,
        "risk_percent": 10,
        "extra_rate": 50,
        "fine": 0,
        "emergency_days": 4,
    },
    {
        "name": "Баржа",
        "rate": 150,
        "days": 6,
        "risk_percent": 30,
        "extra_rate": 150,
        "fine": 20_000,
        "emergency_days": 8,
    },
]


def calculate_base_cost(transport, tons):
    return transport["rate"] * tons


def calculate_emergency_cost(transport, tons):
    if tons == 0:
        return 0
    return calculate_base_cost(transport, tons) + transport["extra_rate"] * tons + transport["fine"]


def calculate_expected_cost(transport, tons):
    base_cost = calculate_base_cost(transport, tons)
    emergency_cost = calculate_emergency_cost(transport, tons)
    probability = transport["risk_percent"] / 100
    return round((1 - probability) * base_cost + probability * emergency_cost, 2)


def find_optimal_distribution(expected_rates):
    """Вернуть объёмы (ж/д, авто, баржа), стоимость и средний обычный срок.

    expected_rates — ожидаемые затраты на тонну в том же порядке.
    В линейной модели они постоянны и не зависят от размера отправки.
    """
    best_distribution = None
    best_cost = float("inf")
    best_average_days = float("inf")

    for rail_tons in range(RAIL_LIMIT + 1):
        for barge_tons in range(BARGE_LIMIT + 1):
            truck_tons = TOTAL_TONS - rail_tons - barge_tons
            if truck_tons < 0:
                continue

            distribution = (rail_tons, truck_tons, barge_tons)
            cost = round(sum(tons * rate for tons, rate in zip(distribution, expected_rates)), 2)
            # При равной стоимости предпочитаем меньший средний срок одной тонны.
            average_days = sum(
                tons * transport["days"]
                for tons, transport in zip(distribution, TRANSPORTS)
            ) / TOTAL_TONS

            if cost < best_cost or (cost == best_cost and average_days < best_average_days):
                best_distribution = distribution
                best_cost = cost
                best_average_days = average_days

    return best_distribution, best_cost, best_average_days


def format_money(amount):
    return f"{amount:,.0f}".replace(",", " ")


def print_results():
    print("Этап 1. Исходные данные")
    print(f"Груз: {TOTAL_TONS} т медного концентрата.\n")
    print(f"{'Транспорт':<18} {'Тариф, руб/т':>12} {'Срок, дни':>10} {'Риск ЧП':>9} {'При ЧП, дни':>12}")
    print("-" * 65)
    for transport in TRANSPORTS:
        print(
            f"{transport['name']:<18} {transport['rate']:>12} {transport['days']:>10}"
            f" {transport['risk_percent']:>8}% {transport['emergency_days']:>12}"
        )
    print("При ЧП: ж/д — штраф 20 000 руб.; авто — доплата 50 руб/т;")
    print("баржа — доплата 150 руб/т и штраф 20 000 руб.")

    print("\nЭтап 2. Анализ рисков: один транспорт для всей партии")
    print("Математическое ожидание = (1 − p) × базовая стоимость + p × стоимость при ЧП.\n")
    print(f"{'Транспорт':<18} {'База, руб.':>12} {'При ЧП, руб.':>13} {'Риск ЧП':>9} {'Ожидание, руб.':>15}")
    print("-" * 71)
    expected_costs = []
    for transport in TRANSPORTS:
        base_cost = calculate_base_cost(transport, TOTAL_TONS)
        emergency_cost = calculate_emergency_cost(transport, TOTAL_TONS)
        expected_cost = calculate_expected_cost(transport, TOTAL_TONS)
        expected_costs.append(expected_cost)
        print(
            f"{transport['name']:<18} {format_money(base_cost):>12}"
            f" {format_money(emergency_cost):>13} {transport['risk_percent']:>8}%"
            f" {format_money(expected_cost):>15}"
        )

    best_transport_index = min(range(len(TRANSPORTS)), key=lambda index: expected_costs[index])
    print(
        f"Выбор для всей партии: {TRANSPORTS[best_transport_index]['name']},"
        f" ожидаемые затраты {format_money(expected_costs[best_transport_index])} руб."
    )
    print("В этой исходной задаче ограничения 60 и 50 т не применяются.")

    # Делим ожидание для всей партии на её объём, а не считаем штраф за одну тонну.
    expected_rates = [cost / TOTAL_TONS for cost in expected_costs]
    print("\nЭтап 3. Учебная линейная модель распределения груза")
    print("x1 — ж/д, x2 — автофуры, x3 — баржа; объёмы в тоннах.")
    coefficients = [f"{rate:g}x{index}" for index, rate in enumerate(expected_rates, start=1)]
    print(f"Z = {' + '.join(coefficients)} → min (руб.)")
    print(f"x1 + x2 + x3 = {TOTAL_TONS}")
    print(f"x1 ≤ {RAIL_LIMIT}, x3 ≤ {BARGE_LIMIT}; x1, x2, x3 ≥ 0.")
    print("Пределы 60 и 50 т — дополнительные учебные предположения.")
    print("Ожидаемые затраты приняты пропорциональными объёму перевозки.")
    print("В исходном условии штрафы фиксированы за партию. Поэтому такое")
    print("распределение — отдельная модель: прямой учёт фиксированных штрафов")
    print("при разделении партии потребовал бы другой целевой функции.")

    distribution, minimum_cost, average_days = find_optimal_distribution(expected_rates)
    print("\nЭтап 4. Оптимизация перебором целых тонн")
    print("Перебираем объёмы ж/д и баржи, остаток отправляем автофурами.\n")
    print(f"{'Транспорт':<18} {'Объём, т':>10} {'Ожидаемые затраты, руб.':>24}")
    print("-" * 54)
    for transport, tons, rate in zip(TRANSPORTS, distribution, expected_rates):
        print(f"{transport['name']:<18} {tons:>10} {format_money(tons * rate):>24}")
    print(f"Средний обычный срок одной тонны: {average_days:.2f} дня.")
    print("Критерий при равной стоимости: сумма (тонны × обычный срок) / 100.")
    print("Это не срок прибытия всей партии; задержки при ЧП здесь не учитываются.")

    print("\nЭтап 5. Итог")
    print("=" * 54)
    print(f"Минимальные ожидаемые затраты: {format_money(minimum_cost)} руб.")
    print("=" * 54)
    print("Ж/д дешевле на тонну, поэтому используем её лимит полностью.")
    print("Оставшийся груз можно делить между авто и баржей без изменения")
    print("стоимости. Выбираем автофуры: их обычный срок доставки меньше.")
    print("Перебраны все допустимые целочисленные варианты, поэтому найден")
    print("глобальный минимум дискретной модели. Для непрерывной модели")
    print("здесь также верно: Z = 255 × 100 − 15x1; минимум при x1 = 60.")
    print("Перебор целых тонн — учебная дискретная модель, а не универсальный")
    print("метод решения непрерывного линейного программирования.")


if __name__ == "__main__":
    print_results()

# Градиентный спуск 3D — Flask App

## Структура проекта

```
gradient3d/
├── app.py                  ← Flask сервер + вся математика
├── requirements.txt
├── templates/
│   └── index.html          ← HTML разметка
└── static/
    ├── css/
    │   └── style.css       ← Стили
    └── js/
        └── main.js         ← Логика визуализации (Plotly 3D)
```

## Как запустить

```bash
# 1. Установить зависимости
pip install -r requirements.txt

# 2. Запустить Flask
python app.py

# 3. Открыть в браузере
http://localhost:5000
```

## Функционал

- **5 функций**: Парабола, Himmelblau, Rosenbrock, Rastrigin, Ackley
- **5 алгоритмов**: Vanilla GD, Momentum, AdaGrad, Adam, RMSProp
- **3D визуализация**: интерактивная поверхность через Plotly.js
- **Формула профессора**: центральная разность ∂f/∂x ≈ [f(x+Δx) − f(x−Δx)] / 2Δx
- **Анимация**: точка движется по поверхности шаг за шагом
- **Кликните** по 3D поверхности — выбрать стартовую точку

## API эндпоинты

| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/` | Главная страница |
| POST | `/api/surface` | Сетка значений для 3D поверхности |
| POST | `/api/run` | Запуск градиентного спуска, возвращает путь |

### Пример запроса к /api/run
```json
{
  "fn": "sphere",
  "algo": "adam",
  "start_x": 2.5,
  "start_y": 2.0,
  "lr": 0.05,
  "max_iter": 300,
  "dx": 0.0001,
  "beta": 0.9
}
```

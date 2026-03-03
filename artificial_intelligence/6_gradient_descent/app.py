from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# ─────────────────────────────────────────────
#  Функции для оптимизации
# ─────────────────────────────────────────────
FUNCTIONS = {
    "sphere": {
        "label": "Парабола x² + y²",
        "fn": lambda x, y: x**2 + y**2,
        "range": 3.0,
        "minima": [[0, 0]],
    },
    "himmelblau": {
        "label": "Himmelblau",
        "fn": lambda x, y: (x**2 + y - 11)**2 + (x + y**2 - 7)**2,
        "range": 5.0,
        "minima": [[3, 2], [-2.805, 3.131], [-3.779, -3.283], [3.584, -1.848]],
    },
    "rosenbrock": {
        "label": "Rosenbrock",
        "fn": lambda x, y: (1 - x)**2 + 100 * (y - x**2)**2,
        "range": 2.2,
        "minima": [[1, 1]],
    },
    "rastrigin": {
        "label": "Rastrigin",
        "fn": lambda x, y: 20 + x**2 - 10*math.cos(2*math.pi*x) + y**2 - 10*math.cos(2*math.pi*y),
        "range": 4.0,
        "minima": [[0, 0]],
    },
    "ackley": {
        "label": "Ackley",
        "fn": lambda x, y: -20*math.exp(-0.2*math.sqrt(0.5*(x**2+y**2)))
                            - math.exp(0.5*(math.cos(2*math.pi*x)+math.cos(2*math.pi*y)))
                            + math.e + 20,
        "range": 4.0,
        "minima": [[0, 0]],
    },
}


def safe_eval(fn, x, y):
    try:
        v = fn(x, y)
        return min(v, 1e7) if math.isfinite(v) else 1e7
    except Exception:
        return 1e7


def central_diff_grad(fn, x, y, dx):
    """
    Формула профессора (центральная разность):
    ∂f/∂x ≈ [f(x+Δx) − f(x−Δx)] / (2·Δx)
    """
    gx = (safe_eval(fn, x + dx, y) - safe_eval(fn, x - dx, y)) / (2 * dx)
    gy = (safe_eval(fn, x, y + dx) - safe_eval(fn, x, y - dx)) / (2 * dx)
    return gx, gy


# ─────────────────────────────────────────────
#  Алгоритмы
# ─────────────────────────────────────────────

def run_optimizer(fn_key, algo, start_x, start_y,
                  lr, max_iter, dx, beta=0.9):
    fn_info = FUNCTIONS[fn_key]
    fn = fn_info["fn"]
    R = fn_info["range"] * 1.5

    x, y = start_x, start_y
    path = [{"x": x, "y": y, "f": safe_eval(fn, x, y), "iter": 0}]

    # Algo state
    vx = vy = 0.0
    Gx = Gy = 0.0
    mx = my = vvx = vvy = 0.0
    rmsX = rmsY = 0.0
    t = 0

    for i in range(1, max_iter + 1):
        gx, gy = central_diff_grad(fn, x, y, dx)
        glen = math.sqrt(gx**2 + gy**2)

        if algo == "gd":
            x -= lr * gx
            y -= lr * gy

        elif algo == "momentum":
            vx = beta * vx - lr * gx
            vy = beta * vy - lr * gy
            x += vx
            y += vy

        elif algo == "adagrad":
            Gx += gx**2; Gy += gy**2
            x -= lr / math.sqrt(Gx + 1e-8) * gx
            y -= lr / math.sqrt(Gy + 1e-8) * gy

        elif algo == "adam":
            b1, b2, eps = 0.9, 0.999, 1e-8
            t += 1
            mx = b1*mx + (1-b1)*gx;  my = b1*my + (1-b1)*gy
            vvx = b2*vvx + (1-b2)*gx**2;  vvy = b2*vvy + (1-b2)*gy**2
            mxh = mx / (1 - b1**t);  myh = my / (1 - b1**t)
            vxh = vvx / (1 - b2**t); vyh = vvy / (1 - b2**t)
            x -= lr * mxh / (math.sqrt(vxh) + eps)
            y -= lr * myh / (math.sqrt(vyh) + eps)

        elif algo == "rmsprop":
            rho, eps = 0.9, 1e-8
            rmsX = rho*rmsX + (1-rho)*gx**2
            rmsY = rho*rmsY + (1-rho)*gy**2
            x -= lr / math.sqrt(rmsX + eps) * gx
            y -= lr / math.sqrt(rmsY + eps) * gy

        # Clamp
        x = max(-R, min(R, x))
        y = max(-R, min(R, y))

        fv = safe_eval(fn, x, y)
        path.append({"x": x, "y": y, "f": fv, "iter": i,
                     "grad": glen})

        if glen < 1e-7:
            break

    return path


# ─────────────────────────────────────────────
#  Routes
# ─────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html", functions=FUNCTIONS)


@app.route("/api/surface", methods=["POST"])
def api_surface():
    """Возвращает сетку значений для 3D-поверхности."""
    data = request.get_json()
    fn_key = data.get("fn", "sphere")
    steps = int(data.get("steps", 60))

    fn_info = FUNCTIONS.get(fn_key, FUNCTIONS["sphere"])
    fn = fn_info["fn"]
    R = fn_info["range"]

    xs = [round(-R + 2*R*i/steps, 5) for i in range(steps + 1)]
    ys = [round(-R + 2*R*j/steps, 5) for j in range(steps + 1)]
    zs = []
    for j in range(steps + 1):
        row = []
        for i in range(steps + 1):
            row.append(round(safe_eval(fn, xs[i], ys[j]), 4))
        zs.append(row)

    return jsonify({
        "xs": xs,
        "ys": ys,
        "zs": zs,
        "range": R,
        "minima": fn_info["minima"],
        "label": fn_info["label"],
    })


@app.route("/api/run", methods=["POST"])
def api_run():
    """Запускает градиентный спуск и возвращает путь."""
    data = request.get_json()
    fn_key  = data.get("fn", "sphere")
    algo    = data.get("algo", "gd")
    start_x = float(data.get("start_x", 2.5))
    start_y = float(data.get("start_y", 2.0))
    lr      = float(data.get("lr", 0.05))
    max_iter= int(data.get("max_iter", 200))
    dx      = float(data.get("dx", 1e-4))
    beta    = float(data.get("beta", 0.9))

    if fn_key not in FUNCTIONS:
        return jsonify({"error": "unknown function"}), 400

    path = run_optimizer(fn_key, algo, start_x, start_y,
                         lr, max_iter, dx, beta)

    return jsonify({"path": path, "converged": len(path) <= max_iter})


if __name__ == "__main__":
    app.run(debug=True, port=5000)

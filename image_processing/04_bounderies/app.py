"""Запуск: python app.py. GUI и рисунки обновляются только главным потоком."""

import queue
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle

from processing import (LAPLACIAN, SOBEL_X, SOBEL_Y, canny, derivatives,
                        load_image, normalize, save_image)


class ConvolutionApp:
    def __init__(self, root):
        self.root = root
        root.title("Границы • Лаборатория свёртки")
        root.geometry("1180x850")
        root.minsize(900, 700)
        root.configure(bg="#eef2f8")
        style = ttk.Style(root)
        style.theme_use("clam")
        style.configure("TFrame", background="#eef2f8")
        style.configure("TLabel", background="#eef2f8", foreground="#172b4d")
        style.configure("TButton", padding=8)
        style.configure("Title.TLabel", font=("TkDefaultFont", 19, "bold"))
        self.rgb = self.gray = None
        self.results = {}
        self.busy = False
        self.playing = False
        self.events = queue.Queue()
        self.method = tk.StringVar(value="Sobel")
        self.low, self.high = tk.StringVar(value="50"), tk.StringVar(value="150")
        self.x, self.y = tk.StringVar(value="0"), tk.StringVar(value="0")
        self.kernel_name = tk.StringVar(value="Sobel Gx")
        self.status = tk.StringVar(value="Загрузите изображение, чтобы начать.")
        self.explanation = tk.StringVar(value="Выберите пиксель: кликните по изображению или задайте x и y.")
        main = ttk.Frame(root, padding=16)
        main.pack(fill="both", expand=True)
        ttk.Label(main, text="Лаборатория свёртки", style="Title.TLabel").pack(anchor="w")
        ttk.Label(main, text="Изображение → матрица H × W → производные → границы").pack(anchor="w", pady=(2, 12))
        bar = ttk.Frame(main)
        bar.pack(fill="x")
        self.load_button = ttk.Button(bar, text="Загрузить изображение", command=self.load)
        self.load_button.pack(side="left")
        select = ttk.Combobox(bar, textvariable=self.method, state="readonly",
                              values=["Sobel", "Canny", "Laplacian", "Сравнить все"], width=17)
        select.pack(side="left", padx=10)
        select.bind("<<ComboboxSelected>>", lambda _: self.draw_results())
        ttk.Button(bar, text="Сохранить результат", command=self.save).pack(side="right")
        thresholds = ttk.Frame(main)
        thresholds.pack(fill="x", pady=8)
        ttk.Label(thresholds, text="Canny: нижний порог").pack(side="left")
        ttk.Spinbox(thresholds, from_=0, to=255, textvariable=self.low, width=5).pack(side="left", padx=6)
        ttk.Label(thresholds, text="верхний порог").pack(side="left")
        ttk.Spinbox(thresholds, from_=0, to=255, textvariable=self.high, width=5).pack(side="left", padx=6)
        ttk.Button(thresholds, text="Применить пороги", command=self.apply_thresholds).pack(side="left", padx=8)
        # Резервируем место для состояния до растягиваемого блока графиков.
        footer = ttk.Frame(main)
        footer.pack(side="bottom", fill="x", pady=(10, 0))
        self.progress = ttk.Progressbar(footer, mode="indeterminate")
        self.progress.pack(fill="x", pady=(0, 4))
        ttk.Label(footer, textvariable=self.status, wraplength=850).pack(anchor="w")
        self.tabs = ttk.Notebook(main)
        self.tabs.pack(fill="both", expand=True)
        result_tab, lesson_tab = ttk.Frame(self.tabs), ttk.Frame(self.tabs)
        self.tabs.add(result_tab, text="  Изображения и сравнение  ")
        self.tabs.add(lesson_tab, text="  Как движется ядро 3×3  ")
        self.figure = Figure(figsize=(10, 5), dpi=100, layout="constrained", facecolor="#eef2f8")
        self.canvas = FigureCanvasTkAgg(self.figure, master=result_tab)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        controls = ttk.Frame(lesson_tab, padding=6)
        controls.pack(fill="x")
        for name, variable in [("x (столбец)", self.x), ("y (строка)", self.y)]:
            ttk.Label(controls, text=name).pack(side="left")
            ttk.Entry(controls, textvariable=variable, width=6).pack(side="left", padx=5)
        selector = ttk.Combobox(controls, textvariable=self.kernel_name, width=15,
                               values=["Sobel Gx", "Sobel Gy", "Laplacian"], state="readonly")
        selector.pack(side="left", padx=5)
        selector.bind("<<ComboboxSelected>>", lambda _: self.draw_lesson())
        ttk.Button(controls, text="Показать", command=self.draw_lesson).pack(side="left")
        ttk.Button(controls, text="Шаг →", command=self.step).pack(side="left", padx=5)
        self.play_button = ttk.Button(controls, text="▶ Движение", command=self.toggle_play)
        self.play_button.pack(side="left")
        self.lesson_figure = Figure(figsize=(10, 4), dpi=100, layout="constrained", facecolor="#eef2f8")
        self.lesson_canvas = FigureCanvasTkAgg(self.lesson_figure, master=lesson_tab)
        self.lesson_canvas.get_tk_widget().pack(fill="both", expand=True)
        self.lesson_canvas.mpl_connect("button_press_event", self.pick_pixel)
        ttk.Label(lesson_tab, textvariable=self.explanation, wraplength=1050,
                  justify="left", padding=8).pack(fill="x")
        root.after(100, self.poll)

    def thresholds(self):
        try:
            low, high = int(self.low.get()), int(self.high.get())
        except ValueError:
            raise ValueError("Введите целые значения порогов от 0 до 255.") from None
        if not 0 <= low < high <= 255:
            raise ValueError("Нужно 0 ≤ нижний порог < верхний порог ≤ 255.")
        return low, high

    def load(self):
        if self.busy:
            return
        path = filedialog.askopenfilename(title="Выберите изображение", filetypes=[
            ("Изображения", "*.png *.jpg *.jpeg *.bmp *.tif *.tiff"), ("Все файлы", "*")])
        if not path:
            return
        try:
            low, high = self.thresholds()
        except ValueError as error:
            messagebox.showerror("Пороги Canny", str(error))
            return
        self.stop_play()
        self.busy = True
        self.load_button.configure(state="disabled")
        self.progress.start(12)
        self.status.set("Вычисляю вручную все пиксели. Большие изображения могут потребовать времени…")

        def work():
            try:
                rgb, gray = load_image(path)
                results = derivatives(gray)
                results["canny"] = canny(gray, low, high)
                self.events.put((True, (rgb, gray, results, (low, high))))
            except Exception as error:
                self.events.put((False, str(error)))

        threading.Thread(target=work, daemon=True).start()

    def poll(self):
        try:
            success, payload = self.events.get_nowait()
        except queue.Empty:
            pass
        else:
            self.busy = False
            self.load_button.configure(state="normal")
            self.progress.stop()
            if success:
                self.rgb, self.gray, self.results, self.applied_thresholds = payload
                self.x.set(str(self.gray.shape[1] // 2))
                self.y.set(str(self.gray.shape[0] // 2))
                self.draw_results()
                self.draw_lesson()
                self.update_status()
            else:
                messagebox.showerror("Ошибка загрузки", payload)
                self.status.set("Не удалось загрузить изображение. Можно выбрать другой файл.")
        self.root.after(100, self.poll)

    def update_status(self):
        height, width = self.gray.shape
        low, high = self.applied_thresholds
        self.status.set(f"Матрица H × W: {height} × {width}, uint8. Полное разрешение. "
                        f"Canny: {low}/{high}. Sobel и Laplacian: ручная свёртка, края — повтор пикселя.")

    def apply_thresholds(self):
        if self.gray is None or self.busy:
            return
        try:
            low, high = self.thresholds()
            self.results["canny"] = canny(self.gray, low, high)
        except (ValueError, OverflowError) as error:
            messagebox.showerror("Пороги Canny", str(error))
            return
        self.applied_thresholds = (low, high)
        self.draw_results()
        self.update_status()

    def draw_results(self):
        if self.gray is None:
            return
        self.figure.clear()
        method = self.method.get()
        if method == "Sobel":
            axes = self.figure.subplots(2, 3).ravel()
            plots = [("Оригинал", self.rgb),
                     ("|G| → 0…255", self.results["sobel"]),
                     ("Gx: знак сохранён", self.results["gx"]),
                     ("Gy: знак сохранён", self.results["gy"]),
                     ("|Gx| → 0…255", normalize(np.abs(self.results["gx"]))),
                     ("|Gy| → 0…255", normalize(np.abs(self.results["gy"])))]
        elif method == "Сравнить все":
            axes = self.figure.subplots(2, 2).ravel()
            low, high = self.applied_thresholds
            plots = [("Оригинал", self.rgb), ("Sobel: |G|", self.results["sobel"]),
                     (f"Canny: пороги {low}/{high}", self.results["canny"]),
                     ("Laplacian: |отклик|", self.results["laplacian"])]
        else:
            axes = self.figure.subplots(1, 2).ravel()
            plots = [("Оригинал", self.rgb),
                     (method if method == "Canny" else "Laplacian: |отклик| → 0…255",
                      self.results[method.lower()])]
        for axis, (title, values) in zip(axes, plots):
            if title.startswith(("Gx:", "Gy:")):
                limit = max(1.0, float(np.abs(values).max()))
                artist = axis.imshow(values, cmap="RdBu_r", vmin=-limit, vmax=limit)
                self.figure.colorbar(artist, ax=axis, shrink=0.7)
            else:
                axis.imshow(values, cmap="gray", vmin=0, vmax=255)
            axis.set_title(title, fontsize=10)
            axis.set_axis_off()
        self.canvas.draw_idle()

    def coordinates(self):
        try:
            x, y = int(self.x.get()), int(self.y.get())
        except ValueError:
            raise ValueError("Введите целые координаты x и y.") from None
        height, width = self.gray.shape
        if not (0 <= x < width and 0 <= y < height):
            raise ValueError(f"Координаты: 0 ≤ x < {width}, 0 ≤ y < {height}.")
        return x, y

    def draw_lesson(self):
        if self.gray is None:
            return
        try:
            x, y = self.coordinates()
        except ValueError as error:
            self.stop_play()
            messagebox.showerror("Координаты", str(error))
            return
        kernel = {"Sobel Gx": SOBEL_X, "Sobel Gy": SOBEL_Y,
                  "Laplacian": LAPLACIAN}[self.kernel_name.get()]
        # Тот же padding и тот же переворот, что в основной реализации.
        patch = np.pad(self.gray, 1, mode="edge")[y:y + 3, x:x + 3].astype(float)
        weights = kernel[::-1, ::-1]
        products = patch * weights
        self.lesson_figure.clear()
        axes = self.lesson_figure.subplots(1, 4)
        self.image_axis = axes[0]
        axes[0].imshow(self.gray, cmap="gray", vmin=0, vmax=255)
        axes[0].add_patch(Rectangle((x - 1.5, y - 1.5), 3, 3,
                                   edgecolor="#ff6b00", facecolor="none", linewidth=2))
        axes[0].plot(x, y, "+", color="#ff6b00")
        axes[0].set_title(f"Окно: x={x}, y={y}", fontsize=10)
        for axis, matrix, title in zip(axes[1:], [patch, weights, products],
                                       ["Окно P", "Ядро после переворота", "P × ядро (поэлементно)"]):
            axis.imshow(np.zeros((3, 3)), cmap="Blues", vmin=-1, vmax=1)
            for row in range(3):
                for column in range(3):
                    axis.text(column, row, f"{matrix[row, column]:g}", ha="center", va="center", fontsize=12)
            axis.set_title(title, fontsize=9)
        for axis in axes:
            axis.set_axis_off()
        gx, gy = self.results["gx"][y, x], self.results["gy"][y, x]
        magnitude = self.results["magnitude"][y, x]
        self.explanation.set(
            f"{self.kernel_name.get()}: сумма 9 произведений = {products.sum():g}. "
            f"Gx={gx:g}, Gy={gy:g}; |G| = √(({gx:g})² + ({gy:g})²) = {magnitude:.3f}.\n"
            "Окно движется слева направо, затем переходит на следующую строку. "
            "За краем повторяется ближайший пиксель. Резкая смена яркости даёт большой |G|. "
            "На экране y растёт вниз.")
        self.lesson_canvas.draw_idle()

    def pick_pixel(self, event):
        if self.gray is not None and event.inaxes is getattr(self, "image_axis", None):
            if event.xdata is None or event.ydata is None:
                return
            height, width = self.gray.shape
            self.x.set(str(int(np.clip(round(event.xdata), 0, width - 1))))
            self.y.set(str(int(np.clip(round(event.ydata), 0, height - 1))))
            self.draw_lesson()

    def step(self):
        if self.gray is None:
            return
        try:
            x, y = self.coordinates()
        except ValueError:
            self.draw_lesson()
            return
        height, width = self.gray.shape
        position = (y * width + x + 1) % (height * width)
        self.x.set(str(position % width))
        self.y.set(str(position // width))
        self.draw_lesson()

    def stop_play(self):
        self.playing = False
        self.play_button.configure(text="▶ Движение")
        if hasattr(self, "animation_id"):
            self.root.after_cancel(self.animation_id)
            del self.animation_id

    def toggle_play(self):
        if self.playing:
            self.stop_play()
        elif self.gray is not None and not self.busy:
            self.playing = True
            self.play_button.configure(text="Ⅱ Пауза")
            self.animate()

    def animate(self):
        if self.playing:
            self.step()
            if self.playing:
                self.animation_id = self.root.after(350, self.animate)

    def save(self):
        if self.gray is None or self.busy:
            messagebox.showinfo("Сохранение", "Сначала загрузите изображение и дождитесь вычислений.")
            return
        compare = self.method.get() == "Сравнить все"
        formats = [("PNG", "*.png"), ("JPEG", "*.jpg")]
        if not compare:
            formats.append(("BMP", "*.bmp"))
        path = filedialog.asksaveasfilename(
            title="Сохранить сравнение" if compare else "Сохранить карту границ",
            defaultextension=".png", filetypes=formats)
        if not path:
            return
        try:
            if compare:
                # Сравнение экспортируем с подписями, отдельный метод — как H×W.
                self.figure.savefig(path, dpi=160, facecolor=self.figure.get_facecolor())
            else:
                save_image(path, self.results[self.method.get().lower()])
        except Exception as error:
            messagebox.showerror("Ошибка сохранения", str(error))
            return
        self.status.set(f"Сохранено: {path}")


if __name__ == "__main__":
    window = tk.Tk()
    ConvolutionApp(window)
    window.mainloop()

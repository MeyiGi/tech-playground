from pathlib import Path
import argparse

import cv2
import matplotlib.pyplot as plt
import numpy as np


def fourier_filter(image, sigma=0.08):
    # Дополняем края отражением, чтобы уменьшить артефакты на границе.
    padded = np.pad(image, 32, mode="reflect")
    height, width = padded.shape
    fy = np.fft.fftfreq(height)[:, None]
    fx = np.fft.fftfreq(width)[None, :]

    # Низкие частоты сохраняем, высокие плавно ослабляем.
    mask = np.exp(-(fx**2 + fy**2) / (2 * sigma**2))
    spectrum = np.fft.fft2(padded)
    result = np.fft.ifft2(spectrum * mask).real
    result = result[32:-32, 32:-32]
    return np.clip(np.rint(result), 0, 255).astype(np.uint8)


def make_example():
    # Простой исходник нужен, чтобы проверить фильтры без своей фотографии.
    clean = np.tile(np.linspace(40, 200, 400), (300, 1)).astype(np.uint8)
    cv2.rectangle(clean, (40, 50), (170, 240), 70, -1)
    cv2.circle(clean, (280, 145), 70, 220, -1)
    cv2.putText(clean, "TEST", (180, 270), cv2.FONT_HERSHEY_SIMPLEX, 1, 30, 2)

    rng = np.random.default_rng(42)
    noisy = clean.astype(float) + rng.normal(0, 18, clean.shape)
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)
    points = rng.random(clean.shape)
    noisy[points < 0.015] = 0
    noisy[points > 0.985] = 255
    return clean, noisy


def apply_filters(image):
    median = cv2.medianBlur(image, 3)
    return {
        "До обработки": image,
        "Гаусс, окно 5×5": cv2.GaussianBlur(image, (5, 5), 1),
        "Медиана, окно 3×3": median,
        "Медиана → Гаусс": cv2.GaussianBlur(median, (5, 5), 1),
        "Фурье, НЧ-фильтр": fourier_filter(image),
    }


def main():
    parser = argparse.ArgumentParser(description="Удаление шума и гистограммы")
    parser.add_argument("image", nargs="?", help="Путь к зашумлённой картинке")
    parser.add_argument("--no-show", action="store_true", help="Только сохранить результат")
    args = parser.parse_args()

    clean = None
    if args.image:
        # imdecode работает и с русскими буквами в пути.
        try:
            data = np.fromfile(args.image, dtype=np.uint8)
            image = cv2.imdecode(data, cv2.IMREAD_GRAYSCALE) if data.size else None
        except OSError:
            image = None
        if image is None:
            parser.error("Не удалось прочитать изображение. Проверьте путь и формат.")
    else:
        clean, image = make_example()

    results = apply_filters(image)
    output = Path("results")
    output.mkdir(exist_ok=True)
    fig, axes = plt.subplots(2, len(results), figsize=(18, 7))

    for column, (title, result) in enumerate(results.items()):
        axes[0, column].imshow(result, cmap="gray", vmin=0, vmax=255)
        axes[0, column].set_title(title)
        axes[0, column].axis("off")

        axes[1, column].hist(result.ravel(), bins=256, range=(0, 256), color="gray")
        axes[1, column].set_xlim(0, 255)
        axes[1, column].set_xlabel("Яркость")
        axes[1, column].set_ylabel("Число пикселей")
        cv2.imencode(".png", result)[1].tofile(output / f"{column}.png")

        # Сравнивать ошибку можно только при наличии чистого исходника.
        if clean is not None:
            mse = np.mean((clean.astype(float) - result.astype(float)) ** 2)
            print(f"{title}: MSE = {mse:.1f}")

    fig.tight_layout()
    fig.savefig(output / "comparison.png", dpi=150)
    if clean is not None:
        cv2.imencode(".png", clean)[1].tofile(output / "clean.png")
    print(f"Результаты сохранены в {output.resolve()}")
    if not args.no_show:
        plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()

import argparse
from pathlib import Path

from PIL import Image


def create_circle_mask(width, height, center_x, center_y, radius):
    """Строим круг вручную по уравнению (x - cx)² + (y - cy)² <= r²."""
    return [
        [
            (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2
            for x in range(width)
        ]
        for y in range(height)
    ]


def multiply_circle(pixels, mask, factor=100):
    """Храним результат в матрице: здесь значения могут быть больше 255."""
    return [
        [
            tuple(channel * factor for channel in pixel) if mask[y][x] else pixel
            for x, pixel in enumerate(row)
        ]
        for y, row in enumerate(pixels)
    ]


def normalize_circle(pixels, mask):
    """Масштабируем каналы внутри круга: значение * 255 / максимум."""
    maximum = max(
        (
            max(pixel)
            for y, row in enumerate(pixels)
            for x, pixel in enumerate(row)
            if mask[y][x]
        ),
        default=0,
    )
    if maximum == 0:
        return [row.copy() for row in pixels]

    return [
        [
            tuple(channel * 255 // maximum for channel in pixel)
            if mask[y][x] else pixel
            for x, pixel in enumerate(row)
        ]
        for y, row in enumerate(pixels)
    ]


def pixels_to_image(pixels):
    """Обрезаем значения до 0–255 только при выводе в RGB-изображение."""
    image = Image.new("RGB", (len(pixels[0]), len(pixels)))
    for y, row in enumerate(pixels):
        for x, pixel in enumerate(row):
            image.putpixel((x, y), tuple(min(255, max(0, c)) for c in pixel))
    return image


def main():
    directory = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="Круг, пересвет и ручная нормализация")
    parser.add_argument("--input", type=Path, default=directory / "data/cat_image.jpg")
    parser.add_argument("--output", type=Path, default=directory / "output")
    parser.add_argument("--show", action="store_true", help="Открыть результаты в просмотрщике")
    args = parser.parse_args()

    width, height = 1600, 1200
    with Image.open(args.input) as source:
        original = source.convert("RGB").resize((width, height))

    pixels = [
        [original.getpixel((x, y)) for x in range(width)]
        for y in range(height)
    ]
    mask = create_circle_mask(width, height, width // 2, height // 2, 500)
    multiplied = multiply_circle(pixels, mask)
    # Используем большие числа, а не уже обрезанные белые пиксели.
    normalized = normalize_circle(multiplied, mask)
    mask_pixels = [
        [(255, 255, 255) if inside else (0, 0, 0) for inside in row]
        for row in mask
    ]

    args.output.mkdir(parents=True, exist_ok=True)
    for name, image in (
        ("original", original),
        ("circle_mask", pixels_to_image(mask_pixels)),
        ("multiplied", pixels_to_image(multiplied)),
        ("normalized", pixels_to_image(normalized)),
    ):
        path = args.output / f"{name}.png"
        image.save(path)
        print(f"Сохранено: {path}")
        if args.show:
            image.show(title=name)


if __name__ == "__main__":
    main()

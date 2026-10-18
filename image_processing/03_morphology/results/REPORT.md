# Результаты домашней работы

Вход: `binary_image.png`; размер: 668×459.
Порог: 127, инверсия: False; белый объект, чёрный фон.

NumPy 2.5.4; OpenCV 5.0.0; SciPy 1.18.1

Сравнений: 50. Полностью совпали: 50.

| Пример / операция | Различных пикселей | Максимальная ошибка | NumPy, мс | Библиотека, мс |
|---|---:|---:|---:|---:|---:|
| input/erosion | 0 | 0 | 0.575 | 0.927 |
| input/dilation | 0 | 0 | 1.141 | 0.079 |
| input/opening | 0 | 0 | 1.101 | 0.129 |
| input/closing | 0 | 0 | 1.068 | 0.118 |
| input/gradient | 0 | 0 | 1.375 | 0.158 |
| input/white_top_hat | 0 | 0 | 1.255 | 0.139 |
| input/black_top_hat | 0 | 0 | 1.206 | 0.142 |
| input/contour | 0 | 0 | 0.928 | 0.097 |
| binary_demo/erosion | 0 | 0 | 0.258 | 0.035 |
| binary_demo/dilation | 0 | 0 | 0.25 | 0.034 |
| binary_demo/opening | 0 | 0 | 0.439 | 0.045 |
| binary_demo/closing | 0 | 0 | 0.466 | 0.046 |
| binary_demo/gradient | 0 | 0 | 0.485 | 0.051 |
| binary_demo/white_top_hat | 0 | 0 | 0.51 | 0.05 |
| binary_demo/black_top_hat | 0 | 0 | 0.469 | 0.055 |
| binary_demo/contour | 0 | 0 | 0.298 | 0.056 |
| grayscale/erosion | 0 | 0 | 0.261 | 0.035 |
| grayscale/dilation | 0 | 0 | 0.247 | 0.035 |
| grayscale/opening | 0 | 0 | 0.427 | 0.045 |
| grayscale/closing | 0 | 0 | 0.434 | 0.046 |
| grayscale/gradient | 0 | 0 | 0.524 | 0.05 |
| grayscale/white_top_hat | 0 | 0 | 0.477 | 0.05 |
| grayscale/black_top_hat | 0 | 0 | 0.477 | 0.052 |
| grayscale/contour | 0 | 0 | 0.285 | 0.041 |
| input/zhang_suen | 0 | 0 | 32.621 | 7.849 |
| input/guo_hall | 0 | 0 | 174.544 | 11.217 |
| input/erosion_skeleton | 0 | 0 | 9.641 | 2.335 |
| binary_demo/zhang_suen | 0 | 0 | 10.071 | 2.142 |
| binary_demo/guo_hall | 0 | 0 | 26.096 | 2.624 |
| binary_demo/erosion_skeleton | 0 | 0 | 5.519 | 0.827 |
| shape/square | 0 | 0 | 0.401 | 0.05 |
| shape/cross | 0 | 0 | 0.14 | 0.019 |
| shape/horizontal | 0 | 0 | 0.104 | 0.016 |
| shape/vertical | 0 | 0 | 0.08 | 0.014 |
| shape/diagonal | 0 | 0 | 0.108 | 0.014 |
| shape/disk | 0 | 0 | 0.208 | 0.024 |
| size/3/white_top_hat | 0 | 0 | 0.345 | 0.049 |
| size/3/black_top_hat | 0 | 0 | 0.243 | 0.025 |
| size/5/white_top_hat | 0 | 0 | 0.418 | 0.029 |
| size/5/black_top_hat | 0 | 0 | 0.381 | 0.028 |
| size/11/white_top_hat | 0 | 0 | 1.333 | 0.047 |
| size/11/black_top_hat | 0 | 0 | 1.336 | 0.045 |
| anchor/(0, 0) | 0 | 0 | 0.352 | 0.061 |
| anchor/(2, 2) | 0 | 0 | 0.321 | 0.036 |
| anchor/(4, 4) | 0 | 0 | 0.275 | 0.029 |
| padding/constant | 0 | 0 | 0.178 | 0.027 |
| padding/edge | 0 | 0 | 0.127 | 0.009 |
| padding/reflect | 0 | 0 | 0.123 | 0.007 |
| nonflat/erosion | 0 | 0 | 0.529 | 0.401 |
| nonflat/dilation | 0 | 0 | 0.544 | 0.422 |

Время — один запуск без прогрева и повторов; это иллюстрация, не бенчмарк.
Контур и скелет по эрозиям сравниваются с композицией OpenCV; thinning — с cv2.ximgproc.thinning;
неплоские операции — с SciPy; остальные — с OpenCV morphologyEx.

Для thinning обеим реализациям задан нулевой фон за границей. Для плоской морфологии по умолчанию
используется нейтральный фон: 255 для эрозии, 0 для дилатации. Сравнения включают края.

Разные способы получения скелета могут различаться между собой: каждый сравнивается со своим эталоном.

Opening удаляет одиночные светлые точки; closing заполняет маленькое отверстие в прямоугольнике.
White top-hat выделяет мелкие светлые детали, black top-hat — тёмные. При увеличении ядра
меняется масштаб выделяемых деталей. Форма ядра задаёт направления расширения, anchor сдвигает результат.

![Бинарная морфология](binary_demo_overview.png)
![Полутоновая морфология](grayscale_overview.png)
![Скелеты исходного изображения](input_skeletons.png)
![Скелеты фигур](binary_demo_skeletons.png)
![Форма ядра](kernel_shapes.png)
![Размер ядра](kernel_sizes.png)
![Anchor](kernel_anchors.png)
![Padding](padding.png)
![Неплоское ядро](nonflat_overview.png)

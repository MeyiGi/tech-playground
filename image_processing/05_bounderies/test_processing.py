"""Проверки наблюдаемого поведения ручных операторов и файлового ввода."""

import tempfile
import unittest
from pathlib import Path

import cv2
import numpy as np

from processing import canny, convolve2d, derivatives, load_image, normalize, save_image


class ProcessingTests(unittest.TestCase):
    def test_numeric_example(self):
        gray = np.array([[0, 0, 100]] * 3, dtype=np.uint8)
        result = derivatives(gray)
        self.assertEqual(result["gx"][1, 1], 400)
        self.assertEqual(result["gy"][1, 1], 0)
        self.assertEqual(result["magnitude"][1, 1], 400)
        self.assertEqual(result["sobel"][1, 1], 255)

    def test_both_gradient_components(self):
        y, x = np.mgrid[:5, :7]
        result = derivatives((10 * x + 20 * y).astype(np.uint8))
        self.assertEqual(result["gx"][2, 3], 80)
        self.assertEqual(result["gy"][2, 3], 160)
        self.assertAlmostEqual(result["magnitude"][2, 3], np.sqrt(80**2 + 160**2))
        self.assertEqual(result["laplacian_raw"][2, 3], 0)

    def test_true_convolution_and_border_against_reference(self):
        gray = np.arange(20, dtype=np.uint8).reshape(4, 5)
        kernel = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]], dtype=float)
        # filter2D выполняет корреляцию; переворот превращает её в свёртку.
        expected = cv2.filter2D(gray, cv2.CV_64F, kernel[::-1, ::-1],
                                borderType=cv2.BORDER_REPLICATE)
        np.testing.assert_allclose(convolve2d(gray, kernel), expected)

    def test_constant_and_tiny_images_have_no_edges(self):
        for shape in [(1, 1), (1, 5), (5, 1), (7, 9)]:
            with self.subTest(shape=shape):
                gray = np.full(shape, 100, dtype=np.uint8)
                for result in derivatives(gray).values():
                    self.assertEqual(result.shape, shape)
                    self.assertFalse(result.any())
                self.assertFalse(canny(gray).any())

    def test_laplacian_impulse_preserves_sign(self):
        gray = np.zeros((5, 5), dtype=np.uint8)
        gray[2, 2] = 100
        result = derivatives(gray)
        self.assertEqual(result["laplacian_raw"][2, 2], -400)
        self.assertEqual(result["laplacian_raw"][2, 3], 100)
        self.assertEqual(result["laplacian"][2, 2], 255)

    def test_normalization(self):
        result = normalize(np.array([[0, 100, 200]]))
        np.testing.assert_array_equal(result, [[0, 128, 255]])
        self.assertEqual(result.dtype, np.uint8)
        self.assertFalse(normalize(np.zeros((2, 2))).any())

    def test_canny_step_and_threshold_validation(self):
        gray = np.zeros((30, 30), dtype=np.uint8)
        gray[:, 15:] = 255
        edges = canny(gray)
        self.assertEqual(edges.shape, gray.shape)
        self.assertEqual(set(np.unique(edges)), {0, 255})
        self.assertTrue(edges[:, 12:18].any())
        self.assertFalse(edges[:, :10].any())
        for low, high in [(-1, 150), (150, 50), (50, 50), (0, 256)]:
            with self.assertRaises(ValueError):
                canny(gray, low, high)

    def test_file_round_trip_and_invalid_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "пример.png"
            gray = np.arange(30, dtype=np.uint8).reshape(5, 6)
            save_image(path, gray)
            rgb, loaded = load_image(path)
            self.assertEqual(rgb.shape, (5, 6, 3))
            np.testing.assert_array_equal(loaded, gray)
            path.write_bytes(b"not an image")
            with self.assertRaises(ValueError):
                load_image(path)
            with self.assertRaises(ValueError):
                save_image(Path(directory) / "invalid.txt", gray)

    def test_invalid_shapes(self):
        for gray in [np.zeros((3, 3, 3)), np.array([])]:
            with self.assertRaises(ValueError):
                convolve2d(gray, np.ones((3, 3)))
        with self.assertRaises(ValueError):
            convolve2d(np.zeros((3, 3)), np.ones((2, 2)))


if __name__ == "__main__":
    unittest.main()

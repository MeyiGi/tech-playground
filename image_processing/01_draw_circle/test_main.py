import unittest

from main import (
    create_circle_mask,
    multiply_circle,
    normalize_circle,
    pixels_to_image,
)


class CircleProcessingTests(unittest.TestCase):
    def test_circle_includes_boundary_and_excludes_corners(self):
        self.assertEqual(create_circle_mask(3, 3, 1, 1, 1), [
            [False, True, False],
            [True, True, True],
            [False, True, False],
        ])

    def test_multiplication_retains_details_before_saving(self):
        pixels = [[(40, 100, 200), (240, 250, 255)]]
        mask = [[True, False]]
        multiplied = multiply_circle(pixels, mask)
        self.assertEqual(multiplied, [[(4000, 10000, 20000), pixels[0][1]]])
        self.assertEqual(pixels_to_image(multiplied).getpixel((0, 0)), (255, 255, 255))
        self.assertEqual(
            normalize_circle(multiplied, mask),
            [[(51, 127, 255), pixels[0][1]]],
        )
        self.assertEqual(pixels[0][0], (40, 100, 200))
        self.assertEqual(multiplied[0][0], (4000, 10000, 20000))

    def test_normalization_uses_one_maximum_for_entire_circle(self):
        pixels = [[(1, 2, 4), (5, 8, 10)]]
        mask = [[True, True]]
        self.assertEqual(
            normalize_circle(multiply_circle(pixels, mask), mask),
            [[(25, 51, 102), (127, 204, 255)]],
        )

    def test_normalization_restores_image_with_maximum_255(self):
        pixels = [[(10, 80, 255), (50, 100, 150)]]
        mask = [[True, True]]
        self.assertEqual(normalize_circle(multiply_circle(pixels, mask), mask), pixels)

    def test_black_circle_and_empty_mask_do_not_divide_by_zero(self):
        pixels = [[(0, 0, 0), (20, 30, 40)]]
        for mask in ([[True, False]], [[False, False]]):
            with self.subTest(mask=mask):
                self.assertEqual(normalize_circle(pixels, mask), pixels)


if __name__ == "__main__":
    unittest.main()

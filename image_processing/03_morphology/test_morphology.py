"""Проверка по независимым библиотекам и небольшим примерам с известным ответом."""

import unittest

import cv2
import numpy as np
from numpy.testing import assert_array_equal, assert_allclose
from scipy import ndimage

import morphology as m
from main import OPERATIONS, binary_example, library_flat, library_skeleton, library_thinning


class FlatMorphologyTests(unittest.TestCase):
    def test_worked_binary_example(self):
        image = np.zeros((7, 7), dtype=np.uint8)
        image[2:5, 2:5] = 255
        expected_eroded = np.zeros_like(image)
        expected_eroded[3, 3] = 255
        expected_dilated = np.zeros_like(image)
        expected_dilated[1:6, 1:6] = 255
        kernel = m.structuring_element()
        assert_array_equal(m.erosion(image, kernel), expected_eroded)
        assert_array_equal(m.dilation(image, kernel), expected_dilated)

    def test_all_operations_match_opencv_including_edges(self):
        rng = np.random.default_rng(2026)
        for shape in ((1, 1), (1, 8), (8, 1), (13, 17)):
            gray = rng.integers(0, 256, shape, dtype=np.uint8)
            for image in (gray, (gray > 127).astype(np.uint8) * 255):
                for size in (3, 5):
                    for form in ("square", "cross", "horizontal", "vertical", "diagonal", "disk"):
                        kernel = m.structuring_element(form, size)
                        for name, (manual, code) in OPERATIONS.items():
                            with self.subTest(shape=shape, size=size, form=form, operation=name):
                                assert_array_equal(manual(image, kernel), library_flat(image, kernel, code))

    def test_padding_asymmetric_mask_and_offcenter_anchor(self):
        image = np.random.default_rng(7).integers(0, 256, (8, 11), dtype=np.uint8)
        # Прямоугольная маска чётной высоты проверяет соглашение об anchor.
        kernel = np.array([[1, 0, 1], [0, 1, 0]], dtype=np.uint8)
        for anchor in ((0, 0), (1, 2), (0, 1)):
            for padding, border in (("constant", cv2.BORDER_CONSTANT), ("edge", cv2.BORDER_REPLICATE),
                                    ("reflect", cv2.BORDER_REFLECT_101)):
                for name, (manual, code) in OPERATIONS.items():
                    with self.subTest(anchor=anchor, padding=padding, operation=name):
                        actual = manual(image, kernel, anchor=anchor, padding=padding, border_value=17)
                        expected = library_flat(image, kernel, code, anchor=anchor[::-1],
                                                borderType=border, borderValue=17)
                        assert_array_equal(actual, expected)

    def test_opening_removes_spot_closing_fills_hole(self):
        image = np.zeros((15, 15), dtype=np.uint8)
        image[4:11, 4:11] = 255
        image[1, 1] = 255
        kernel = m.structuring_element()
        expected = image.copy()
        expected[1, 1] = 0
        assert_array_equal(m.opening(image, kernel), expected)
        expected[7, 7] = 0
        assert_array_equal(m.closing(expected, kernel), m.opening(image, kernel))

    def test_grayscale_values_and_subtraction_do_not_wrap(self):
        image = np.array([[10, 200, 10]], dtype=np.uint8)
        kernel = m.structuring_element("horizontal")
        assert_array_equal(m.erosion(image, kernel), [[10, 10, 10]])
        assert_array_equal(m.dilation(image, kernel), [[200, 200, 200]])
        assert_array_equal(m.white_top_hat(image, kernel), [[0, 190, 0]])

    def test_invalid_input_and_no_mutation(self):
        image = np.arange(25, dtype=np.uint8).reshape(5, 5)
        original = image.copy()
        for manual, _ in OPERATIONS.values():
            manual(image, m.structuring_element())
        assert_array_equal(image, original)
        for kernel in (np.zeros((3, 3)), [], [1, 1]):
            with self.assertRaises(ValueError):
                m.erosion(image, kernel)
        for anchor in ((-1, 0), (3, 0), (0.5, 1)):
            with self.assertRaises(ValueError):
                m.dilation(image, np.ones((3, 3)), anchor=anchor)
        with self.assertRaises(ValueError):
            m.erosion(image.astype(float), np.ones((3, 3)))
        with self.assertRaises(ValueError):
            m.erosion(image, np.ones((3, 3)), padding="unknown")


class NonflatTests(unittest.TestCase):
    def test_matches_scipy_with_asymmetric_heights_and_anchor(self):
        image = np.random.default_rng(8).normal(100, 50, (9, 12))
        for shape in ((3, 3), (2, 4)):
            structure = np.arange(np.prod(shape), dtype=float).reshape(shape) - 3
            footprint = np.ones(shape, dtype=bool)
            footprint[0, -1] = False
            for anchor in ((0, 0), (shape[0] // 2, shape[1] // 2)):
                origin = tuple(a - s // 2 for a, s in zip(anchor, shape))
                for padding, mode in (("constant", "constant"), ("edge", "nearest"), ("reflect", "mirror")):
                    for operation in ("erosion", "dilation"):
                        with self.subTest(shape=shape, anchor=anchor, padding=padding, operation=operation):
                            actual = m.nonflat_morphology(image, structure, operation, footprint=footprint,
                                                          anchor=anchor, padding=padding, border_value=13)
                            expected = getattr(ndimage, f"grey_{operation}")(
                                image, structure=structure, footprint=footprint, origin=origin, mode=mode, cval=13)
                            assert_allclose(actual, expected, rtol=0, atol=1e-12)

    def test_zero_height_is_active_and_values_are_not_clipped(self):
        image = np.array([[0., 255.]])
        assert_array_equal(m.nonflat_morphology(image, [[10]], "erosion"), [[-10, 245]])
        assert_array_equal(m.nonflat_morphology(image, [[10]], "dilation"), [[10, 265]])
        assert_array_equal(m.nonflat_morphology(image, [[0]], "erosion"), image)


class SkeletonTests(unittest.TestCase):
    def test_thinning_matches_opencv_on_shapes_edges_and_random_masks(self):
        rng = np.random.default_rng(42)
        images = [binary_example(), np.zeros((9, 11), np.uint8), np.full((9, 11), 255, np.uint8),
                  np.array([[255]], dtype=np.uint8), np.full((1, 9), 255, np.uint8),
                  np.full((9, 1), 255, np.uint8)]
        images += [(rng.random((23, 29)) > density).astype(np.uint8) * 255
                   for density in (0.2, 0.5, 0.8) for _ in range(10)]
        for image in images:
            original = image.copy()
            for manual, code in ((m.zhang_suen, cv2.ximgproc.THINNING_ZHANGSUEN),
                                  (m.guo_hall, cv2.ximgproc.THINNING_GUOHALL)):
                with self.subTest(shape=image.shape, method=manual.__name__):
                    result = manual(image)
                    assert_array_equal(result, library_thinning(image, code))
                    assert_array_equal(manual(result), result)  # Достигнута сходимость.
                    self.assertFalse(np.any((result > 0) & (image == 0)))
                    assert_array_equal(image, original)

    def test_preserves_connectivity_hole_and_line_endpoints(self):
        image = np.zeros((35, 35), dtype=np.uint8)
        image[5:30, 5:30] = 255
        image[12:23, 12:23] = 0
        line = np.zeros((9, 11), dtype=np.uint8)
        line[4, 2:9] = 255
        for manual in (m.zhang_suen, m.guo_hall):
            result = manual(image)
            self.assertEqual(ndimage.label(result, structure=np.ones((3, 3)))[1], 1)
            self.assertEqual(ndimage.label(result == 0)[1], 2)  # Внешний фон + отверстие.
            self.assertLess(np.count_nonzero(result), np.count_nonzero(image))
            assert_array_equal(manual(line), line)

    def test_erosion_skeleton_matches_independent_composition(self):
        for image in (binary_example(), np.full((9, 11), 255, np.uint8), np.zeros((1, 1), np.uint8)):
            assert_array_equal(m.morphological_skeleton(image), library_skeleton(image))

    def test_binary_representations_and_invalid_input(self):
        image = binary_example()
        for manual in (m.zhang_suen, m.guo_hall, m.morphological_skeleton):
            assert_array_equal(manual(image), manual(image > 0))
            assert_array_equal(manual(image), manual(image // 255))
            with self.assertRaises(ValueError):
                manual(np.array([[128]], dtype=np.uint8))
        with self.assertRaises(ValueError):
            m.thinning(image, "unknown")


if __name__ == "__main__":
    unittest.main()

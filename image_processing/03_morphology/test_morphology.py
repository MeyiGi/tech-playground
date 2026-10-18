import unittest
import numpy as np
from numpy.testing import assert_array_equal
from scipy import ndimage
import morphology as m
from compare import compare


class MorphologyTests(unittest.TestCase):
    def test_square(self):
        image = np.zeros((7, 7), dtype=int)
        image[2:5, 2:5] = 255
        eroded = np.zeros_like(image)
        eroded[3, 3] = 255
        dilated = np.zeros_like(image)
        dilated[1:6, 1:6] = 255
        kernel = np.ones((3, 3), dtype=int)
        assert_array_equal(m.erosion(image, kernel), eroded)
        assert_array_equal(m.dilation(image, kernel), dilated)

    def test_against_libraries(self):
        rng = np.random.default_rng(42)
        for shape in [(1, 1), (1, 9), (9, 1), (15, 17)]:
            gray = rng.integers(0, 256, shape, dtype="uint8")
            compare(gray)
            compare(np.where(gray > 127, 255, 0).astype("uint8"))

    def test_noise_and_hole(self):
        image = np.zeros((15, 15), dtype=int)
        image[4:11, 4:11] = 255
        noisy = image.copy()
        noisy[1, 1] = 255
        kernel = np.ones((3, 3), dtype=int)
        assert_array_equal(m.opening(noisy, kernel), image)
        hole = image.copy()
        hole[7, 7] = 0
        assert_array_equal(m.closing(hole, kernel), image)

    def test_thinning_preserves_ring_and_reaches_stable_result(self):
        image = np.zeros((25, 25), dtype=int)
        image[3:22, 3:22] = 255
        image[8:17, 8:17] = 0
        for thin in [m.zhang_suen, m.guo_hall]:
            result = thin(image)
            assert_array_equal(thin(result), result)
            self.assertEqual(ndimage.label(result, structure=np.ones((3, 3)))[1], 1)
            self.assertEqual(ndimage.label(result == 0)[1], 2)
            self.assertLess(np.count_nonzero(result), np.count_nonzero(image))

    def test_skeleton_of_line_and_empty_image(self):
        cross = np.zeros((9, 9), dtype=int)
        cross[4, 2:7] = 255
        for function in [m.zhang_suen, m.guo_hall, m.morphological_skeleton]:
            assert_array_equal(function(cross), cross)
            assert_array_equal(function(np.zeros((3, 3), dtype=int)), np.zeros((3, 3)))
        self.assertTrue(np.any(m.morphological_skeleton(np.full((5, 5), 255))))

    def test_nonflat_does_not_clip_values(self):
        image = np.array([[0, 255]], dtype=int)
        kernel = np.ones((1, 1), dtype=int)
        assert_array_equal(m.erosion(image, kernel, heights=np.array([[10]])), [[-10, 245]])
        assert_array_equal(m.dilation(image, kernel, heights=np.array([[10]])), [[10, 265]])


if __name__ == "__main__":
    unittest.main()

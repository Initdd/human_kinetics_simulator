import unittest
from utils.line import Line

class TestLine(unittest.TestCase):
    def setUp(self):
        self.line1 = Line((0, 0), (3, 4))
        self.line2 = Line((0, 0), (4, 3))
        self.line3 = Line((0, 0), (-3, 4))
        self.line4 = Line((0, 0), (4, 0))

    def test_length(self):
        self.assertEqual(self.line1.length(), 5)

    def test_slope(self):
        self.assertEqual(self.line1.slope(), 4/3)
        self.assertEqual(self.line2.slope(), 3/4)

    def test_is_parallel(self):
        line_parallel = Line((1, 1), (4, 5))
        self.assertTrue(self.line1.is_parallel(line_parallel))
        self.assertFalse(self.line1.is_parallel(self.line2))

    def test_is_perpendicular(self):
        line_perpendicular = Line((0, 0), (4, -3))
        self.assertTrue(self.line1.is_perpendicular(line_perpendicular))
        self.assertFalse(self.line1.is_perpendicular(self.line2))

    def test_translate(self):
        self.line1.translate(1, 1)
        self.assertEqual(self.line1.start_point, (1, 1))
        self.assertEqual(self.line1.end_point, (4, 5))

    def test_rotate_on_origin(self):
        self.line1.rotate_on_origin(90)
        self.assertAlmostEqual(self.line1.start_point[0], 0, places=5)
        self.assertAlmostEqual(self.line1.start_point[1], 0, places=5)
        self.assertAlmostEqual(self.line1.end_point[0], -4, places=5)
        self.assertAlmostEqual(self.line1.end_point[1], 3, places=5)

    def test_rotate_on_point(self):
        # Rotate 90 degrees clockwise
        self.line4.rotate_on_point(90, self.line4.start_point)
        self.assertAlmostEqual(self.line4.start_point[0], 0, places=5)
        self.assertAlmostEqual(self.line4.start_point[1], 0, places=5)
        self.assertAlmostEqual(self.line4.end_point[0], 0, places=5)
        self.assertAlmostEqual(self.line4.end_point[1], 4, places=5)

    def test_get_rotation(self):
        line = Line((1, 1), (3, 14))
        rotation = line.get_rotation()
        #self.assertAlmostEqual(rotation, 78.69006752597979, places=5)
        print(rotation)

    def test_str(self):
        self.assertEqual(str(self.line1), "Line((0, 0), (3, 4))")

if __name__ == '__main__':
    #unittest.main()
    line = Line((0, 0), (5, 5))
    line.rotate_on_point(100, line.start_point)
    rotation = line.get_rotation()
    #self.assertAlmostEqual(rotation, 78.69006752597979, places=5)
    print(rotation)
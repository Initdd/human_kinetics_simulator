import unittest
import typing as tp
from parts.limb import Limb

class TestLimb(unittest.TestCase):
    def setUp(self):
        self.limb = Limb(10, (0, 0), [45, 90])

    def test_init(self):
        self.assertEqual(self.limb.length, 10)
        self.assertEqual(self.limb.position, (0, 0))
        self.assertEqual(len(self.limb.parts), 2)

    def test_move(self):
        self.limb.move((10, 10))
        self.assertEqual(self.limb.position, (10, 10))

    def test_rotate_part(self):
        self.limb = Limb(10, (0, 0), [45, 45])
        self.limb.rotate_part(0, -45)
        angles = self.limb.get_angles()
        self.assertEqual(angles[0], 0)
        self.assertEqual(angles[1], 0)

    def test_get_crit_pos(self):
        positions = self.limb.get_crit_pos()
        self.assertEqual(len(positions), len(self.limb.parts) + 1)

    def test_get_angles(self):
        angles = self.limb.get_angles()
        self.assertEqual(len(angles), len(self.limb.parts))

    def test_get_length(self):
        self.assertEqual(self.limb.get_length(), 10)

    def test_set_angle(self):
        self.limb.set_angle(0, 90)
        angle = self.limb.get_angle(0)
        self.assertEqual(angle, 90)

    def test_get_angle(self):
        angle = self.limb.get_angle(0)
        self.assertEqual(angle, 45)

    def test_get_angle_big(self):
        limb = Limb(10, (0, 0), [45, 95])
        angle = limb.get_angle(1)
        self.assertAlmostEqual(angle, 95, places=2)

if __name__ == '__main__':
    unittest.main()
import unittest
import calculate_reflection_ceiling_cavity as calcu


class TestCalcu(unittest.TestCase):
    def test_calculate(self):
        data = calcu.calculateCavity(1, 1, 1, 1, 1)
        self.assertEqual(data, -0.06022527509949815)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    if __name__ == '__main__':
        unittest.main()

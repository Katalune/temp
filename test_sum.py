import unittest

from utilities import sum


class Tests(unittest.TestCase):
    def test_sum(self):
        """1 + 1 = 2"""
        self.assertEquals(sum(1, 1), 2)


if __name__ == "__main__":
    unittest.main()

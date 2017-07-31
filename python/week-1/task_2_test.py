import unittest
from task_2 import height_tree

class HeightTreeTestCase(unittest.TestCase):
    """Tests for `task_2.py`."""

    def test_1(self):
        self.assertEqual('3', height_tree([4, -1, 4, 1, 1]))


    def test_2(self):
        self.assertEqual('4', height_tree([-1, 0, 4, 0, 3]))


if __name__ == '__main__':
    unittest.main()

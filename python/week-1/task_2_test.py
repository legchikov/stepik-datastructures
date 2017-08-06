import unittest
from task_2 import height_tree, create_tree

class HeightTreeTestCase(unittest.TestCase):
    """Tests for `task_2.py`."""

    def setUp(self):
        self.root = -1

    def test_1(self):
        seq = [4, -1, 4, 1, 1]
        self.assertEqual(3, height_tree(create_tree(seq), self.root))

    def test_2(self):
        seq = [-1, 0, 4, 0, 3]
        self.assertEqual(4, height_tree(create_tree(seq), self.root))

    def test_3(self):
        seq = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]
        self.assertEqual(4, height_tree(create_tree(seq), self.root))

    def test_4(self):
        seq = [1, 2, 3, 4, 5, 6, 7, -1]
        self.assertEqual(8, height_tree(create_tree(seq), self.root))


if __name__ == '__main__':
    unittest.main()

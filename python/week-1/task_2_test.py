import unittest
from task_2 import height_tree

class HeightTreeTestCase(unittest.TestCase):
    """Tests for `task_2.py`."""

    def test_1(self):
        self.assertEqual('Success', height_tree())

if __name__ == '__main__':
    unittest.main()

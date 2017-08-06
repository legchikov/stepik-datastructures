import unittest
from task_3 import pocket_simulator

class PocketSimulatorTestCase(unittest.TestCase):
    """Tests for `task_3.py`."""

    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(None, pocket_simulator())


if __name__ == '__main__':
    unittest.main()

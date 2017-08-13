import unittest
from task_3 import pocket_simulator

class PocketSimulatorTestCase(unittest.TestCase):
    """Tests for `task_3.py`."""

    def setUp(self):
        pass

    def test_0(self):
        buffer_size = 1
        pockets = []
        self.assertEqual('', pocket_simulator(buffer_size, pockets))

    def test_1(self):
        buffer_size = 1
        pockets = [(0, 0)]
        self.assertEqual('0', pocket_simulator(buffer_size, pockets))

    def test_2(self):
        buffer_size = 1
        pockets = [(0, 1), (0, 1)]
        self.assertEqual('0 -1', pocket_simulator(buffer_size, pockets))

    def test_3(self):
        buffer_size = 1
        pockets = [(0, 1), (1, 1)]
        self.assertEqual('0 1', pocket_simulator(buffer_size, pockets))


if __name__ == '__main__':
    unittest.main()

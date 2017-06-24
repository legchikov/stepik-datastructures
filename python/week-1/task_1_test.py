import unittest
from task_1 import check_brackets

class CheckBracketsTestCase(unittest.TestCase):
    """Tests for `task_1.py`."""

    def test_1(self):
        self.assertEqual('Success', check_brackets('[]'))

    def test_2(self):
        self.assertEqual('Success', check_brackets('{}[]'))


    def test_3(self):
        self.assertEqual('Success', check_brackets('[()]'))


    def test_4(self):
        self.assertEqual('Success', check_brackets('(())'))


    def test_5(self):
        self.assertEqual('Success', check_brackets('{[]}()'))


    def test_6(self):
        self.assertEqual('1', check_brackets('('))


    def test_7(self):
        self.assertEqual('3', check_brackets('{[}'))


    def test_8(self):
        self.assertEqual('Success', check_brackets('foo(bar);'))


    def test_9(self):
        self.assertEqual('10', check_brackets('foo(bar[i);'))


if __name__ == '__main__':
    unittest.main()

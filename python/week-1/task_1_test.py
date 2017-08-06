import unittest
from task_1 import check_brackets

class CheckBracketsTestCase(unittest.TestCase):
    """Tests for `task_1.py`."""

    def test_suites(self):
        self.assertEqual('Success', check_brackets('[]'))
        self.assertEqual('Success', check_brackets('{}[]'))
        self.assertEqual('Success', check_brackets('[()]'))
        self.assertEqual('Success', check_brackets('(())'))
        self.assertEqual('Success', check_brackets('{[]}()'))
        self.assertEqual('1', check_brackets('('))
        self.assertEqual('3', check_brackets('{[}'))
        self.assertEqual('Success', check_brackets('foo(bar);'))
        self.assertEqual('10', check_brackets('foo(bar[i);'))
        self.assertEqual('5', check_brackets('()[]}'))
        self.assertEqual('Success', check_brackets(''))
        self.assertEqual('1', check_brackets(')'))
        self.assertEqual('3', check_brackets('{{{[][][]'))
        self.assertEqual('1', check_brackets(']{{}}'))

if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
import unittest

try:
    from .context import sissy_university
except ImportError:
    from context import sissy_university



class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()
# -*- coding: utf-8 -*-
import unittest

try:
    from .context import sissy_university
except ImportError:
    from context import sissy_university


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(sissy_university.hmm())


if __name__ == '__main__':
    unittest.main()

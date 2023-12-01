from unittest import TestCase

from dayx import p1, p2


class Test(TestCase):
    def test_p1(self):
        test_input = """ """.split("\n")
        expected = 0
        self.assertEqual(p1(test_input), expected)

    def test_p2(self):
        test_input = """ """.split("\n")
        expected = 0
        self.assertEqual(p2(test_input), expected)

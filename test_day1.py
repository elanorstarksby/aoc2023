from unittest import TestCase

from day1 import calculate_total, p1, p2


class Test(TestCase):
    def test_calculate_total_p1_beginning_end(self):
        test_input = "1abc2"
        self.assertEqual(calculate_total(test_input, 1), 12)

    def test_calculate_total_p1_middle_middle(self):
        test_input = "pqr3stu8vwx"
        self.assertEqual(calculate_total(test_input, 1), 38)

    def test_calculate_total_p1_multiple(self):
        test_input = "a1b2c3d4e5f"
        self.assertEqual(calculate_total(test_input, 1), 15)

    def test_calculate_total_p1_single_middle(self):
        test_input = "treb7uchet"
        self.assertEqual(calculate_total(test_input, 1), 77)

    def test_calculate_total_p2_mixed_letters(self):
        test_input = "two1nine"
        self.assertEqual(calculate_total(test_input, 2), 29)

    def test_calculate_total_p2_overlap(self):
        test_input = "eightwothree"
        self.assertEqual(calculate_total(test_input, 2), 83)

    def test_calculate_total_p2_mixed_both(self):
        test_input = "zoneight234"
        self.assertEqual(calculate_total(test_input, 2), 14)

    def test_p1(self):
        test_input = ("1abc2\n"
                      "pqr3stu8vwx\n"
                      "a1b2c3d4e5f\n"
                      "treb7uchet").split("\n")
        self.assertEqual(p1(test_input), 142)

    def test_p2(self):
        test_input = ("two1nine\n"
                      "eightwothree\n"
                      "abcone2threexyz\n"
                      "xtwone3four\n"
                      "4nineeightseven2\n"
                      "zoneight234\n"
                      "7pqrstsixteen").split("\n")
        self.assertEqual(p2(test_input), 281)

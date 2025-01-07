import unittest
from unittest.mock import patch
from first_requirement import One as FirstReq
from second_requirement import Two as SecondReq
from third_requirement import Three as ThirdReq
from fourth_requirement import Four as FourthReq
from fifth_requirement import Five as FifthReq


class TestFirstRequirement(unittest.TestCase):

    @patch("builtins.input", side_effect=["1,2"])
    def test_two_numbers(self, mock_input):
        obj = FirstReq()
        self.assertEqual(obj.first(), 3)  # 1 + 2 = 3

    @patch("builtins.input", side_effect=["1,-3"])
    def test_positive_and_negative(self, mock_input):
        obj = FirstReq()
        self.assertEqual(obj.first(), -2)  # 1 + (-3) = -2

    @patch("builtins.input", side_effect=["20"])
    def test_single_number(self, mock_input):
        obj = FirstReq()
        with self.assertRaises(TypeError):
            obj.first()  # Exception for less than 2 numbers

    @patch("builtins.input", side_effect=["5,tytyt"])
    def test_invalid_number(self, mock_input):
        obj = FirstReq()
        self.assertEqual(obj.first(), 5)  # 5 + 0 = 5

    @patch("builtins.input", side_effect=["1,2,3"])
    def test_more_than_two_numbers(self, mock_input):
        obj = FirstReq()
        with self.assertRaises(TypeError):
            obj.first()  # Exception for more than 2 numbers


class TestSecondRequirement(unittest.TestCase):

    @patch("builtins.input", side_effect=["1,2,3,4"])
    def test_multiple_numbers(self, mock_input):
        obj = SecondReq()
        self.assertEqual(obj.second(), 10)  # 1 + 2 + 3 + 4 = 10

    @patch("builtins.input", side_effect=["10,-5,5"])
    def test_positive_and_negative_multiple(self, mock_input):
        obj = SecondReq()
        self.assertEqual(obj.second(), 10)  # 10 + (-5) + 5 = 10

    @patch("builtins.input", side_effect=["100"])
    def test_single_number(self, mock_input):
        obj = SecondReq()
        with self.assertRaises(TypeError):
            obj.second()  # Exception for less than 2 numbers

    @patch("builtins.input", side_effect=["3,invalid,7"])
    def test_invalid_number(self, mock_input):
        obj = SecondReq()
        self.assertEqual(obj.second(), 10)  # 3 + 0 + 7 = 10

    @patch("builtins.input", side_effect=[" "])
    def test_empty_input(self, mock_input):
        obj = SecondReq()
        with self.assertRaises(TypeError):
            obj.second()  # Exception for less than 2 numbers


class TestThirdRequirement(unittest.TestCase):

    @patch("builtins.input", side_effect=["1,2,3,4"])
    def test_multiple_numbers(self, mock_input):
        obj = ThirdReq()
        self.assertEqual(obj.third(), 10)  # 1 + 2 + 3 + 4 = 10

    @patch("builtins.input", side_effect=["10,-5,5"])
    def test_positive_and_negative_multiple(self, mock_input):
        obj = ThirdReq()
        self.assertEqual(obj.third(), 10)  # 10 + (-5) + 5 = 10

    @patch("builtins.input", side_effect=["100"])
    def test_single_number(self, mock_input):
        obj = ThirdReq()
        with self.assertRaises(TypeError):
            obj.third()  # Exception for less than 2 numbers

    @patch("builtins.input", side_effect=["3,invalid,7"])
    def test_invalid_number(self, mock_input):
        obj = ThirdReq()
        self.assertEqual(obj.third(), 10)  # 3 + 0 + 7 = 10

    @patch("builtins.input", side_effect=[" "])
    def test_empty_input(self, mock_input):
        obj = ThirdReq()
        with self.assertRaises(TypeError):
            obj.third()  # Exception for less than 2 numbers

    @patch("builtins.input", side_effect=[r"87\n68"])
    def test_newline_separator(self, mock_input):
        obj = ThirdReq()
        self.assertEqual(obj.third(), 155)  # 87 + 68 = 155

    @patch("builtins.input", side_effect=["87&68"])
    def test_invalid_separator(self, mock_input):
        obj = ThirdReq()
        with self.assertRaises(TypeError):
            obj.third()  # Exception for less than 2 numbers


class TestFourthRequirement(unittest.TestCase):

    @patch("builtins.input", side_effect=["1,2,3,4"])
    def test_multiple_numbers(self, mock_input):
        obj = FourthReq()
        self.assertEqual(obj.fourth(), 10)  # 1 + 2 + 3 + 4 = 10

    @patch("builtins.input", side_effect=["10,-5,5"])
    def test_positive_and_negative_multiple(self, mock_input):
        obj = FourthReq()
        with self.assertRaises(TypeError):
            obj.fourth()  # Exception for negative numbers

    @patch("builtins.input", side_effect=[r"10,(5)\n5"])
    def test_negative_alt_format_mixed_separators(self, mock_input):
        obj = FourthReq()
        with self.assertRaises(TypeError):
            obj.fourth()  # Exception for negative numbers

    @patch("builtins.input", side_effect=["100"])
    def test_single_number(self, mock_input):
        obj = FourthReq()
        with self.assertRaises(TypeError):
            obj.fourth()  # Exception for less than 2 numbers

    @patch("builtins.input", side_effect=["3,invalid,7"])
    def test_invalid_number(self, mock_input):
        obj = FourthReq()
        self.assertEqual(obj.fourth(), 10)  # 3 + 0 + 7 = 10

    @patch("builtins.input", side_effect=[" "])
    def test_empty_input(self, mock_input):
        obj = FourthReq()
        with self.assertRaises(TypeError):
            obj.fourth()  # Exception for less than 2 numbers

    @patch("builtins.input", side_effect=[r"87\n68"])
    def test_newline_separator(self, mock_input):
        obj = FourthReq()
        self.assertEqual(obj.fourth(), 155)  # 87 + 68 = 155

    @patch("builtins.input", side_effect=["87&68"])
    def test_invalid_separator(self, mock_input):
        obj = FourthReq()
        with self.assertRaises(TypeError):
            obj.fourth()  # Exception for less than 2 numbers


class TestFifthRequirement(unittest.TestCase):

    @patch("builtins.input", side_effect=["1,2,3,4"])
    def test_multiple_numbers(self, mock_input):
        obj = FifthReq()
        self.assertEqual(obj.fifth(), 10)  # 1 + 2 + 3 + 4 = 10

    @patch("builtins.input", side_effect=["10,-5,5"])
    def test_positive_and_negative_multiple(self, mock_input):
        obj = FifthReq()
        with self.assertRaises(TypeError):
            obj.fifth()  # Exception for negative numbers

    @patch("builtins.input", side_effect=[r"10,(5)\n5"])
    def test_negative_alt_format_mixed_separators(self, mock_input):
        obj = FifthReq()
        with self.assertRaises(TypeError):
            obj.fifth()  # Exception for negative numbers

    @patch("builtins.input", side_effect=["100"])
    def test_single_number(self, mock_input):
        obj = FifthReq()
        with self.assertRaises(TypeError):
            obj.fifth()  # Exception for less than 2 numbers

    @patch("builtins.input", side_effect=["3,invalid,7"])
    def test_invalid_number(self, mock_input):
        obj = FifthReq()
        self.assertEqual(obj.fifth(), 10)  # 3 + 0 + 7 = 10

    @patch("builtins.input", side_effect=[" "])
    def test_empty_input(self, mock_input):
        obj = FifthReq()
        with self.assertRaises(TypeError):
            obj.fifth()  # Exception for less than 2 numbers

    @patch("builtins.input", side_effect=[r"87\n68"])
    def test_newline_separator(self, mock_input):
        obj = FifthReq()
        self.assertEqual(obj.fifth(), 155)  # 87 + 68 = 155

    @patch("builtins.input", side_effect=["87&68"])
    def test_invalid_separator(self, mock_input):
        obj = FifthReq()
        with self.assertRaises(TypeError):
            obj.fifth()  # Exception for less than 2 numbers

    @patch("builtins.input", side_effect=["600,5004,6005"])
    def test_invalid_number_length(self, mock_input):
        obj = FifthReq()
        self.assertEqual(obj.fifth(), 600)  # 600 + 0 + 0 = 600

    @patch("builtins.input", side_effect=[r"600\n5604,6007\n7005"])
    def test_mixed_separator_invalid_number_length(self, mock_input):
        obj = FifthReq()
        self.assertEqual(obj.fifth(), 600)  # 600 + 0 + 0 = 600


if __name__ == "__main__":
    unittest.main()

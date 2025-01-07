import unittest
from unittest.mock import patch
from fifth_requirement import Five as FifthReq
from sixth_requirement import Six as SixthReq


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


class TestSixthRequirement(unittest.TestCase):

    @patch("builtins.input", side_effect=["1,2,3,4"])
    def test_multiple_numbers(self, mock_input):
        obj = SixthReq()
        self.assertEqual(obj.sixth(), 10)  # 1 + 2 + 3 + 4 = 10

    @patch("builtins.input", side_effect=["10,-5,5"])
    def test_positive_and_negative_multiple(self, mock_input):
        obj = SixthReq()
        with self.assertRaises(TypeError):
            obj.sixth()  # Exception for negative numbers

    @patch("builtins.input", side_effect=[r"10,(5)\n5"])
    def test_negative_alt_format_mixed_separators(self, mock_input):
        obj = SixthReq()
        with self.assertRaises(TypeError):
            obj.sixth()  # Exception for negative numbers

    @patch("builtins.input", side_effect=["100"])
    def test_single_number(self, mock_input):
        obj = SixthReq()
        with self.assertRaises(TypeError):
            obj.sixth()  # Exception for less than 2 numbers

    @patch("builtins.input", side_effect=["3,invalid,7"])
    def test_invalid_number(self, mock_input):
        obj = SixthReq()
        self.assertEqual(obj.sixth(), 10)  # 3 + 0 + 7 = 10

    @patch("builtins.input", side_effect=[" "])
    def test_empty_input(self, mock_input):
        obj = SixthReq()
        with self.assertRaises(TypeError):
            obj.sixth()  # Exception for less than 2 numbers

    @patch("builtins.input", side_effect=[r"87\n68"])
    def test_newline_separator(self, mock_input):
        obj = SixthReq()
        self.assertEqual(obj.sixth(), 155)  # 87 + 68 = 155

    @patch("builtins.input", side_effect=["87&68"])
    def test_invalid_separator(self, mock_input):
        obj = SixthReq()
        with self.assertRaises(TypeError):
            obj.sixth()  # Exception for less than 2 numbers

    @patch("builtins.input", side_effect=[r"//#\n20#21#23"])
    def test_custom_separators(self, mock_input):
        obj = SixthReq()
        self.assertEqual(obj.sixth(), 64)  # 20 + 21 + 23 = 64

    @patch("builtins.input", side_effect=[r"//[#]\n20#21#23"])
    def test_custom_separators(self, mock_input):
        obj = SixthReq()
        with self.assertRaises(TypeError):
            obj.sixth()  # Should not accept block format custom seperators until req. 7

    @patch("builtins.input", side_effect=["600,5004,6005"])
    def test_invalid_number_length(self, mock_input):
        obj = SixthReq()
        self.assertEqual(obj.sixth(), 600)  # 600 + 0 + 0 = 600

    @patch("builtins.input", side_effect=[r"600\n5604,6007\n7005"])
    def test_mixed_separator_invalid_number_length(self, mock_input):
        obj = SixthReq()
        self.assertEqual(obj.sixth(), 600)  # 600 + 0 + 0 = 600


if __name__ == "__main__":
    unittest.main()

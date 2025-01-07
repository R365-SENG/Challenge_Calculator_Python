import re


class Calculator:
    def __init__(self):
        """A calculator that takes user input and performs mathematical operations.
        Invalid input is converted to zero.

        Attributes:
        operators               The numbers to be added.

        Methods:
        addition                Adds numbers together, printing the formula used and the result.
        check_for_separator     Checks for a valid separator. Default separator is a comma. (",")
        check_arg_quantity      Optional. Limits the quantity of numbers accepted as input. Default is 2.

        """
        self.arguments = self.__get_math_function_arguments__()

    # Separator is a protected keyword in Python. Default separator is a comma.
    def check_for_separator(
        self, arguments: str, separator_strings: list = [","]
    ) -> list:
        arguments = arguments.strip(" ")
        operators = []
        for string in separator_strings:
            arguments = arguments.replace(string, " ")
        operators = arguments.split(" ")

        if len(operators) < 2:
            raise TypeError(
                f"Please make sure you utilize one of the available separators: {separator_strings} "
            )
        return operators

    def check_exact_quantity(self, operators: list, quantity: int = 2) -> list:
        if len(operators) != quantity:
            raise TypeError(f"Please make sure you input {quantity} numbers.")
        return operators

    def check_minimum_quantity(self, operators: list, quantity: int = 2) -> list:
        if len(operators) < quantity:
            raise self.QuantityError
        return operators

    def deny_negative_inputs(
        self,
        operators: list,
        denied_formats: re.Pattern = re.compile(r"(^[(-][0-9.]*[)]?$)"),
    ) -> list:
        for n in operators:
            if re.match(denied_formats, n):
                raise TypeError(
                    f"Negative numbers are not accepted. The negative number you entered was {n}. Please enter positive numbers only."
                )
            else:
                pass
        return operators

    def __format_input__(
        self,
        operators: list,
        accepted_formats: re.Pattern = re.compile(r"(^[0|[.(-]|[0-9.]*[)]?$)"),
    ):
        """Default accepted_formats pattern includes all positive and negative numbers.
        It also permits parentheses, minus signs, and decimal periods."""
        formatted_operators = [
            int(n) if re.match(accepted_formats, n) else int(0) for n in operators
        ]
        return formatted_operators

    def __get_math_function_arguments__(self) -> list:
        arguments = input(
            """Please enter two numbers, separated by a comma.\nInvalid values will be converted to 0.\n"""
        )
        return arguments

    def addition(self, formatted_operators: list) -> int:
        result = sum(formatted_operators)
        printable_operation = (
            f"{' + '.join([str(number) for number in formatted_operators])} = "
        )
        print(f"{printable_operation}{result}")
        return result

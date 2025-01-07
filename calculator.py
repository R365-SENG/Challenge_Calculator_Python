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

    # Separator is a protected keyword in Python, added"_string."
    def check_for_separator(self, arguments: str, separator_string: str = ",") -> list:
        arguments = arguments.strip(" ")
        if not separator_string in arguments:
            raise TypeError(
                f'Please make sure you separate number input with the separator " {separator_string} ".'
            )
        operators = arguments.split(separator_string)
        return operators

    def check_exact_quantity(self, operators: list, quantity: int = 2) -> list:
        if len(operators) != quantity:
            raise TypeError(f"Please make sure you input {quantity} numbers.")
        return operators

    def check_minimum_quantity(self, operators: list, quantity: int = 2):
        if len(operators) < quantity:
            raise self.QuantityError
        return operators

    def __format_input__(
        self,
        operators: list,
        accepted_formats: re.Pattern = re.compile(r"(^[0|[.(-]|[0-9.]*[)]?$)"),
    ):
        """Default accepted_formats pattern includes all positive and negative numbers.
        It also permits parentheses, minus signs, and decimal periods."""
        formatted_operators = [
            float(n) if re.match(accepted_formats, n) else float(0) for n in operators
        ]
        return formatted_operators

    def __get_math_function_arguments__(self) -> list:
        arguments = input(
            """Please enter two numbers, separated by a comma.\nInvalid values will be converted to 0.\n"""
        )
        return arguments

    def addition(self, formatted_operators: list) -> float:
        result = sum(formatted_operators)
        printable_operation = (
            f"{' + '.join([str(number) for number in formatted_operators])} = "
        )
        print(f"{printable_operation}{result}")
        return result

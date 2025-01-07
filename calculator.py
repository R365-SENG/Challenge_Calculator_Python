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
        self.QuantityError = TypeError(
            "Please limit your input to two numbers, separated by a comma."
        )
        self.SeparatorError = TypeError(
            "Please make sure you separate number inputs with a comma."
        )
        self.arguments = self.__get_math_function_arguments__()

    def check_for_separator(self, arguments: str, separator: str = ",") -> list:
        arguments = arguments.strip(" ")
        if not separator in arguments:
            raise self.SeparatorError
        operators = arguments.split(separator)
        return operators

    def check_arg_quantity(self, operators: list, quantity: int = 2) -> list:
        if len(operators) != quantity:
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

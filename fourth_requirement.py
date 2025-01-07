import re
from calculator import Calculator


class Four(Calculator):
    def __init__(self):
        super().__init__()

    def fourth(self):

        arguments = self.arguments

        separated_args = self.check_for_separator(
            arguments=arguments, separator_strings=[",", "\\n", r"\n"]
        )
        positive_operators = self.deny_negative_inputs(operators=separated_args)
        quantity_args = self.check_minimum_quantity(operators=positive_operators)

        operators = self.__format_input__(
            operators=quantity_args,
        )

        result = self.addition(formatted_operators=operators)
        return result


if __name__ == "__main__":
    Completed = Four()
    Completed.fourth()

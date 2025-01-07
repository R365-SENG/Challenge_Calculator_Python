from calculator import Calculator


class Five(Calculator):
    def __init__(self):
        super().__init__()

    def fifth(self):

        arguments = self.arguments

        separated_args = self.check_for_separator(
            arguments=arguments, separator_strings=[",", "\\n", r"\n"]
        )
        positive_operators = self.deny_negative_inputs(operators=separated_args)
        quantity_checked_operators = self.check_minimum_quantity(
            operators=positive_operators
        )

        formatted_operators = self.__format_input__(
            operators=quantity_checked_operators,
        )
        length_limited_operators = self.deny_large_numbers(
            operators=formatted_operators
        )
        result = self.addition(formatted_operators=length_limited_operators)
        return result


if __name__ == "__main__":
    Completed = Five()
    Completed.fifth()

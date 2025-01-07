from calculator import Calculator


class Three(Calculator):
    def __init__(self):
        super().__init__()

    def third(self):
        arguments = self.arguments
        separated_args = self.check_for_separator(
            arguments=arguments, separator_strings=[",", "\\n"]
        )
        quantity_args = self.check_minimum_quantity(operators=separated_args)
        operators = self.__format_input__(operators=quantity_args)
        result = self.addition(formatted_operators=operators)
        return result


if __name__ == "__main__":
    Completed = Three()
    Completed.third()

from calculator import Calculator


class Six(Calculator):
    def __init__(self):
        super().__init__()

    # Separator is a protected keyword in Python. Default separator is a comma.
    def parse_one_custom_separator(self, arguments: str):
        custom_separators = [",", "\\n", r"\n"]
        if r"//" in arguments and r"\n" in arguments:
            separators = arguments.partition(r"\n")
            arguments = "".join(list(separators[2:]))
            separator = separators[0].lstrip("//")
            custom_separators.append(separator)
        else:
            pass
        return (arguments, custom_separators)

    def sixth(self):
        arguments = self.arguments
        parsed_arguments, custom_separators = self.parse_one_custom_separator(
            arguments=arguments
        )
        seperated_arguments = self.check_for_separator(
            arguments=parsed_arguments, separator_strings=custom_separators
        )
        positive_operators = self.deny_negative_inputs(operators=seperated_arguments)
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
    Completed = Six()
    Completed.sixth()

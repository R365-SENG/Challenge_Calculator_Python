from calculator import Calculator


class Two(Calculator):
    def __init__(self):
        super().__init__()

    def second(self):
        arguments = self.arguments
        separated_args = self.check_for_separator(arguments=arguments)
        quantity_args = self.check_minimum_quantity(operators=separated_args)
        operators = self.__format_input__(operators=quantity_args)
        result = self.addition(formatted_operators=operators)
        return result


if __name__ == "__main__":
    Completed = Two()
    Completed.first()

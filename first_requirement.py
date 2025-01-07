from calculator import Calculator


class One(Calculator):
    def __init__(self):
        super().__init__()

    def first(self):
        arguments = self.arguments
        separated_args = self.check_for_separator(arguments=arguments)
        quantity_args = self.check_exact_quantity(operators=separated_args)
        operators = self.__format_input__(operators=quantity_args)
        result = self.addition(formatted_operators=operators)
        return result


if __name__ == "__main__":
    Completed = One()
    Completed.first()

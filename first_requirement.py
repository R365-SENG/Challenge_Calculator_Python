from calculator import Calculator


class Requirements(Calculator):
    def __init__(self):
        super().__init__()

    def first(self):
        arguments = self.arguments
        separated_args = self.check_for_separator(arguments=arguments)
        quantity_args = self.check_arg_quantity(operators=separated_args)
        operators = self.__format_input__(operators=quantity_args)
        result = self.addition(formatted_operators=operators)


Completed = Requirements()
Completed.first()

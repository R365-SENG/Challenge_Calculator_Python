from calculator import Calculator


class Requirements(Calculator):
    def __init__(self):
        super().__init__()

    def second(self):
        arguments = self.arguments
        separated_args = self.check_for_separator(arguments=arguments)
        operators = self.__format_input__(operators=separated_args)
        result = self.addition(formatted_operators=operators)


Completed = Requirements()
Completed.second()

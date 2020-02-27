class Interpreter:
    def eval(self, expression):
        if type(expression) == list:
            raise NotImplementedError
        elif type(expression) == int:
            return expression
        elif type(expression) == str:
            return expression

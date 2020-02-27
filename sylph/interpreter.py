class Interpreter:
    KEYWORDS = ["+", "-", "*"]

    def eval_keyword(self, keyword):
        if keyword == "+":
            def sum(rand1, rand2):
                return rand1 + rand2
            return sum
        elif keyword == "-":
            def sub(rand1, rand2):
                return rand1 - rand2

            return sub
        elif keyword == "*":
            def product(rand1, rand2):
                return rand1 * rand2
            return product

    def eval(self, expression):
        if type(expression) == list:
            operator = expression[0]
            operands = expression[1:]
            evaled_operands = [self.eval(operand) for operand in operands]
            evaled_operator = self.eval(operator)
            return evaled_operator(*evaled_operands)
        elif type(expression) == int:
            return expression
        elif type(expression) == str:
            if expression in self.KEYWORDS:
                return self.eval_keyword(expression)
            else:
                return expression

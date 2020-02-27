import copy


class NoSuchVariableException(BaseException):
    pass


class Environment:
    def extend(self, var, value):
        raise NotImplementedError

    def lookup(self, var):
        raise NotImplementedError


class DictEnvironment(Environment):
    def __init__(self, initial_state=None):
        if initial_state:
            self.env = copy.copy(initial_state)
        else:
            self.env = {}

    def extend(self, var, value):
        copied_env = copy.copy(self.env)
        copied_env[var] = value
        return DictEnvironment(copied_env)

    def lookup(self, var):
        if var in self.env:
            return self.env[var]
        else:
            raise NoSuchVariableException("No such variable: '{}' (env: {})".format(var, self.env))


class Interpreter:
    BUILTIN_FNS = ["+", "-", "*"]
    KEYWORDS = ["lambda"]

    def lookup(self, env, var):
        if var in env:
            return self.env[var]
        else:
            raise NoSuchVariableException

    def eval_lambda(self, operands, env):
        assert len(operands) == 2
        params = operands[0]
        body = operands[1]
        assert type(params) == list
        assert len(params) == 1
        param = params[0]

        def fn(arg):
            extended_env = env.extend(param, arg)
            return self.eval(body, extended_env)
        return fn

    def eval_keyword(self, keyword, operands, env):
        if keyword == "lambda":
            return self.eval_lambda(operands, env)

    def eval_builtin(self, builtin):
        if builtin == "+":
            def sum(rand1, rand2):
                return rand1 + rand2
            return sum
        elif builtin == "-":
            def sub(rand1, rand2):
                return rand1 - rand2

            return sub
        elif builtin == "*":
            def product(rand1, rand2):
                return rand1 * rand2
            return product

    def eval(self, expression, env=None):
        if env is None:
            env = DictEnvironment()

        if type(expression) == list:
            operator = expression[0]
            operands = expression[1:]
            if operator in self.KEYWORDS:
                return self.eval_keyword(operator, operands, env)
            else:
                evaled_operands = [self.eval(operand, env) for operand in operands]
                evaled_operator = self.eval(operator, env)
                return evaled_operator(*evaled_operands)
        elif type(expression) == int:
            return expression
        elif type(expression) == str:
            if expression in self.BUILTIN_FNS:
                return self.eval_builtin(expression)
            else:
                return env.lookup(expression)

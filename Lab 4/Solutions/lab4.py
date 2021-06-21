class Equation:
    def __init__(self, equation):
        self.equation = equation + " "
        self.operators = []
        self.values = []
        self.priority = False
        self.error = False

    def interpret_operator(self, value1, value2):
        def helper(operator):
            return {
                '+': value1 + value2,
                '-': value1 - value2,
                '*': value1 * value2,
                '/': value1 / value2
            }.get(operator)
        if self.priority:
            return helper(self.operators.pop())
        else:
            return helper(self.operators.pop(0))

    def add_or_subtract(self):
        while self.operators:
            self.values.insert(0, self.interpret_operator(self.values.pop(0), self.values.pop(0)))

    def interpret(self):
        last_char = True  # false - liczba, true - operator
        num_buffer = ""
        for char in self.equation:
            if char.isdigit() or char == '.':
                if not last_char:
                    self.error = True
                    break
                num_buffer += char

            elif char == ' ':
                if num_buffer:
                    if self.priority:
                        self.values.append(self.interpret_operator(self.values.pop(), float(num_buffer)))
                        self.priority = False
                    else:
                        self.values.append(float(num_buffer))
                    num_buffer = ""
                    last_char = False

            elif char == '*' or char == '/':
                if last_char or not self.values:
                    self.error = True
                    break
                self.priority = True
                self.operators.append(char)
                last_char = True

            elif char == '+' or char == '-':
                if last_char or not self.values:
                    self.error = True
                    break
                self.operators.append(char)
                last_char = True

            else:
                self.error = True
                break

        if self.error:
            self.values.clear()
        self.add_or_subtract()
        if len(self.values) != 1:
            print("Error")
        print(self.values[0])


if __name__ == '__main__':
    equation = Equation(input("podaj rownanie:"))
    equation.interpret()

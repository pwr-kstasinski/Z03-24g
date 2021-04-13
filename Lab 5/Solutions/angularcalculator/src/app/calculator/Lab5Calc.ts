import {CalcDefinition, Operator} from './CalcDefinition';

export class Lab5Calc extends CalcDefinition {
  constructor() {
    const availableInfixOperators: string[] = ['+', '-', '*', '/', '^', '%'];
    const availablePrefixOperators: string[] = ['sqrt', 'abs', 'log'];
    const availablePostfixOperators: string[] = ['!'];
    const convertableOutfixOperators: [string, string][] = [['|', '|']];
    const outfixToPrefixMappings: Map<[string, string], string> = new Map<[string, string], string>().set(['|', '|'], 'abs');
    const acceptableLeftBrackets: string[] = ['(', '{', '['];
    const acceptableRightBrackets: string[] = [')', '}', ']'];

    const operatorsPriorities: Map<string, number> = new Map<string, number>();
    for (const postfixOperator of availablePostfixOperators)
    {
      operatorsPriorities.set(postfixOperator, 5);
    }
    for (const prefixOperator of availablePrefixOperators)
    {
      operatorsPriorities.set(prefixOperator, 4);
    }
    operatorsPriorities.set('^', 3);
    operatorsPriorities.set('*', 2);
    operatorsPriorities.set('/', 2);
    operatorsPriorities.set('%', 2);
    operatorsPriorities.set('+', 1);
    operatorsPriorities.set('-', 1);

    super(availableInfixOperators,
          availablePrefixOperators,
          availablePostfixOperators,
          convertableOutfixOperators,
          outfixToPrefixMappings,
          operatorsPriorities,
          acceptableLeftBrackets,
          acceptableRightBrackets);
  }

  makeOperator(symbol: string): Operator {
    switch (symbol) {
      case '+':
        return new class extends Operator {
          constructor() {
            super(Operator.DOUBLE_OPERAND_OPERATOR, symbol);
          }
          safeCalculate(operands: number[]): number {
            return operands[0] + operands[1];
          }
        }();
      case '-':
        return new class extends Operator {
          constructor() {
            super(Operator.DOUBLE_OPERAND_OPERATOR, symbol);
          }
          safeCalculate(operands: number[]): number {
            return operands[0] - operands[1];
          }
        }();
      case '*':
        return new class extends Operator {
          constructor() {
            super(Operator.DOUBLE_OPERAND_OPERATOR, symbol);
          }
          safeCalculate(operands: number[]): number {
            return operands[0] * operands[1];
          }
        }();
      case '/':
        return new class extends Operator {
          constructor() {
            super(Operator.DOUBLE_OPERAND_OPERATOR, symbol);
          }
          safeCalculate(operands: number[]): number {
            if (operands[1] === 0) {
              throw new Error('Cannot divide by zero!');
            }
            return operands[0] / operands[1];
          }
        }();
      case '%':
        return new class extends Operator {
          constructor() {
            super(Operator.DOUBLE_OPERAND_OPERATOR, symbol);
          }
          safeCalculate(operands: number[]): number {
            if (operands[1] === 0) {
              throw new Error('Cannot divide by zero!');
            }
            return operands[0] % operands[1];
          }
        }();
      case '^':
        return new class extends Operator {
          constructor() {
            super(Operator.DOUBLE_OPERAND_OPERATOR, symbol);
          }
          safeCalculate(operands: number[]): number {
            return Math.pow(operands[0], operands[1]);
          }
        }();
      case '!':
        return new class extends Operator {
          constructor() {
            super(Operator.SINGLE_OPERAND_OPERATOR, symbol);
          }
          safeCalculate(operands: number[]): number {
            let operand = operands[0];
            if (operand < 0) {
              throw new Error('Cannot calculate factorial of a negative number!');
            }
            let result = 1;
            while (operand > 1) {
              result *= operand--;
            }
            return result;
          }
        }();
      case 'sqrt':
        return new class extends Operator {
          constructor() {
            super(Operator.SINGLE_OPERAND_OPERATOR, symbol);
          }
          safeCalculate(operands: number[]): number {
            const operand = operands[0];
            if (operand < 0) {
              throw new Error('Cannot calculate square root of a negative number!');
            }
            return Math.sqrt(operand);
          }
        }();
      case 'abs':
        return new class extends Operator {
          constructor() {
            super(Operator.SINGLE_OPERAND_OPERATOR, symbol);
          }
          safeCalculate(operands: number[]): number {
            return Math.abs(operands[0]);
          }
        }();
      case 'log':
        return new class extends Operator {
          constructor() {
            super(Operator.SINGLE_OPERAND_OPERATOR, symbol);
          }
          safeCalculate(operands: number[]): number {
            const operand = operands[0];
            if (operand <= 0) {
              throw new Error('Cannot calculate logarithm of a non-positive number!');
            }
            return Math.log10(operand);
          }
        }();
      default:
        return new class extends Operator {
          constructor() {
            super(Operator.VALUE, symbol);
          }
          safeCalculate(operands: number[]): number {
            if (isNaN(parseFloat(symbol)) || symbol.search('=') !== -1) {
              throw new Error('Invalid expression: ' + symbol);
            }
            return Number(symbol);
          }
        }();
    }
  }

}

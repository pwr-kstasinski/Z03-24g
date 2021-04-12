import { Stack } from './Stack';

export class RpnConverter {
  private static leftBrackets: string[] = ['(', '[', '{'];
  private static rightBrackets: string[] = [')', ']', '}'];
  private static allOperands: string[] = ['+', '-', '*', '/', '%', '^'];

  private static addSpaces(normal: string): string {
    let output = '';
    // tslint:disable-next-line:prefer-for-of
    for (let i = 0; i < normal.length; i++)
    {
      if (this.leftBrackets.includes(normal[i]) || this.rightBrackets.includes(normal[i]) || this.allOperands.includes(normal[i]))
      {
        output += ' ';
        output += normal[i];
        output += ' ';
      }
      else
      {
        output += normal[i];
      }
    }
    return output;
  }

  private static priority(ch: string): number {
    switch (ch) {
      case '+':
      case '-':
        return 1;
      case '*':
      case '/':
      case '%':
        return 2;
      case '^':
        return 3;
    }
    return -1;
  }

  private static analyze(normal: string[]): Array<string> {
    const operands: Stack<string> = new Stack<string>();
    const rpn: Array<string> = new Array<string>();


    // tslint:disable-next-line:prefer-for-of
    for (let offset = 0; offset < normal.length; offset++)
    {
      /*przetwarzanie warunkowe*/
      const actualString = normal[offset];

      const actualNumber = parseFloat(actualString);
      if (!isNaN(actualNumber))
      {
        rpn.push(actualNumber.toString());
        console.log('   [NUMBER] ' + actualNumber);
      }
      else
      {
        if (this.leftBrackets.includes(actualString))
        {
          console.log('   [LEFT BRACKET] ' + actualString);
          operands.push('(');
        }
        else if (this.rightBrackets.includes(actualString))
        {
          console.log('   [RIGHT BRACKET] ' + actualString);
          while (!(operands.peek() === '('))
          {
            rpn.push(operands.pop());
          }
          operands.pop();
        }
        else if (this.allOperands.includes((actualString)))
        {

          console.log('   [OPERAND BRACKET] ' + actualString);
          while (!operands.empty() && this.priority(actualString) <= this.priority(operands.peek())) {
            rpn.push(operands.pop());
          }
          operands.push(actualString);
        } else if (actualString === '') {

        } else {
          throw new Error('Invalid format of expression!' + actualString);
        }
      }
      console.log('   NUMBER_OF_OPERANDS: ' + operands.size());
      console.log('   RPN: ' + rpn);
    }
    while (!operands.empty()) {
      rpn.push(operands.pop());
    }
    return rpn;

  }

  public static toRpn(normal: string): Array<string> {
    console.log('converting to rpn...');
    console.log('normal: ' + normal);
    const sanitizedNormal = this.addSpaces(normal);
    console.log('sanitized: ' + sanitizedNormal);
    const splittedNormal = sanitizedNormal.split(' ');
    console.log('splitted: ' + splittedNormal);
    const rpn: Array<string> = this.analyze(splittedNormal);
    console.log('rpn format: ' + rpn);
    return rpn;

  }
}

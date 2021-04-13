import { TreeNode} from './TreeNode';
import { Stack } from './Stack';
import {CalcDefinition, Operator} from './CalcDefinition';


export class ExpressionService {
  private calcLogic: CalcDefinition;
  private normalForm = '';
  private rpnForm: Array<string> = [''];
  private treeForm: ExpressionTree;

  constructor(calcLogic: CalcDefinition) {
    this.calcLogic = calcLogic;
  }

  public getRpnForm(): Array<string> {
    return this.rpnForm;
  }

  public updateNormalForm(normalForm: string): void {
    this.normalForm = normalForm;
    this.normalToRpn();
    this.rpnToTree();
  }

  private normalToRpn(): void {
    console.log('converting to rpn...');
    console.log('normal: ' + this.normalForm);
    this.normalForm = this.sanitizeNormal(this.normalForm);
    console.log('sanitized: ' + this.normalForm);
    const splittedNormal = this.normalForm.split(' ');
    console.log('splitted: ' + splittedNormal);
    const rpn: Array<string> = this.splittedNormalToRpn(splittedNormal);
    console.log('rpn format: ' + rpn);
    this.rpnForm = rpn;

  }

  private sanitizeNormal(normal: string): string {
    // TODO: OUTFIX TO PREFIX SANITIZING
    let output = '';
    // tslint:disable-next-line:prefer-for-of
    for (let i = 0; i < normal.length; i++)
    {
      const symbol = normal[i];
      if (this.calcLogic.isAcceptableLeftBracket(symbol)) {
        output += ' ';
        output += '(';
        output += ' ';
      }
      else if (this.calcLogic.isAcceptableRightBracket(symbol)) {
        output += ' ';
        output += ')';
        output += ' ';
      }
      else if (this.calcLogic.isAvailableOperator(symbol)) {
        output += ' ';
        output += symbol;
        output += ' ';
      }
      else
      {
        output += normal[i];
      }
    }
    return output;
  }

  private splittedNormalToRpn(normal: string[]): Array<string> {
    const operands: Stack<string> = new Stack<string>();
    const rpn: Array<string> = new Array<string>();


    // tslint:disable-next-line:prefer-for-of
    for (let offset = 0; offset < normal.length; offset++)
    {
      /*przetwarzanie warunkowe*/
      const actualString = normal[offset];

      const actualNumber = parseFloat(actualString);
      if (!isNaN(actualNumber)) {
        rpn.push(actualNumber.toString());
      }
      else {
        if (this.calcLogic.isAcceptableLeftBracket(actualString)) {
          operands.push('(');
        }
        else if (this.calcLogic.isAcceptableRightBracket(actualString)) {
          while (!(this.calcLogic.isAcceptableLeftBracket(operands.peek())))
          {
            console.log('   POP AND PUSH: ' + operands.peek());
            rpn.push(operands.pop());
          }
          console.log('   POP: ' + operands.peek());
          operands.pop();
        }
        else if (this.calcLogic.isAvailablePostfixOperator(actualString)) {
          rpn.push(actualString);
        }
        else if (this.calcLogic.isAvailableOperator(actualString)) {
          while (!operands.empty()
              && !this.calcLogic.isAcceptableLeftBracket(operands.peek())
              && this.calcLogic.getPriorityOfOperator(actualString) <= this.calcLogic.getPriorityOfOperator(operands.peek())) {
            rpn.push(operands.pop());
          }
          operands.push(actualString);
        } else if (actualString === '') {

        } else {
          throw new Error('Invalid format of expression! Unknown symbol: ' + actualString + '.');
        }
      }
    }
    while (!operands.empty()) {
      rpn.push(operands.pop());
    }
    return rpn;
  }

  private rpnToTree(): void {
    this.treeForm = new ExpressionTree(this.rpnForm, this.calcLogic);
  }

  public evaluate(): number {
    return this.treeForm.calculate();
  }

}

class ExpressionTree {
  private root: TreeNode<Operator>;
  private calcLogic: CalcDefinition;

  /*  private jsonNodes: string[];
    private jsonLinks: string[];*/

  public constructor(rpnArgs: Array<string>, calcDefinition: CalcDefinition) {
    this.calcLogic = calcDefinition;
    this.init(rpnArgs);
  }

  public init(rpnArgs: Array<string>): void {
    const waitingNodes: Stack<TreeNode<Operator>> = new Stack<TreeNode<Operator>>();
    let i = 0;
    for (const arg of rpnArgs) {
      const operator = this.calcLogic.makeOperator(arg);
      const nodesForConnect = new Stack<TreeNode<Operator>>();
      for (let j = 0; j < operator.getNumberOfOperandsNeeded(); j++) {
        if (waitingNodes.empty()) {
          throw new Error('Expression is invalid!');
        }
        nodesForConnect.push(waitingNodes.pop());
      }
      const newNode = new TreeNode<Operator>(operator, '0');
      while (!nodesForConnect.empty()) {
        newNode.pushBackChild(nodesForConnect.pop());
      }
      waitingNodes.push(newNode);
    }
    this.root = waitingNodes.peek();
    ++i;
  }

  public calculate(): number {
    return this.calculateRec(this.root);
  }

  private calculateRec(actualNode: TreeNode<Operator>): number {
    const operator = actualNode.getValue();
    if (operator.getNumberOfOperandsNeeded() === Operator.VALUE) {
      return operator.calculate([]);
    } else if (operator.getNumberOfOperandsNeeded() === Operator.SINGLE_OPERAND_OPERATOR) {
      return operator.calculate([
        this.calculateRec(actualNode.getChild(0))
      ]);
    } else if (operator.getNumberOfOperandsNeeded() === Operator.DOUBLE_OPERAND_OPERATOR) {
      return operator.calculate([
        this.calculateRec(actualNode.getChild(0)),
        this.calculateRec(actualNode.getChild(1))
      ]);
    } else {
      throw new Error('Unsupported type of operator - too much operands needed: ' + operator.getNumberOfOperandsNeeded() + '!');
    }
  }
}

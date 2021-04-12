import { BinaryTreeNode} from './BinaryTreeNode';
import { Stack } from './Stack';



export class RpnBinaryTree {
  private static allOperands: string[] = ['+', '-', '*', '/', '%', '^'];

  private root: BinaryTreeNode<string>;


  public constructor(rpnArgs: Array<string>) {
    this.createNewTree(rpnArgs);
  }

  private createNewTree(rpnArgs: Array<string>): void {
    const stack: Stack<BinaryTreeNode<string>> = new Stack<BinaryTreeNode<string>>();
    for (const arg in rpnArgs)
    {
      if (RpnBinaryTree.allOperands.includes(arg))
      {
        const operatorNode: BinaryTreeNode<string> = new BinaryTreeNode<string>(arg);
        if (stack.size() >= 2) {
          operatorNode.setRightSon(stack.pop());
          operatorNode.setLeftSon(stack.pop());
          stack.push(operatorNode);
        }
        else {
          throw new Error('Given rpnArgs are invalid!');
        }
      }
      else
      {
        stack.push(new BinaryTreeNode<string>(arg));
      }
    }
    this.root = stack.peek();
  }

  public calculate(): number {
    return this.calculateRec(this.root);
  }

  private calculateRec(actualNode: BinaryTreeNode<string>): number {
    if (RpnBinaryTree.allOperands.includes(actualNode.getValue())) {
      const leftOperand: number = this.calculateRec(actualNode.getLeftSon());
      const rightOperand: number = this.calculateRec(actualNode.getRightSon());
      const operator: string = actualNode.getValue();
      switch (operator) {
        case '+':
          console.log('calculateRec return: ' + (leftOperand + rightOperand));
          return leftOperand + rightOperand;
        case '-':
          console.log('calculateRec return: ' + (leftOperand - rightOperand));
          return leftOperand - rightOperand;
        case '*':
          console.log('calculateRec return: ' + (leftOperand * rightOperand));
          return leftOperand * rightOperand;
        case '/':
          console.log('calculateRec return: ' + (leftOperand / rightOperand));
          return leftOperand / rightOperand;
        case '%':
          console.log('calculateRec return: ' + (leftOperand % rightOperand));
          return leftOperand % rightOperand;
      }
    } else {
      console.log('calculateRec return: ' + Number(actualNode.getValue()));
      return Number(actualNode.getValue());
    }
    throw new Error('Exception while calculating RPN!');
  }

}

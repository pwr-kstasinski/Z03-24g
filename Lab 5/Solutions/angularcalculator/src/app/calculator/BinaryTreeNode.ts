export class BinaryTreeNode<E> {
  private value: E;
  private leftSon: BinaryTreeNode<E>;
  private rightSon: BinaryTreeNode<E>;
  private father: BinaryTreeNode<E>;

  public constructor(value: E) {
    this.value = value;
  }

  public getValue(): E {
    return this.value;
  }

  public setValue(value: E): void {
  this.value = value;
  }

  public getLeftSon(): BinaryTreeNode<E> {
    return this.leftSon;
  }

  public setLeftSon(leftSon: BinaryTreeNode<E>): void {
    this.leftSon = leftSon;
  }

  public hasLeftSon(): boolean {
    return this.leftSon != null;
  }

  public getRightSon(): BinaryTreeNode<E> {
    return this.rightSon;
  }

  public setRightSon(rightSon: BinaryTreeNode<E>): void {
    this.rightSon = rightSon;
  }

  public hasRightSon(): boolean {
    return this.rightSon != null;
  }

  public setFather(father: BinaryTreeNode<E>): void {
    this.father = father;
  }
}

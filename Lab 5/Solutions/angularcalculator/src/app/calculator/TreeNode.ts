export class TreeNode<E> {
  private readonly id: string;
  private value: E;
  private children: TreeNode<E>[] = [];
  private father: TreeNode<E>;

  public constructor(value: E, id: string) {
    this.value = value;
    this.id = id;
  }

  public getId(): string {
    return this.id;
  }

  public getValue(): E {
    return this.value;
  }

  public setValue(value: E): void {
  this.value = value;
  }

  public setFather(father: TreeNode<E>): void {
    this.father = father;
  }

  public pushBackChild(child: TreeNode<E>): void {
    this.children.push(child);
  }

  public getNumberOfChildren(): number {
    return this.children.length;
  }

  public getChild(childNr: number): TreeNode<E> {
    if (childNr < 0 || childNr >= this.getNumberOfChildren()) {
      throw new Error('Child at index ' + childNr + ' in [' + this.id + '] ' + this.value + 'doesn\'t exist!');
    }
    return this.children[childNr];
  }
}

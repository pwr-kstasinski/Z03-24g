export class Stack<T> {
  private store: T[] = [];
  push(val: T): void {
    this.store.push(val);
  }
  pop(): T | undefined {
    return this.store.pop();
  }
  peek(): T | undefined {
    const temp = this.store.pop();
    this.store.push(temp);
    return temp;
  }
  empty(): boolean {
    return ((this.store.length) === 0);
  }
  size(): number {
    return this.store.length;
  }
}

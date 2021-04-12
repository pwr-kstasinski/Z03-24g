import { Component, OnInit } from '@angular/core';
import { RpnConverter } from './rpnconverter';
import { RpnBinaryTree } from './RpnBinaryTree';

@Component({
  selector: 'app-calculator',
  templateUrl: './calculator.component.html',
  styleUrls: ['./calculator.component.css']
})
export class CalculatorComponent implements OnInit {

  display = '';
  rpn: Array<string> = new Array<string>('Oczekiwanie na wykonywanie działania...');
  rpnBinaryTree: RpnBinaryTree = null;
  result: number = null;

  constructor() { }

  ngOnInit(): void {
  }

  digit(num: number): void {
    this.display += num.toString();
  }

  comma(): void {
    this.display += '.';
  }

  bracket(opening: boolean): void {
    if (opening)
    {
      this.display += '(';
    }
    else
    {
      this.display += ')';
    }
  }

  infix_operator(operator: string): void {
    this.display += operator;
  }

  clear(): void {
    this.display = '';
  }

  backspace(): void {
    this.display = this.display.slice(0, -1);
  }

  perform(): void {
    this.rpn = RpnConverter.toRpn(this.display);
    this.rpnBinaryTree = new RpnBinaryTree(this.rpn);
    this.result = this.rpnBinaryTree.calculate();
  }

}

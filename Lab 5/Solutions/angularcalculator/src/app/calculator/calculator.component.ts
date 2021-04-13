import { Component, OnInit } from '@angular/core';
import { ExpressionService } from './ExpressionService';
import { Lab5Calc } from './Lab5Calc';

@Component({
  selector: 'app-calculator',
  templateUrl: './calculator.component.html',
  styleUrls: ['./calculator.component.css']
})
export class CalculatorComponent implements OnInit {

  display = '';
  rpn: Array<string> = new Array<string>('Oczekiwanie na wykonywanie działania...');
  result: number = null;
  graphNodesJsons: string[] = null;
  graphLinksJsons: string[] = null;
  graphCustomColorsJsons: string[] = null;

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
    const expressionService = new ExpressionService(new Lab5Calc());
    expressionService.updateNormalForm(this.display);
    this.rpn = expressionService.getRpnForm();
    this.result = expressionService.evaluate();
  }

}

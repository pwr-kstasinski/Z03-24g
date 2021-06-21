import { Component, OnInit } from '@angular/core';
import { ExpressionService } from './ExpressionService';
import { Lab5Calc } from './Lab5Calc';
import {Node} from '@swimlane/ngx-graph/lib/models/node.model';
import {Edge} from '@swimlane/ngx-graph/lib/models/edge.model';

@Component({
  selector: 'app-calculator',
  templateUrl: './calculator.component.html',
  styleUrls: ['./calculator.component.css']
})
export class CalculatorComponent implements OnInit {

  display = '';
  rpn: Array<string> = new Array<string>('Oczekiwanie na wykonywanie działania...');
  result: number = null;
  graphNodesJsons: Node[] = null;
  graphLinksJsons: Edge[] = null;
  expressionService = new ExpressionService(new Lab5Calc());

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

  prefix_operator(operator: string): void {
    this.display += operator;
  }

  postfix_operator(operator: string): void {
    this.display += operator;
  }

  clear(): void {
    this.display = '';
  }

  backspace(): void {
    this.display = this.display.slice(0, -1);
  }

  reciprocal(): void {
    this.display = '1/(' + this.display + ')';
  }

  perform(): void {
    if (this.display.length === 0) {
      this.display = '0';
    }
    try {
      this.expressionService.updateNormalForm(this.display);
      this.rpn = this.expressionService.getRpnForm();
      this.result = this.expressionService.evaluate();
      [this.graphNodesJsons, this.graphLinksJsons] = this.expressionService.getGraph();
    } catch (e) {
      this.rpn = Array<string>('');
      this.result = e.toString();
      this.graphLinksJsons = null;
      this.graphNodesJsons = null;
    }
  }

}

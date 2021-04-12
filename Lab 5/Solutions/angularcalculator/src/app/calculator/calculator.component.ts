import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-calculator',
  templateUrl: './calculator.component.html',
  styleUrls: ['./calculator.component.css']
})
export class CalculatorComponent implements OnInit {

  display = '';
  output = '';

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

  calculate(): void {
    this.output = 'Calculating!';
  }
}

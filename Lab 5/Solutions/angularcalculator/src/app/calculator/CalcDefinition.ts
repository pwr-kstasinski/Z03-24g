export abstract class Operator {
  public static readonly VALUE = 0;
  public static readonly SINGLE_OPERAND_OPERATOR = 1;
  public static readonly DOUBLE_OPERAND_OPERATOR = 2;
  private readonly numberOfOperandsNeeded: number;
  private readonly symbol: string;

  protected constructor(numberOfOperandsNeeded: number, symbol: string) {
    this.numberOfOperandsNeeded = numberOfOperandsNeeded;
    this.symbol = symbol;
  }

  public getNumberOfOperandsNeeded(): number {
    return this.numberOfOperandsNeeded;
  }
  public getSymbol(): string {
    return this.symbol;
  }

  protected abstract safeCalculate(operands: number[]): number;
  private checkNumberOfOperands(numberOfOperands: number): void {
    if (numberOfOperands !== this.getNumberOfOperandsNeeded()) {
      throw new Error('Incorrect quantity of operands for ' + this.getSymbol() + ' operator! ' +
        'Given ' + numberOfOperands + ', expected ' + this.getNumberOfOperandsNeeded() + '.');
    }
  }

  public readonly calculate = (operands: number[]): number => {
    this.checkNumberOfOperands(operands.length);
    return this.safeCalculate(operands);
  }

}

export abstract class CalcDefinition {
  private readonly availableInfixOperators: string[];
  private readonly availablePrefixOperators: string[];
  private readonly availablePostfixOperators: string[];
  private readonly convertableOutfixOperators: [string, string][];
  private readonly outfixToPrefixMappings: Map<[string, string], string>;
  private readonly operatorsPriorities: Map<string, number>;
  private readonly acceptableLeftBrackets: string[];
  private readonly acceptableRightBrackets: string[];

  protected constructor(availableInfixOperators: string[],
                        availablePrefixOperators: string[],
                        availablePostfixOperators: string[],
                        convertableOutfixOperators: [string, string][],
                        outfixToPrefixMappings: Map<[string, string], string>,
                        operatorsPriorities: Map<string, number>,
                        acceptableLeftBrackets: string[],
                        acceptableRightBrackets: string[]) {
    this.availableInfixOperators = availableInfixOperators;
    this.availablePrefixOperators = availablePrefixOperators;
    this.availablePostfixOperators = availablePostfixOperators;
    this.convertableOutfixOperators = convertableOutfixOperators;
    this.outfixToPrefixMappings = outfixToPrefixMappings;
    this.operatorsPriorities = operatorsPriorities;
    this.acceptableLeftBrackets = acceptableLeftBrackets;
    this.acceptableRightBrackets = acceptableRightBrackets;
  }

  public isAvailableInfixOperator(symbol: string): boolean {
    return this.availableInfixOperators.includes(symbol);
  }
  public isAvailablePrefixOperator(symbol: string): boolean {
    return this.availablePrefixOperators.includes(symbol);
  }
  public isAvailablePostfixOperator(symbol: string): boolean {
    return this.availablePostfixOperators.includes(symbol);
  }
  public isAvailableOperator(symbol: string): boolean {
    return this.isAvailableInfixOperator(symbol) || this.isAvailablePrefixOperator(symbol) || this.isAvailablePostfixOperator(symbol);
  }
  public getConvertableOutfixOperators(): [string, string][] {
    return this.convertableOutfixOperators;
  }
  public getOutfixToPrefixMapping(outfixSymbols: [string, string]): string {
    if (!this.outfixToPrefixMappings.has(outfixSymbols)) {
      throw new Error('Outfix "' + outfixSymbols + '" operators are not supported by this calculator definition!');
    }
    return this.outfixToPrefixMappings.get(outfixSymbols);
  }
  public getPriorityOfOperator(symbol: string): number {
    if (!this.operatorsPriorities.has(symbol)) {
      console.log('trying to get... ' + this.operatorsPriorities.get(symbol));
      throw new Error('There is no "' + symbol + '" operator in calculator\'s definition priorities of operators!');
    }
    return this.operatorsPriorities.get(symbol);
  }
  public isAcceptableLeftBracket(symbol: string): boolean {
    return this.acceptableLeftBrackets.includes(symbol);
  }
  public isAcceptableRightBracket(symbol: string): boolean {
    return this.acceptableRightBrackets.includes(symbol);
  }

//  public abstract calculate(operator: Operator, operands: number[]): number;
  public abstract makeOperator(name: string): Operator;
}

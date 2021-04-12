from sya import parse, OPDICT
def test(exp):
    print(exp)
    t1 = parse(exp)
    print(t1.evalAST(OPDICT))
    t1.display()
test('1 + 2')
test('(5+2.1)*10.2')
test('1.1 + 2')
test('(3 * (1 + 2))')
test('5.1 / 6')
test('0.85 * .15 + 3.14 - 2')
test('1 + 2 * 3 - 4 / 5 + 6 * 7 - 8 / 9 + 10')
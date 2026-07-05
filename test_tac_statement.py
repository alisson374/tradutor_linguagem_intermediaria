import pytest
from tac import Tac

class TestTacStatement:
  def test_if_statement_should_generate_correct_tac(self):
    #var int cont, a, cont2;
    # if (cont < 5) {
    #   a = a + cont2;
    # }

    ast = [
      ('declaration', [('int', [('var', 'cont'), ('var', 'a'), ('var', 'cont2')])]),
      ('if', ('relop', '<', ('id', 'cont'), ('num', 5)), [('assign', ('id', 'a'), ('binop', '+', ('id', 'a'), ('id', 'cont2')))])
    ]

    expected_tac = [
      'IF cont >= 5 GOTO END1',
      'T1 = a + cont2',
      'a = T1',
      'END1:',
    ]

    tac = Tac()
    generated_tac = tac.generateTac(ast)

    assert generated_tac == expected_tac, f"Expected {expected_tac}, but got {generated_tac}"

  def test_while_statement_should_generate_correct_tac(self):
    # var int cont;
    # cont = 0;
    # while (cont < 10) {
    #   cont = cont + 1;
    # }

    ast = [
      ('declaration', [('int', [('var', 'cont')])]),
      ('assign', ('id', 'cont'), ('num', 0)),
      ('while', ('relop', '<', ('id', 'cont'), ('num', 10)), 
       [('assign', ('id', 'cont'), ('binop', '+', ('id', 'cont'), ('num', 1)))])
    ]

    expected_tac = [
      'cont = 0',
      'WHILE1:',
      '\tIF cont >= 10 GOTO END2',
      '\tT1 = cont + 1',
      '\tcont = T1',
      '\tGOTO WHILE1',
      'END2:'
    ]

    tac = Tac()
    generated_tac = tac.generateTac(ast)

    assert generated_tac == expected_tac, f"Expected {expected_tac}, but got {generated_tac}"

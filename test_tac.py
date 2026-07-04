from tac import tac

class TestTACGenerator:
  def test_simple_assignment_shoud_paste(self):
    # num = 0;
    
    ast = [
      ('assign', ('id', 'num'), ('num', 0))
    ]

    expected_tac = [
      'num = 0'
    ]

    generated_tac = tac.generateTac(ast)

    assert generated_tac == expected_tac, f"Expected {expected_tac}, but got {generated_tac}"

  def test_if_statement_should_generate_correct_tac(self):
    # if (cont < 5) {
    #   num = num + cont2;
    # }

    ast = [
      ('if', ('relop', '<', ('id', 'cont'), ('num', 5)), [('assign', ('id', 'num'), ('binop', '+', ('id', 'num'), ('id', 'cont2')))])
    ]

    expected_tac = [
      'IF cont >= 5 GOTO END1',
      'T1 = num + cont2',
      'num = T1',
      'END1',
    ]

    generated_tac = tac.generateTac(ast)

    assert generated_tac == expected_tac, f"Expected {expected_tac}, but got {generated_tac}" 

  def test_declaration_variable_should_generate_correct_tac(self):
    # var
    #   int cont;
    
    ast = [
      ('declaration', [('int', ['var', 'cont'])])
    ]


    tac.generateTac(ast)

    assert tac.variables[0] == ('int', ('var', 'cont')), f"Expected ('int', ('var', 'cont')), but got {tac.variables[0]}"
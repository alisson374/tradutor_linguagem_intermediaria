from tac import tac

class TestTACGenerator:
  def test_simple_assignment_shoud_paste(self):
    # Example AST for testing
    ast = [
      ('assign', ('id', 'num'), ('num', 0))
    ]

    expected_tac = [
      'num = 0'
    ]

    generated_tac = tac.generateTac(ast)

    assert generated_tac == expected_tac, f"Expected {expected_tac}, but got {generated_tac}"

  def test_if_statement_should_generate_correct_tac(self):
    # Example AST for testing
    ast = [
      ('if', ('relop', '<', ('id', 'cont'), ('num', 5)), [('assign', ('id', 'num'), ('binop', '+', ('id', 'num'), ('id', 'cont2')))])
    ]

    expected_tac = [
      'IF cont < 5 GOTO L0',
      'num = num + cont2',
      'GOTO L1',
      'L0:',
      'L1:'
    ]

    generated_tac = tac.generateTac(ast)

    assert generated_tac == expected_tac, f"Expected {expected_tac}, but got {generated_tac}" 
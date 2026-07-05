from tac import Tac

class TestTACGeneratorAssign:
  def test_simple_assignment_shoud_paste(self):
    # var int a;
    # a = 0;
    
    ast = [
      ('declaration', [('int', [('var', 'a')])]),
      ('assign', ('id', 'a'), ('num', 0))
    ]

    expected_tac = [
      'a = 0'
    ]
    
    tac = Tac()
    generated_tac = tac.generateTac(ast)

    assert generated_tac == expected_tac, f"Expected {expected_tac}, but got {generated_tac}"

  def test_assign_vector_to_num(self):
    # var int v[8], a;
    # a = v[5];
    
    ast = [
      ('declaration', [('int', [('vector', 'v', ('num', 8)), ('var', 'a')])]),
      ('assign', ('id', 'a'), ('vector_access', 'v', ('num', 5)))
    ]

    expected_tac = [
      'T1 = c(v)',
      'T2 = 5 * largura(v)',
      'T3 = T1[T2]',
      'a = T3'
    ]
    
    tac = Tac()
    generated_tac = tac.generateTac(ast)

    assert generated_tac == expected_tac, f"Expected {expected_tac}, but got {generated_tac}"
  
  def test_assign_num_to_vector(self):
    # var int v[8], a;
    # v[5] = a;
    
    ast = [
      ('declaration', [('int', [('vector', 'v', ('num', 8)), ('var', 'a')])]),
      ('assign', ('vector_access', 'v', ('num', 5)), ('id', 'a'))
    ]

    expected_tac = [
      'T1 = c(v)',
      'T2 = 5 * largura(v)',
      'T1[T2] = a'
    ]
    
    tac = Tac()
    generated_tac = tac.generateTac(ast)

    assert generated_tac == expected_tac, f"Expected {expected_tac}, but got {generated_tac}"
  
  def test_assign_matrix_to_num(self):
    # var int m[2][3], a;
    # a = m[1][2];
    
    ast = [
      ('declaration', [('int', [('matrix', 'm', ('num', 2), ('num', 3)), ('var', 'a')])]),
      ('assign', ('id', 'a'), ('matrix_access', 'm', ('num', 1), ('num', 2)))
    ]

    expected_tac = [
      'T1 = 1 * 3',
      'T1 = T1 + 2',
      'T2 = c(m)',
      'T3 = T1 * largura(m)',
      'T4 = T2[T3]',
      'a = T4'
    ]
    
    tac = Tac()
    generated_tac = tac.generateTac(ast)

    assert generated_tac == expected_tac, f"Expected {expected_tac}, but got {generated_tac}"
  
  def test_assign_num_to_matrix(self):
    # var int m[2][3], a;
    # m[1][2] = a;
    
    ast = [
      ('declaration', [('int', [('matrix', 'm', ('num', 2), ('num', 3)), ('var', 'a')])]),
      ('assign', ('matrix_access', 'm', ('num', 1), ('num', 2)), ('id', 'a'))
    ]

    expected_tac = [
      'T1 = 1 * 3',
      'T1 = T1 + 2',
      'T2 = c(m)',
      'T3 = T1 * largura(m)',
      'T2[T3] = a'
    ]
    
    tac = Tac()
    generated_tac = tac.generateTac(ast)

    assert generated_tac == expected_tac, f"Expected {expected_tac}, but got {generated_tac}"
  
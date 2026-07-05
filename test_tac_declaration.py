import pytest
from tac import Tac

class TestTACGeneratorDeclaration:
  
  @pytest.mark.parametrize(
    "type_var, expected",
    [
      ("int", ('int', ('var', 'cont'))), # var int cont;
      ("char", ('char', ('var', 'cont'))) # var char cont;
    ],
  )
  def test_declaration_simple_variable_should_generate_correct_tac(self, type_var, expected):
    ast = [
      ('declaration', [(type_var, [('var', 'cont')])])
    ]

    tac = Tac()
    tac.generateTac(ast)

    var = tac.variables[0]
    assert var == expected, f"Expected {expected}, but got {var}"
  
  @pytest.mark.parametrize(
    "type_var, expected",
    [
      ('int', ('int', ('vector', 'x', ('num', 8)))), # var int x[8];
      ('char', ('char', ('vector', 'x', ('num', 8)))) # var char x[8];
    ],
  )
  def test_declaration_vector_should_generate_correct_tac(self, type_var, expected):
    # var int cont;
    
    ast = [
      ('declaration', [(type_var, [('vector', 'x', ('num', 8))])])
    ]

    tac = Tac()
    tac.generateTac(ast)

    var = tac.variables[0]
    assert var == expected, f"Expected {expected}, but got {var}"
  
  @pytest.mark.parametrize(
    "type_var, expected",
    [
      ('int', ('int', ('matrix', 'a', ('num', 10), ('num', 2)))), # var inta[10][2];
      ('char', ('char', ('matrix', 'a', ('num', 10), ('num', 2)))) # var char a[10][2];
    ],
  )
  def test_declaration_matrix_should_generate_correct_tac(self, type_var, expected):
    # var int cont;
    
    ast = [
      ('declaration', [(type_var, [('matrix', 'a', ('num', 10), ('num', 2))])])
    ]

    tac = Tac()
    tac.generateTac(ast)

    var = tac.variables[0]
    assert var == expected, f"Expected {expected}, but got {var}"

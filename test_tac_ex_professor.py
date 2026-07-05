from tac import Tac

class TestTacExProfessor:
  def test_exemplo_professor_corrigido(self):
    # var
    # int cont, num;
    # real cont2;
    #
    # num = 0;
    #
    # while(cont < 10) {
    # cont2 = 3.1415 * cont2 ^ 2;
    #   if (cont < 5) {
    #     num = num + cont2;
    #   }
    #   else {
    #     cont = 0;
    #   }
    #     cont = cont + 1;
    # }

    ast = [
      ('declaration', [('int', [('var', 'cont'), ('var', 'num')]), ('real', [('var', 'cont2')])]),
      ('assign', ('id', 'num'), ('num', 0)),
      ('while', ('relop', '<', ('id', 'cont'), ('num', 10)), 
       [('assign', ('id', 'cont2'), ('binop', '*', ('num', 3.1415), ('binop', '^', ('id', 'cont2'), ('num', 2)))), 
        ('ifelse', ('relop', '<', ('id', 'cont'), ('num', 5)), 
         [('assign', ('id', 'num'), ('binop', '+', ('id', 'num'), ('id', 'cont2')))], 
         [('assign', ('id', 'cont'), ('num', 0))]), 
        ('assign', ('id', 'cont'), ('binop', '+', ('id', 'cont'), ('num', 1)))])
    ]

    expected_tac = [
      'num = 0',
      'WHILE1:',
      '\tIF cont >= 10 GOTO END2',
      '\tT1 = cont2 ^ 2',
      '\tT2 = 3.1415 * T1',
      '\tcont2 = T2',
      '\tIF cont >= 5 GOTO ELSE3',
      '\tT3 = num + cont2',
      '\tnum = T3',
      '\tGOTO END4',
      'ELSE3:',
      '\tcont = 0',
      'END4:',
      '\tT4 = cont + 1',
      '\tcont = T4',
      '\tGOTO WHILE1',
      'END2:'
    ]

    tac = Tac()
    generated_tac = tac.generateTac(ast)
    assert generated_tac == expected_tac

  

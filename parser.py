# parser.py

import ply.yacc as yacc
from scanner import tokens

# ==========================================================
# Program
# ==========================================================

def p_program(p):
  'program : statement_list'
  p[0] = ('program', p[1])

# ==========================================================
# Statement list
# ==========================================================

def p_statement_list_single(p):
  'statement_list : statement'
  p[0] = [p[1]]

def p_statement_list_multiple(p):
  'statement_list : statement_list statement'
  p[0] = p[1] + [p[2]]

# ==========================================================
# Statements
# ==========================================================

def p_statement_declaration(p):
  'statement : declaration SEMI'
  p[0] = p[1]

def p_statement_assignment(p):
  'statement : assignment SEMI'
  p[0] = p[1]

def p_statement_while(p):
  'statement : while_stmt'
  p[0] = p[1]

def p_statement_if(p):
  'statement : if_stmt'
  p[0] = p[1]

# ==========================================================
# Declaration
# ==========================================================

def p_declaration(p):
  'declaration : RW_VAR type declarator_list'
  p[0] = ('declaration', p[2], p[3])

def p_type_int(p):
  'type : RW_INT'
  p[0] = 'int'

def p_type_real(p):
  'type : RW_REAL'
  p[0] = 'real'

# ==========================================================
# Declarator list
# ==========================================================

def p_declarator_list_single(p):
  'declarator_list : declarator'
  p[0] = [p[1]]

def p_declarator_list_multiple(p):
  'declarator_list : declarator_list COMMA declarator'
  p[0] = p[1] + [p[3]]

# ==========================================================
# Declarators
# ==========================================================

def p_declarator_var(p):
  'declarator : ID'
  p[0] = ('var', p[1])

def p_declarator_vector(p):
  'declarator : ID ACOL expression FCOL'
  p[0] = ('vector', p[1], p[3])

def p_declarator_matrix(p):
  'declarator : ID ACOL expression FCOL ACOL expression FCOL'
  p[0] = ('matrix', p[1], p[3], p[6])

# ==========================================================
# Assignment
# ==========================================================

def p_assignment(p):
  'assignment : location CMD_ATR expression'
  p[0] = ('assign', p[1], p[3])

# ==========================================================
# Locations
# ==========================================================

def p_location_id(p):
    'location : ID'
    p[0] = ('id', p[1])

def p_location_vector(p):
  'location : ID ACOL expression FCOL'
  p[0] = ('vector_access', p[1], p[3])

def p_location_matrix(p):
  'location : ID ACOL expression FCOL ACOL expression FCOL'
  p[0] = ('matrix_access', p[1], p[3], p[6])

# ==========================================================
# Expressions
# ==========================================================

def p_expression(p):
  'expression : relational_expression'
  p[0] = p[1]

# ==========================================================
# Relational expressions
# ==========================================================

def p_relational_single(p):
  'relational_expression : arithmetic_expression'
  p[0] = p[1]

def p_relational_binary(p):
  '''
  relational_expression : arithmetic_expression OP_MIN arithmetic_expression
                        | arithmetic_expression OP_MAX arithmetic_expression
                        | arithmetic_expression OP_MIN_EQUAL arithmetic_expression
                        | arithmetic_expression OP_MAX_EQUAL arithmetic_expression
                        | arithmetic_expression OP_EQUAL arithmetic_expression
                        | arithmetic_expression OP_DIFF arithmetic_expression
  '''
  p[0] = ('relop', p[2], p[1], p[3])

# ==========================================================
# Arithmetic
# ==========================================================

def p_arithmetic_add(p):
  '''
  arithmetic_expression : arithmetic_expression OP_ADD term
                        | arithmetic_expression OP_SUB term
  '''
  p[0] = ('binop', p[2], p[1], p[3])

def p_arithmetic_term(p):
  'arithmetic_expression : term'
  p[0] = p[1]

# ==========================================================
# Term
# ==========================================================

def p_term(p):
  '''
  term : term OP_MUL power
      | term OP_DIV power
  '''
  p[0] = ('binop', p[2], p[1], p[3])

def p_term_power(p):
  'term : power'
  p[0] = p[1]

# ==========================================================
# Power
# ==========================================================

def p_power(p):
  'power : factor OP_PWR power'
  p[0] = ('binop', '^', p[1], p[3])

def p_power_factor(p):
  'power : factor'
  p[0] = p[1]

# ==========================================================
# Factors
# ==========================================================

def p_factor_num(p):
  'factor : NUM'
  p[0] = ('num', p[1])

def p_factor_location(p):
  'factor : location'
  p[0] = p[1]

def p_factor_expression(p):
  'factor : APAR expression FPAR'
  p[0] = p[2]

# ==========================================================
# While
# ==========================================================

def p_while(p):
  'while_stmt : RW_WHILE APAR expression FPAR ACHAVE statement_list FCHAVE'
  p[0] = ('while', p[3], p[6])

# ==========================================================
# If
# ==========================================================

def p_if(p):
  'if_stmt : RW_IF APAR expression FPAR ACHAVE statement_list FCHAVE RW_ELSE ACHAVE statement_list FCHAVE'
  p[0] = ('if', p[3], p[6], p[10])

# ==========================================================
# Operator precedence
# ==========================================================

precedence = (
  ('left', 'OP_MIN', 'OP_MAX', 'OP_MIN_EQUAL', 'OP_MAX_EQUAL', 'OP_EQUAL', 'OP_DIFF'),
  ('left', 'OP_ADD', 'OP_SUB'),
  ('left', 'OP_MUL', 'OP_DIV'),
  ('right', 'OP_PWR'),
)

# ==========================================================
# Error handling
# ==========================================================

def p_error(p):
  if p:
    print(f"Syntax error at '{p.value}'")
  else:
    print("Syntax error at EOF")

# ==========================================================
# Build parser
# ==========================================================


# Build the parser
parser = yacc.yacc()




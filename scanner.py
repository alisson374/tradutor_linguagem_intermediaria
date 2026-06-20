import ply.lex as lex

# --------------------------------
# Tokens
# --------------------------------
tokens = [
  'ID',
  'NUM',

  # Operadores aritméticos
  'OP_ADD',
  'OP_SUB',
  'OP_MUL',
  'OP_DIV',
  'OP_PWR',

  # Operadores relacionais
  'OP_MIN',
  'OP_MAX',
  'OP_MIN_EQUAL',
  'OP_MAX_EQUAL',
  'OP_EQUAL',
  'OP_DIFF',

  # Atribuição
  'CMD_ATR',

  # Delimitadores
  'APAR',
  'FPAR',
  'ACHAVE',
  'FCHAVE',
  'ACOL',
  'FCOL',
  'COMMA',
  'SEMI'
]

# --------------------------------
# Palavras reservadas
# --------------------------------
reserved = {
  'if': 'RW_IF',
  'else': 'RW_ELSE',
  'while': 'RW_WHILE',
  'var': 'RW_VAR',
  'int': 'RW_INT',
  'real': 'RW_REAL'
}

tokens += list(reserved.values())

# --------------------------------
# Regras simples
# --------------------------------
t_OP_ADD = r'\+'
t_OP_SUB = r'-'
t_OP_MUL = r'\*'
t_OP_DIV = r'/'
t_OP_PWR = r'\^'

t_OP_MAX_EQUAL = r'>='
t_OP_MIN_EQUAL = r'<='
t_OP_EQUAL = r'=='
t_OP_DIFF = r'!='
t_CMD_ATR = r'='
t_OP_MIN = r'<'
t_OP_MAX = r'>'

t_APAR = r'\('
t_FPAR = r'\)'
t_ACHAVE = r'\{'
t_FCHAVE = r'\}'
t_ACOL = r'\['
t_FCOL = r'\]'
t_COMMA = r','
t_SEMI = r';'
# --------------------------------
# Tokens complexos
# --------------------------------
def t_NUM(t):
  r'\d+(\.\d*)?'
  t.value = float(t.value) if '.' in t.value else int(t.value)
  return t


def t_ID(t):
  r'[A-Za-z][A-Za-z\d]*'
  t.type = reserved.get(t.value, 'ID')
  return t

# --------------------------------
# Ignorar espaços e tabs
# --------------------------------
t_ignore = ' \t\n'

# --------------------------------
# Tratamento de erro
# --------------------------------
def t_error(t):
  print(f"Caractere ilegal '{t.value[0]}'")
  t.lexer.skip(1)

# --------------------------------
# Construção do lexer
# --------------------------------
lexer = lex.lex()
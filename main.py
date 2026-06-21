from parser import parser
from scanner import scanner
from tac import tac




def print_tokens(src):
  scanner.input(src)

  print("Tokens table:")
  print('{:<10} {:<10}'.format('Token', 'Lexeme'))
  while True:  
     tok = scanner.token()
     if not tok: break
     print(f"{tok.type:<10} {tok.value:<10}")

def print_ast(tree):
   print("\nAST:")
   for node in tree:
      print(f'stmt{tree.index(node)}: {node}\n')

with open('codigo.txt', 'r', encoding='utf-8') as file:
  contentFile = file.read()

source = contentFile.strip()
(prog, mainStatementTree) = parser.parse(source)

print_tokens(source)
print_ast(mainStatementTree)
for line in tac.generateTac(mainStatementTree):
   print(line)
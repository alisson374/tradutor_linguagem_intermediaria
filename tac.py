
# class TACGenerator:

#     def __init__(self):
#         self.temp_count = 0
#         self.label_count = 0
#         self.code = []

#     # ----------------------------------
#     # Helpers
#     # ----------------------------------

#     def new_temp(self):
#         self.temp_count += 1
#         return f"t{self.temp_count}"

#     def new_label(self):
#         self.label_count += 1
#         return f"L{self.label_count}"

#     def emit(self, instruction):
#         self.code.append(instruction)

#     # ----------------------------------
#     # Entry point
#     # ----------------------------------

#     def generate(self, ast):

#         if ast[0] == 'program':
#             for stmt in ast[1]:
#                 self.gen_stmt(stmt)

#         return self.code

#     # ----------------------------------
#     # Statements
#     # ----------------------------------

#     def gen_stmt(self, node):

#         kind = node[0]

#         if kind == 'declaration':
#             return

#         if kind == 'assign':
#             self.gen_assign(node)
#             return

#         if kind == 'while':
#             self.gen_while(node)
#             return

#         if kind == 'if':
#             self.gen_if(node)
#             return

#     # ----------------------------------
#     # Assignment
#     # ----------------------------------

#     def gen_assign(self, node):

#         _, location, expr = node

#         value = self.gen_expr(expr)
#         target = self.gen_location(location)

#         self.emit(f"{target} = {value}")

#     # ----------------------------------
#     # While
#     # ----------------------------------

#     def gen_while(self, node):

#         _, condition, body = node

#         start = self.new_label()
#         end = self.new_label()

#         self.emit(f"{start}:")

#         cond = self.gen_expr(condition)

#         self.emit(f"ifFalse {cond} goto {end}")

#         for stmt in body:
#             self.gen_stmt(stmt)

#         self.emit(f"goto {start}")
#         self.emit(f"{end}:")

#     # ----------------------------------
#     # If Else
#     # ----------------------------------

#     def gen_if(self, node):

#         _, condition, then_body, else_body = node

#         else_label = self.new_label()
#         end_label = self.new_label()

#         cond = self.gen_expr(condition)

#         self.emit(f"ifFalse {cond} goto {else_label}")

#         for stmt in then_body:
#             self.gen_stmt(stmt)

#         self.emit(f"goto {end_label}")

#         self.emit(f"{else_label}:")

#         for stmt in else_body:
#             self.gen_stmt(stmt)

#         self.emit(f"{end_label}:")

#     # ----------------------------------
#     # Expressions
#     # ----------------------------------

#     def gen_expr(self, node):

#         kind = node[0]

#         if kind == 'num':
#             return str(node[1])

#         if kind == 'id':
#             return node[1]

#         if kind == 'vector_access':
#             index = self.gen_expr(node[2])
#             return f"{node[1]}[{index}]"

#         if kind == 'matrix_access':
#             i = self.gen_expr(node[2])
#             j = self.gen_expr(node[3])
#             return f"{node[1]}[{i}][{j}]"

#         if kind == 'relop':

#             op = node[1]

#             left = self.gen_expr(node[2])
#             right = self.gen_expr(node[3])

#             temp = self.new_temp()

#             self.emit(
#                 f"{temp} = {left} {op} {right}"
#             )

#             return temp

#         if kind == 'binop':

#             op = node[1]

#             left = self.gen_expr(node[2])
#             right = self.gen_expr(node[3])

#             temp = self.new_temp()

#             self.emit(
#                 f"{temp} = {left} {op} {right}"
#             )

#             return temp

#         self.error(f"Unknown expression {kind}")

#     # ----------------------------------
#     # Locations
#     # ----------------------------------

#     def gen_location(self, node):

#         kind = node[0]

#         if kind == 'id':
#             return node[1]

#         if kind == 'vector_access':

#             idx = self.gen_expr(node[2])

#             return f"{node[1]}[{idx}]"

#         if kind == 'matrix_access':

#             i = self.gen_expr(node[2])
#             j = self.gen_expr(node[3])

#             return f"{node[1]}[{i}][{j}]"

#         self.error(f"Unknown location {kind}")
    

# generator = TACGenerator()

# tac = generator.generate(result)

# for line in tac:
#     print(line)


class Tac:
  def __init__(self):
    self.temp_count = 0
    self.label_count = 0
    self.code = []
    self.indent = 0
    self.variables = []

  def generateTac(self, ast):
    for node in ast:
      self.generate_statement(node)
    return self.code

  def generate_statement(self, node):
    smt = node[0]
    
    if smt == 'declaration':
      self.generate_table_variable(node)
    
    elif smt == 'assign':
      self.generate_assign(node)

    elif smt == 'while':
      self.generate_while(node)

    elif smt == 'if':
      self.generate_if(node)

    elif smt == 'ifelse':
      self.generate_if_else(node)

  def generate_assign(self, node):
    _, name, expr2 = node
    if not self.check_variable(name[1]):
      self.error(f"Variable '{name[1]}' not declared")
    else:
      target = self.gen_target(name)
      value = self.generate_expression(expr2)
      self.code.append(f"{"\t" * self.indent}{target} = {value}")

  def generate_while(self, node):
    _, condition, body = node
  
    start = self.while_label()
    end = self.end_label()

    start_label = self.set_start_label(start)
    self.indent += 1
    self.code.append(start_label)

    cond = self.generate_inverse_relop(condition)

    self.code.append(f"{"\t" * self.indent}IF {cond} GOTO {end}")

    for stmt in body:
        self.generate_statement(stmt)

    self.code.append(f"{"\t" * self.indent}GOTO {start}")
    self.code.append(f"{end}:")
    self.indent -= 1

  def generate_table_variable(self, node):
    _, v_types, = node
    for var in v_types:
      v_type, variables = var
      for variable in variables:
        self.variables.append((v_type, variable))
          
  def check_variable(self, variable):
    name = variable

    if isinstance(variable, tuple) and len(variable) >= 2:
        if variable[0] == 'id':
            name = variable[1]
        elif variable[0] in ('var', 'vector', 'matrix'):
            name = variable[1]

    for _, declarator in self.variables:
        if isinstance(declarator, tuple) and len(declarator) >= 2:
            if declarator[1] == name:
                return True

    return False

  def generate_if(self, node):
    _, expression_b, then_body = node
    
    if len(expression_b) != 4:
      self.error("Invalid IF expression structure")
    
    if expression_b[0] != 'relop':
      self.error("IF expression must be a relational operation")
    
    end = self.end_label()
    b_exp = self.generate_inverse_relop(expression_b)
    
    start_label = "IF" + ' ' + b_exp + ' GOTO ' + end
    self.code.append(f"{"\t" * self.indent}{start_label}")

    for stmt in then_body:
        self.generate_statement(stmt)

    self.code.append(f"{end}:")
    
  def generate_if_else(self, node):
    _, expression_b, then_body, else_body = node
    
    if len(expression_b) != 4:
      self.error("Invalid IF expression structure")
    
    if expression_b[0] != 'relop':
      self.error("IF expression must be a relational operation")
    
    else_label = self.else_label()
    end_label = self.end_label()
    
    b_exp = self.generate_inverse_relop(expression_b)
    
    start_label = "IF" + ' ' + b_exp + ' GOTO ' + else_label
    self.code.append(f"{"\t" * self.indent}{start_label}")
    
    for stmt in then_body:
        self.generate_statement(stmt)

    self.code.append(f"{"\t" * self.indent}GOTO {end_label}")
    self.code.append(f"{else_label}:")
    
    for stmt in else_body:
        self.generate_statement(stmt)

    self.code.append(f"{end_label}:")

  def generate_expression(self, node):
    kind = node[0]
    if kind == 'num':
      return str(node[1])
    elif kind == 'id':
      if not self.check_variable(node):
        self.error(f"Variable '{node[1]}' not declared")
      return node[1]
    elif kind == 'binop':
      op = node[1]
      left = self.generate_expression(node[2])
      right = self.generate_expression(node[3])
      temp = self.temp();

      self.code.append(f"{"\t" * self.indent}{temp} = {left} {op} {right}")
      return temp
    elif kind == 'relop':
        return self.generate_relop(node) 
    elif kind == 'vector_access':
      if not self.check_variable(node[1]):
        self.error(f"Variable '{node[1]}' not declared")
      else:
        index = self.generate_expression(node[2])
        return f"{node[1]}[{index}]"
    elif kind == 'matrix_access':
      if not self.check_variable(node[1]) or not self.check_variable(node[2]) or not self.check_variable(node[3]):
        self.error(f"Variable '{node[1]}' or its indices not declared")
      else: 
        i = self.generate_expression(node[2])
        j = self.generate_expression(node[3])
        return f"{node[1]}[{i}][{j}]"
    

  def generate_inverse_relop(self, node):
    inverse_table = {
      '<': '>=',
      '>': '<=',
      '<=': '>',
      '>=': '<',
      '==': '<>',
      '<>': '=='
    }
    title = node[0]
    if title != "relop":
      self.error("Expected a relational operation node")

    _, operator, left, right = node
    first_operand = self.generate_expression(left)
    second_operand = self.generate_expression(right)

    return f"{first_operand} {inverse_table[operator]} {second_operand}"
  
  def generate_relop(self, node):
    op = node[1]
    left = self.generate_expression(node[2])
    right = self.generate_expression(node[3])
    temp = self.temp();

    self.code.append(f"{"\t" * self.indent}{temp} = {left} {op} {right}")
    return temp

  def temp(self):
    self.temp_count += 1
    return f"T{self.temp_count}"  
  
  def while_label(self):
    self.label_count += 1
    return f"WHILE{self.label_count}"

  def else_label(self):
    self.label_count += 1
    return f"ELSE{self.label_count}"

  def end_label(self):
    self.label_count += 1
    return f"END{self.label_count}"

  def if_label(self):
    self.label_count += 1
    return f"IF{self.label_count}"
  
  def set_start_label(self, start):
    return f"{"\t" * self.indent}{start}:"

  def gen_target(self, node):
    kind = node[0]

    if kind == 'id': 
      return node[1]
    if kind == 'vector_access':
      index = self.generate_expression(node[2])
      return f"{node[1]}[{index}]"
    if kind == 'matrix_access':
      i = self.generate_expression(node[2])
      j = self.generate_expression(node[3])
      return f"{node[1]}[{i}][{j}]"

    self.error(f"destino do tipo {kind} desconhecido")
    
  def error(self, message):
    exit(f"TAC Generation Error: {message}")
    
tac = Tac()
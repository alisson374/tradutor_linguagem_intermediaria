
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

#         raise Exception(f"Unknown expression {kind}")

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

#         raise Exception(f"Unknown location {kind}")
    

# generator = TACGenerator()

# tac = generator.generate(result)

# for line in tac:
#     print(line)

class Tac:
  def __init__(self):
    self.temp_count = 0
    self.label_count = 0
    self.code = []

  def generateTac(self, ast):
    for node in ast:
      self.generate_smt(node)
    return self.code

  def generate_smt(self, node):
    smt = node[0]
    
    if smt == 'assign':
      self.generate_assign(node)
    elif smt == 'while':
      self.generate_while(node)
  
  def generate_assign(self, node):
    _, expr1, expr2 = node
    self.code.append(f"{expr1[1]} = {expr2[1]}")

  def generate_while(self, node):
    _, condition, body = node
  
    start = self.while_label()
    end = self.end_label()

    self.code.append(f"{start}:")

    cond = self.generate_expression(condition)

    self.code.append(f"IF {cond} GOTO {end}")

    for stmt in body:
        self.generate_statement(stmt)

    self.code.append(f"GOTO {start}")
    self.code.append(f"{end}:")

  def generate_expression(self, node):
    #to do 
    return "expression"

  def generate_statement(self, node):
    #to do 
    return "expression"

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

tac = Tac()
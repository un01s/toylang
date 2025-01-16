# 
# simple interpreter in python
#
# step4: 
# -- add variables
#

import sys

class Ev:
  def ev(self, s):
    self.vars = {} # dictionary to store variable names and their values
    lines = [x for x in s.split("\n") if x.strip() != ""]
    for line in lines:
      (name, _, expr) = line.split(maxsplit=2)
      self.vars[name] = self.ev_expr(expr)
    print(self.vars) 
  def ev_expr(self, s):
    toks = s.split()
    stack = []
    for tok in toks:
      if tok.isdigit():
        stack.append(int(tok))
      elif tok in self.vars:
        stack.append(self.vars[tok])
      elif tok == "+":
        rhs = stack.pop()
        lhs = stack.pop()
        stack.append(lhs + rhs)
    return stack[0]

Ev().ev(open(sys.argv[1]).read())

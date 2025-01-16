# 
# simple interpreter in python
#
# step3: 
# -- refactor the code with class
# -- handle multiple lines of code
#

import sys

class Ev:
  def ev(self, s):
    lines = [x for x in s.split("\n") if x.strip() != ""]
    for line in lines:
      print(self.ev_expr(line)) 
  def ev_expr(self, s):
    toks = s.split()
    stack = []
    for tok in toks:
      if tok.isdigit():
        stack.append(int(tok))
      elif tok == "+":
        rhs = stack.pop()
        lhs = stack.pop()
        stack.append(lhs + rhs)
    return stack[0]

Ev().ev(open(sys.argv[1]).read())

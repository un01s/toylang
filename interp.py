# 
# simple interpreter in python
#

import sys

def ev(s):
  toks = s.split()
  stack = []
  for tok in toks:
    if tok.isdigit():
      stack.append(int(tok))
    elif tok == "+":
      rhs = stack.pop()
      lhs = stack.pop()
      stack.append(lhs + rhs)
  print(stack[0])

ev(open(sys.argv[1]).read())

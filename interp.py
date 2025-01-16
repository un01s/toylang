# 
# simple interpreter in python
#

import sys

def ev(s):
  print(s)

ev(open(sys.argv[1]).read())

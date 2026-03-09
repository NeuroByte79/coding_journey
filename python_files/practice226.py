import keyword
print(keyword.kwlist)

import math 
import random
import os
import sys
print(math.factorial(5))
print(math.degrees(math.pi))
print(random.random(),"\n")
print(dir(__builtins__) ,"\n")
print(dir(math),'\n')
print(dir(random),'\n')
print(dir(sys),'\n')
print(dir(os),'\n')
help(random.randint,)
print(sys.version,'\n')
print(os.getcwd,'\n')
print(sys.platform,'\n')
print(sys.path,'\n')
import os, sys

def BADFunction(x,y): return x+y

class myclass:
 def __init__(self): self.a=1;self.b=2
 def getData(self): return self.a+self.b

def foo():
    print("This is a long line that should definitely trigger a max-line-length warning in pylint configuration if it's set to anything reasonable like 100 characters or less.")
    unused_variable = 42
    a = 1
    b = 2
    if a == 1:
        if b == 2:
            if True:
                if False:
                    if a == b:
                        print("Deeply nested!")

foo()
BADFunction(1,2)

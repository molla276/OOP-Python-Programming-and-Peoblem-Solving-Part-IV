num=0
def demo():
    #print(num)
    num=1
    print("The Number is:",num)
demo()

def demo():
    print(Str)
# Global  
Str = "You are clever"
demo()

def func_outer():
    x = "local"
    def func_inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    func_inner()
    print("outer:", x)
func_outer()

# Built-in Scope 
from math import pi 
# pi = 'Not defined in global pi'
def func_outer(): 
    # pi = 'Not defined in outer pi' 
    def inner(): 
        # pi = 'not defined in inner pi' 
        print(pi) 
    inner() 
func_outer()
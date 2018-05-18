import sys
sys.setrecursionlimit(50000) # extra stack room


import time
from random import *


def guess( hidden ):
    """ a #-guessing example
        to highlight using the
        random library
    """

    comp_guess = choice(range(100)) # 0 to 99, incl.

    if comp_guess == hidden:
        print("I got it! It was", comp_guess)
        print("Total guesses:")
        return 1

    else:
        print("Aargh. I guessed", comp_guess)
        time.sleep(0.1)
        return 1 + guess( hidden )
import random
def rwpos(a, b):
    
    compgs =  random.choice(range(a-b, a+b))
    if compgs == a:
        print("start is", compgs)
        return 1
    else:
        print("start is", compgs)
        return 1 + rwpos(a, b)
print rwpos(40, 4)
import sys
import random
import time
def rwsteps(start, low, hi):
    cmgs = random.choice(range(low, hi))
    if cmgs == start:
         print "start is", cmgs
         return 1
    else:
         print "start is", cmgs
         time.sleep(0.1) 
         return 1 + rwsteps(start, low, hi)
print rwsteps(10, 5, 15)
    

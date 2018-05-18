import math
def fn(n):
    #a=math.sqrt(n)
    b=math.cos(n)
    #c=cos(pi)
    return b
def dbl(x):
    return 2*x
def tpl(x):
    return 3*x
def sq(n):
    return n*n
def interp(low,hi,fraction):
    return (((hi-low)*fraction)+low)
def checkends(string):
    if string[0]==string[-1]:
        return True
    else:
        return False

def flipside( s ):
    x = len(s)//2
    return  s[:x]+s[x:]

def convertFromSeconds( s ):
    days = s // (24*60*60)  
    s = s % (24*60*60)     
    hours = s //(60*60)
    minutes = s //(60)
    seconds = s //(1)
    return [days, hours, minutes, seconds]



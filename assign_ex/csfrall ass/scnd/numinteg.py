def db(x):
     return 2*x
def sq(x):
     return x**2
def lcmult( N ):
   return [ 2*x for x in range(N) ]
def lcidiv( N ):
   return [ x/2 for x in range(N) ]
def lcfdiv( N ):
   return [ float(x)/2 for x in range(N) ]
def unitfracs( N ):
    pass
def unitfracs1(N):
     return [ float(x)/2 *2/N   for x in range(N) ]
def scaledfracs(low,high,N):
   #return [  float ( low + ( ( high - low ) / (n) ) )  for x in range(n)]
        #return [float( low + (i * ((high - low))/( N))) for i in range(N)]
    return [ float ( low + ( i * float ( high - low ) / N ) ) for i in range ( N )]
def sqfracs(low,high,n):
    return[ float(low +(i*(high - low)/n))*float(low +(i*(high - low)/n)) for i in range(n) ]
def fofracs(f,low,high,n):
    return[ float (low +(i*(high - low)/n)) for i in range(n) ]

print(db(5))
print(sq(4))
print(lcmult(9))
print(lcidiv(5))
print(lcfdiv(10))
print(unitfracs( 5 ))
print(unitfracs1( 5 ))

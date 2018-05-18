def flipside(s):
  
  x = len(s)//2
  return s[x:] + s[:x]


print(flipside('carpets'))
print(flipside('python'))
print(flipside('flipside'))  
print(flipside('az'))              
print(flipside('a'))                
print(flipside(''))
def mult(n, m):
  return n * m
print mult(6, 7)
print mult(6, -7)
print mult(-6, -7)
print mult(6, 0)
print mult(0, 7)
print mult(0, 0)
def dot(a, b):
  if len(a) != len(b):
    return float(0)
  elif a == ' ' and b == ' ':
    return float(0)
  else:
    ab = [a[i]*b[i] for i in range(len(a))]
    c = sum(ab)
    return float (c)

print dot([1, 2, 3, 4], [10, 100, 1000, 10000])
print dot([5, 3], [6, 4])
print dot([5, 3], [6])
print dot([], [6])
print dot([], [])

def scrableScore(a):
    itr = 'abcdefghijklmnopqrstuvwxyz'
    itr1 = ('a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u') 
    itr2 = ('d', 'g') 
    itr3 = ('b','c', 'm', 'p') 
    itr4 = ('f', 'h', 'v', 'w', 'y') 
    itr5 = ('k') 
    itr6 = ('j', 'x') 
    itr7 = ('q','z')
    if len(a) == 0:  
        return 0
    if a[0] not in itr:
        return 0
    if a[0] in itr1:
       return 1 + scrableScore(a[1:])
    if a[0] in itr2:
        return 2 + scrableScore(a[1:])
    if a[0] in itr3:
        return 3 + scrableScore(a[1:]) 
    if a[0] in itr4:
        return 4 + scrableScore(a[1:]) 
    if a[0] in itr5:
        return 5 + scrableScore(a[1:]) 
    if a[0] in itr6:
        return 8 + scrableScore(a[1:]) 
    if a[0] in itr7:
        return 10 + scrableScore(a[1:])
    
print(scrableScore('quetzal'))
print (scrableScore('jonquil'))
print (scrableScore('syzygy'))
print (scrableScore('abcdefghijklmnopqrstuvwxyz'))
print (scrableScore('?!@#$%^&*()'))
print (scrableScore(''))
def scrableScore(a):
    itr = 'abcdefghijklmnopqrstuvwxyz'
    itr1 = ('aeilnorstu') 
    itr2 = ('dg') 
    itr3 = ('bcmp') 
    itr4 = ('fhvwy') 
    itr5 = ('k') 
    itr6 = ('jx') 
    itr7 = ('qz') 
    if a in itr1:
       return 1 
    if a in itr2:
        return 2 
    if a in itr3:
        return 3  
    if a in itr4:
        return 4  
    if a in itr5:
        return 5  
    if a in itr6:
        return 8  
    if a in itr7:
        return 10  
print(scrableScore('qz'))
def transcribe(a):
    b = ' '
    if len(a) == 0:
        return ' '
    if a[0] == ' ':
        return transcribe(a[1:]) 
    if a[0] == 'A':
        return 'U' + transcribe(a[1:])
    if a[0] == 'C':
        return 'G' + transcribe(a[1:])
    if a[0] == 'G':
        return 'C' + transcribe(a[1:])
    if a[0] == 'T':
        return 'A' + transcribe(a[1:])
    else:
        return ''
print transcribe('ACGT TGCA')
print transcribe('GATTACA')
print transcribe('cs5')
print transcribe('')





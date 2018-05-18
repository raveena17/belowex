'''def erdos(n):
    if n%2 ==0:
        a = (n/2)
        return a
    else:
        a = (3*n + 1)
        return a
print erdos(84)
print erdos(1413)
print erdos(1)'''
'''def erdosIter(n, i):
    for x in range(i):
        if n%2 == 0:
           n = (n/2)
           
        else:
            n = (3*n + 1)
    return n
print erdosIter(84, 1)
print erdosIter(42, 0)
print erdosIter(3, 7)'''

def erdosIter(n):
         count=0
         count = count + 1
        # a = []
         
         if n == 1:
             return ' '
         if n%2 == 0:
          
           n = (n/2)
           #print n
           
           #count=count+1
           print n
           #a.append(n)
           #print a,
           
           return  (erdosIter(n))
           
         else:
            n = (3*n + 1)
            print n
            #a.append(n)
            #count=count+1
            #print count
            #print a,
            
            return  (erdosIter(n))
         
          
   
  
print erdosIter(3)
#print erdosIter(42)
#print erdosIter(3)

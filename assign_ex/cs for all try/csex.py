def rot(a,n):
 #import pdb; pdb.set_trace()
 res =""
 b=len(a)
 print b
 for i in range(b):
   c = ord (a[i])
   if c <= 65 and c >= 32:
         res+=(chr(c))
   if c <= 90 and c >65:   #-------CAPS-------#
      l2 =(c+n)
      if l2 >= 90:
        l3 = l2 - 25
        res+=(chr(l3))
      else:
            l2 = c+n
            
            res+=(chr(l2))      
   d = (c + n)  
   if d > 122:    #------small------------#
      l1 = (d - 26)
      res+=(chr(l1))
   else:
       res+=(chr(d))
      
 print res
print rot('xyza?',1)
 
 

def rot(a, n):
 #import pdb;pdb.set_trace()
 res =""
 b = len(a)
 #print b
 #if b == 0:
      return ''
 c = ord (a[0])
 if c <= 90:   #-------CAPS-------#
      l2 =(c+n)
      if l2 >= 90:
        l3 = l2 - 25
        l4 = chr(l3)
        #print l4,
        res+=l4
        return rot(a[1:], n)
      else:
        l5 = chr(l2)
        #print(l5,)
        res+=l5
        return rot(a[1:], n)
 d = (c + n)
 if d > 122:    #------small------------#
      l1 = (d - 26)
      s = chr(l1)
      #print s,
      res+=s
      return rot(a[1:], n)
 else:
      f = chr(d)
      #print f,
      res+=f
      return rot(a[1:], n)
 print res
 print rot("xyza", 1)
 #print res

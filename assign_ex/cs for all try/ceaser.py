def rot(c, n):
    a = ord(c)
    b = (a + n)
    #print(b)
    if b >= 122:
        l1 = (b - 26)
        s = chr(l1)
        return s
    if b <= 90:
        l2 = (b - 25)
        t = chr(l2)
        return t
        
    else:
        d = chr(b)
        return d
        
    
         

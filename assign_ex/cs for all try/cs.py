def rot(c, n):
    a = ord(c)
    if a == 32:
        t = chr(a)
        return t
    if a <= 90:
        l2 = (a + n)
        if l2 > 90:
            l3 = l2 -25
            return  chr(l3)
        else:
            return chr(l2)
    b = (a + n)
    if b > 122:
        l1 = (b - 26)
        return chr(l1) 
    else:
        return chr(b)
print rot('a', 5)
        

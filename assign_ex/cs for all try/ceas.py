def rot(c, n):
    ass = ord(c)
    if ass <= 90:
        l2 = (ass + n)
        l3 = chr(l2)
        return l3
    b = (ass + n)
    print(b)
    if b >= 122:
        l1 = (b - 26)
        s = chr(l1)
        return s
    else:
        d = chr(b)
        return d
        

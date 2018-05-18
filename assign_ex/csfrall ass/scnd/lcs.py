def lcs(string1, string2,res):
    a = string1
    b=''
    if len(string2) == 0:
        return 0
    if string2[0] not in a:
        return (lcs(string1[0:], string2[1:],))
    if string2[0] in a:
        c = (lcs(string1[1:], string2[1:]))
        b+=string2[0]
    print b    
print(lcs('human', 'chimp',res))
print(lcs('gattaca', 'tacgaacta',res))
print(lcs('wow', 'whew',res))
    
  

def lcs(string1, string2,res):
    a = string2
    #res=''
    if len(string1) == 0:
        return res
    if string1[0] not in a:
        return (lcs(string1[1:], string2[0:],res))
    if string1[0] in a:
        #b=[]
        #string1[0].append(b)
        #print(string1[0])
        b=string1[0]
        res=res+b
        #print b
        return (lcs(string1[1:], string2[1:],res))
print(lcs('human', 'chimp',res=''))
print(lcs('gattaca', 'tacgaacta',res=''))
print(lcs('wow', 'whew',res=''))
    

'''def simpleDistance(s1, s2):
    Takes two strings of the same length and returns the
       number of positions in which they differ.
    if s2 == "":     # len(s2) is also 0 since strings
                         # have the same length
        return 0          # base case
    
    if s1[0] == s2[0]:   # recursive step, case 1
        return 1 + simpleDistance(s1[1:], s2[0:])
    elif s2 == " " and s1[1:] :
        return simpleDistance(s1[1:], s2[0:])
    else:                 
                         # s1[0] == s2[0]
        return simpleDistance(s1[0:], s2[1:])'''
    
def simpleDistance(s1, s2):
    '''Takes two strings of the same length and returns the
       number of positions in which they differ.'''
    if len(s1) == 0:        
         return 0  
    if s1[0] == s2[0]: 
         return 1 + simpleDistance(s1[0:], s2[1:])
    else:
         return simpleDistance(s1[1:], s2[0:])
     
'''def lcs(a, b):
    if a == "":
        return 0
    if a[0] == b[0]:
        return (a[0]) + (lcs(a[1], b[1]))
    else:
        return lcs(a[0], b[1])'''
        
        
 

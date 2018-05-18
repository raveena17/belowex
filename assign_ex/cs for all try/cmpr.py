'''def cmpr(a, b):
    if len(a) == 0:
        return 0
    elif a[0] == b[0]:
        return 1 + (cmpr(a[1:], b[1:]))
    else:
        return (cmpr(a[0:], b[1:]))'''
'''def cmpr(s1, s2):
    Takes two strings of the same length and returns the
       number of positions in which they differ
    if len(s1) == 0:     # len(s2) is also 0 since strings
                         # have the same length
        return 0         # base case
    elif s1[0] == s2[0]: # recursive step, case 1
        return 1 + cmpr(s1[1:], s2[1:])
    else:                # recursive step, case 2:
                         #   s1[0] == s2[0]
        return cmpr(s1[1:], s2[1:])'''
'''def simpleDistance(s1, s2):
    Takes two strings of the same length and returns the
       number of positions in which they differ.
    if len(s1) == 0:     # len(s2) is also 0 since strings
                         # have the same length
        return 0         # base case
    elif s1[0] == s2[0]: # recursive step, case 1
        return 1 + simpleDistance(s1[0], s2[1:])
    else:                # recursive step, case 2:
                         #   s1[0] == s2[0]
        return simpleDistance(s1[1:], s2[0:])''''
def simpleDistance(s1, s2):
    '''Takes two strings of the same length and returns the
       number of positions in which they differ.'''
    if len(s1) == 0:     # len(s2) is also 0 since strings
                         # have the same length
        return 0         # base case
    elif s1[0] != s2[0]: # recursive step, case 1
        return 1 + simpleDistance(s1[0:], s2[1:])
    else:                # recursive step, case 2:
                         
        return simpleDistance(s1[1:], s2[0:])

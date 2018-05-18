def simpleDistance(s1, s2):
    '''Takes two strings of the same length and returns the
       number of positions in which they differ.'''
    if len(s1) == 0:     # len(s2) is also 0 since strings
                         # have the same length
        return 0         # base case
    elif s1[0] == s2[0]: # recursive step, case 1
        return 1 + simpleDistance(s1[:0], s2[1:])
    else:                # recursive step, case 2:
                         #   s1[0] == s2[0]
        return simpleDistance(s1[1:], s2[0:])

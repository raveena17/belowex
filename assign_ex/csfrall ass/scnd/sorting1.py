def st(string1, string2):
    if len(string1) == 0:
        return 0
    a = string2
    if string1[0] in a:
        return 1 + st(string1[1:], string2[0:])
    if string1[0] not in a:
        return 0 + st(string1[1:], string2[0:])
print(st('geese', 'elate'))
print(st('dinner', 'syrup'))
print(st('gattaca', 'aggtccaggcgc'))
def recursivesort(alist):
    def helper(sorting,already):
        new=[]
        if len(sorting)==0:
            return already
        else:
            x=min(sorting)
            sorting.remove(x)
            new.append(x)
            return helper(sorting,already+new)
    return helper(alist,[])

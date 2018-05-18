def st(string1, string2):
    if len(string2) == 0:
        return 0
    a = string1
    if string2[0] in a:
        return 1 + st(string1[0:], string2[1:])
    if string2[0] not in a:
        return 0 + st(string1[0:], string2[1:])
print(st('geese', 'elate'))
print(st('dinner', 'syrup'))
print(st('gattaca', 'aggtccaggcgc'))

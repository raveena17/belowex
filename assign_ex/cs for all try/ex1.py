'''def st(string1, string2):
    if len(string1) == 0:
        return 0
    a = [string1]
    if string2[0] in a:
        return 1 + st(string1[0:], string2[1:])
    if string2[0] not in a:
        return 0 + st(string1[0:], string2[1:])
print(st('abc', 'cba'))'''
def asc(string):
    a=''
    for i in range(3):
        a+='@'
        print a
    
#print asc('@')
        

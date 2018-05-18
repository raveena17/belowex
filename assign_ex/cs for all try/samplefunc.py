'''def scrableScore(a):
    itr = 'abcdefghijklmnopqrstuvwxyz'
    itr1 = ('a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u') 
    itr2 = ('d', 'g') 
    itr3 = ('b','c', 'm', 'p') 
    itr4 = ('f', 'h', 'v', 'w', 'y') 
    itr5 = ('k') 
    itr6 = ('j', 'x') 
    itr7 = ('q','z') 
    if a[0] in itr1:
       return 1 + scrableScore(a[1:])
    if a[0] in itr2:
        return 2 + scrableScore(a[1:])
    if a[0] in itr3:
        return 3 + scrableScore(a[1:]) 
    if a[0] in itr4:
        return 4 + scrableScore(a[1:]) 
    if a[0] in itr5:
        return 5 + scrableScore(a[1:]) 
    if a[0] in itr6:
        return 8 + scrableScore(a[1:]) 
    if a[0] in itr7:
        return 10 + scrableScore(a[1:] 
print(scrableScore('quetsal'))'''
'''def choose_sets(mylist,length):
    mylen = len(mylist)

    if length == mylen:
        return [mylist]
    if length == 1:
        return [[i] for i in mylist]
    if length > mylen:
        return []

    ToRet = []
    for k in xrange(mylen): 
        if mylen - k + 1> length :
            for j in choose_sets(mylist[k+1:],length-1):
                New = [mylist[k]]
                New.extend(j)
                ToRet.append(New)
    return ToRet

print choose_sets([1,2,3,4],2)'''
def combinations(lst,k):
    n = len(lst)
    if n == k:
        return [set(lst)]
    if k == 1:
        return [set([lst[i]]) for i in range(n)]
    v1 = combinations(lst[:-1], k-1)
    v1new = [ i.add(lst[n-1]) for i in v1]
    v2 = combinations(lst[:-1], k)
    return v1+v2
print(combinations([1,2,3,4], 2))
                                 

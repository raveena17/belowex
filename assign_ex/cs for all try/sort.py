'''def sort(alist):
    a=[]
    if alist == []:
        return a
    else:
        b=min(alist)
        b.append(a)
        b.remove(alist)
        return a
    return sort(alist)
print  sort([0,1,0,1])'''
'''def cmpr(s1,s2):
    if s1[0] != s2[0]:
        return 1
    elif s1[0]==s2[0]:
        count=0
        count=count+1
        return count
    else:
        count1=cmpr(s1[1:],s2[1:])
    return 0'''
def resort(a_list):
    def hel(list1, list2):
        new = []
        if len(list1) == 0:
            return list2
        else:    
            x = min(list1)    
            list1.remove(x)
            new.append(x)
            return hel(list1, list2 + new)
    #return hel(a_list, [])
print resort([1,0,1,0])
'''def cmpr(a,b):
    if a[0]==b[0]:
        return (1 + (cmpr(a[1:],b[1:])))
    else:
        return (cmpr(a[0:], b[1:]))'''
    

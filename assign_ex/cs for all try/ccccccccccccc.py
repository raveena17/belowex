def add(x,y):
    return x+y
def mapreduce(mapfn,n,mylist):
    mylist1=mylist
    newlist=reduce(mapfn, mylist)
    a=newlist-mylist[0]
    if a!=n:
        b=newlist-mylist[1]
        #print b
    if a==n:
        print 'True'
    if newlist== []:
          return False
        #return newlist
#print(mapreduce(add,42,[25,1,25]))
def fn(n,mylist):
    if len(mylist) == 0:
        return False
    b=sum(mylist)
   # print b
    c=b-mylist[0]
    if c==n:
        return True

    else:
        return fn(n,mylist[1:])
print fn(42,[25,16,2,15])

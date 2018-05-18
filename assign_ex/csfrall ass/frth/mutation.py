myarray = [1, 2,5,6]
def threshold(myarray, thresh):
    for i in range(len(myarray)):
        if myarray[i] > thresh:
            myarray[i] = 0
        else:
             myarray[i]
    return myarray         
#print threshold(myarray, 5)
'''def myreverse(l):
    a = len(l)
    for i in range(a):
      if  == 0:
        l
    else:
        res'''
x = [1, 2 ,3, 4, 5]
def myreverse(x):
 newx = []
 for i in range(1, len(x)+1):
  newx.append(x[-i])
  #print x[-i]
        
 print newx
l = [1,2,3,4,5]
def myremove(l, elem):
    for i in range(len(l)):
        if l[i] == elem:
          l.remove(l[i])
        else:
             l[i]
    print l
#print myremove(l, 5)   

array=([[8,1,6],[3,5,7],[4,9,2]])
def twod(array):
  #import pdb;pdb.set_trace()
  e=len(array)
  a=[]
  for row in range(e):
       a.append(sum(col[row] for col in array))
  a1=((sum(a)/float(e)))
  #print a1
  #print a
  b=[]
  for col in range(e):
        b.append (sum(row[col] for row in array))
  b1=((sum(b))/float(e))
  #print b1
  #print b
  c=0
  for row in range(len(array)):
      for col in range(len(array)):
            if row==col:
              c=c+(array[row][col])
  d=0
  for row in range(len(array)):
       for col in range((e-1),-1,-1): 
            d = d + array[row][col]
            break
  if a1==b1==c==d:
     return True
  else:
    return False
print twod(array)
    
   

'''def d2d():
    grid = [ [1]*8 for n in range(8)]
    print grid
    for row in range(grid):
        for col in range(row):
            print [row][col]'''



'''def d2d():
    #xs=[[1,2],[3,4],[5,6]]
    for i in range(len(xs)):
        for j in range(len(xs[i])):
            print xs

    return [xs[i][j]]'''
def ls(n):
    a=len(n)
    b=[]
    for i in range(1,a+1):
        b.append(n[-i])   
    return b

'''def ascii():
    
   print ("Pattern C")
   for e in range (11,0,-1):
      print((11-e) * ' ' + e * '*')

   print ('')
   print ("Pattern D")
   for g in range (11,0,-1):
      print(g * ' ' + (11-g) * '*')'''
'''def asc(n):

   for idx in range(n-1):
      print((n-idx) * ' ' + (2*idx+1) * '*')
   for idx in range(n-1, -1, -1):
      print((n-idx) * ' ' + (2*idx+1) * '*')
print asc(4)'''
def createdonerow(width, height):
    A=''
    row=''
    for row in range(height):
        row=''
        for col in range(width):
           row+='*'
        A+='*'   
        print row
print createdonerow(3,5)


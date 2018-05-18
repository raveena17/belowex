def nim():
    print('Welcome to nim')
    a=input('how many piles would u like')
    b=input('how many coins in pile 0')
    c=input('how many coins in pile 1')
    d=input('how many coins in pile 2')
    e=input('how many coins in pile 3')
    f = b - 1
    print('i remove 1 coins from file 0')
    print('pile 0 has coins',f)
    print('pile 1 has coins',c)
    print('pile 1 has coins',d)
    print('pile 1 has coins',e)
    '''i=0
    i1=0
    i2=0
    i3=0'''
    g=input('which pile would u like  to remove from?')
    i=0
    i1=0
    i2=0
    i3=0
    if g==0:
          h=input('how many coins remove from pile')
          i = b-h
          print('pile 0 has coins',i)
          #if i==0:
            #print('thanks for playing')
        
    if g==1:
         h=input('how many coins remove from pile')
         i1 = b-h
         print('pile 1 has coins',i1)
         #if i1==0:
           # print('thanks for playing')
    if g==2:
        h=input('how many coins remove from pile')
        i2 = b-h
        print('pile 2 has coins',i2)
        #if i2==0:
           #print('thanks for playing')
    if g==3:
         h=input('how many coins remove from pile')
         i3 = b-h
         print('pile 3 has coins',i3)
    while  i!=0 and i1!=0 and i2!=0 and i3!=0:
            if i==0 and i1==0 and i2==0 and i3==0: 
              print('thanks for playing')
              break
            
        
    
    

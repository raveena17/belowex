def nim():
    print('Welcome to nim')
    a=input('how many piles would u like')
    b=input('how many coins in pile 0')
    c=input('how many coins in pile 1')
    d=input('how many coins in pile 2')
    e=input('how many coins in pile 3')
    f = b - 1
    #while True:
    print('i remove 1 coins from file 0')
    print('pile 0 has coins',f)
    print('pile 1 has coins',c)
    print('pile 2 has coins',d)
    print('pile 3 has coins',e)
    while True:
       g=input('which pile would u like  to remove from?')
       i=0
       if g==0:
          h=input('how many coins remove from pile')
          i = b-h
          print('pile 0 has coins',i)
          if i==0:
            print('thanks for playing')
        
       elif g==1:
         h=input('how many coins remove from pile')
         i1 = b-h
         print('pile 0 has coins',i)
         if i1==0:
            print('thanks for playing')
       elif g==2:
        h=input('how many coins remove from pile')
        i2 = b-h
        print('pile 0 has coins',i)
        if i2 == 0:
           print('thanks for playing')
       elif g==3:
         h=input('how many coins remove from pile')
         i3 = b-h
         print('pile 0 has coins',i)
         if i3==0:
           print('thanks for playing')
        
    
    

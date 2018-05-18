def nim():
 while True:
    print('Welcome to nim')
    #a=input('how many piles would u like')
    b=input('how many coins in pile 0')
    c=input('how many coins in pile 1')
    d=input('how many coins in pile 2')
    e=input('how many coins in pile 3')
    f = b - 1
    print(' remove 1 coins from file 0')
    print('pile 0 has coins',f)
    print('pile 1 has coins',c)
    print('pile 1 has coins',d)
    print('pile 1 has coins',e)
    
    while e>0 or f>0 or c>0 or d>0:
       g=input('which pile would u like  to remove from?')
       if g==0:
          h=input('how many coins remove from pile')
          f = f-h
          print 'pile 0 has coins',f
       if g==1:
          h=input('how many coins remove from pile')
          c = c-h
          print 'pile 1 has coins',c      
       if g==2:
          h=input('how many coins remove from pile')
          d = d-h
          print 'pile 2 has coins',d     
       if g==3:
          h=input('how many coins remove from pile')
          e = e-h
          print 'pile 3 has coins',e
    print 'I Win.'
        
    p=raw_input('would you like to play again')
    if p =='n':
       print'thanks for playing!Bye'
       break
        
       
    

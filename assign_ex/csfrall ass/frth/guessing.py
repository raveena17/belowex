L=[[2.000,4.000,5.000,34.000],[2.000,7.000,4.000,36.000],[3.000,5.000,4.000,35.000]]
def guess(L):
 print('1:enter the value in existing array')
 print('2:print the array')
 print('3:multiply an array row')
 print('4:Add one row into another')
 print('5:Add multiple of one row to another')
 print('6:solve')
 print('7:Invert[This is extra credit]')
 print('8:Quit')
 while True:
    a =input('choose one:')
    if a==2:
        print('The array is now',L)
    if a==3:
        b=input('which row?')
        c=input('what multiple')
        d=(L[b]*c)
        print('The array is now',d)
    if a==4:
        b=input('which is the source row')
        c=input('which is the destination row')
        d=(L[0]+L[1])
        print('the array is now',d)
    if a==5:
        b=input('which is the source')
        c=input('what multiple of that row')
        d=input('which is the destination row')
        e=(L[b]*c)
        f=(e)+(L[d])
        print('the array is now',f)
    if a==8:
        print'Quitt'
        break
print guess(L)
        

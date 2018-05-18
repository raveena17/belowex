import math
def mn():
 print('0 input a new list')
 print('1 print the current list')
 print('2 find the avg price')
 print('3 find stdrd deviation')
 print('4 find the min and its day')
 print('5 find the max and its day')
 print('6 your t investment plan')
 print('9 quit')
 L=[]
 while True:
    a = input('enter ur choice:')
    #L=[]
    if a == 0:
         for i in range(3):
             a=input('enter the value')
             L.append(a)
         print L
    elif a==1:
        print'Day  Price'
        print'---  -----'
        for i in range(3):
            print i ,float(L[i])         
    elif a== 2:
         avg = float(sum(L)/len(L))
         print(avg)
    elif a==3:
        dev = float(math.sqrt(sum(L)-((sum(L)/len(L))))**2/len(L))
        print dev
    elif a==4:
         mini = (min(L))
         for i in range(len(L)):
             if L[i]==mini:
               print'The min is {} on day'.format(mini),i
    elif a==5:
         maxi = max(L)
         for i in range(len(L)):
             if L[i]==maxi:
               print'The max is {} on day'.format(maxi),i
         
    elif a==6:
          print'your TTS investment strategy is to'
          print 'Buy on day 1 at price',L[1]
          print 'Sell on day 2 at price', L[2]
          l=L[2]-L[1]
          print 'For a total profit of',l
    elif a==7:
           print('The choice 7 is not an option')
           print('try again')
    elif a==9:
           print('Quit')
           print('See you yesterday')
           break
print mn() 
          
          

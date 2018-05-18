import math
def firstNumlarger():
    while True:
      a=input(" enter the num")
      b=input("enter the num")
      if a>b:
                print('a is  larger than b')
                break
      if a<b:
                print('a is not larger than b')
                print('try again')

def sumto42(): 
      while True:
            t=0
            for s in range(5):
              s=input('enter the value')
              t = t+s
            print t
            if t==42:
                    break            
            else:
                 print('try again')
            
   
#print(firstNumlarger())
print sumto42()
 

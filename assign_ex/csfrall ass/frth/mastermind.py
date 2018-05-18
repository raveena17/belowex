import random
def mas():
    while True:
      print('welcome to mastermind')
      print('---------------------')
      a=input('how many holes per row shall we have?')
      b=input('how many rounds shall we have?')
      c=input('how many colors shall we have?')
      score=''
      for i in range(b):         
         l=[]  
         print 'enter your guess for round',i
         d=input('enter guess for hole 0:')
         e=input('enter guess for hole 1:')
         f=input('enter guess for hole 2:')
         comp = random.choice(range(c))
         l.append(d)
         l.append(e)
         l.append(f)
         #score=''
         if comp == d and comp == e and comp == f:
               score += '3 black'
         elif comp != d and comp != e and comp != f:
                score += '3 white' 
         elif comp == d and comp == e and  comp != f:
                score +=   '2black & 1 white'
         elif comp == d and comp != e and comp != f:
               score += '1 black & 2 white'
         elif comp != d and comp != e and comp != f:
               score +='3 white'
         print'===START BOARD==='
         print'round {}'.format(i),l,score
         print '===END BOARD===' 
      g=raw_input('would you like to play again?')
      if g=='no':
        break
    
        

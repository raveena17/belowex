import random
def gues(high, low):
 count=0
 while True:
    comp = random.choice(range(low, high))
    print 'ur num is',comp
    a = raw_input('enter yes or no:')
    count=count+1
    if a == 'y':
       print 'I guessed your number in {} tries.'.format(count)
       c=raw_input('Play again')
       if c=='n':
          break
    if a == 'n':
      b=raw_input('Is your number higher or lower ')
      if b=='l':
       comp = random.choice(range(low,comp))
      if b=='h':
          comp = random.choice(range(comp,high))  
print gues(10, 1)


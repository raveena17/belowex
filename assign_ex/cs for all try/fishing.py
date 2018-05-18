from fish import Fish

from pond import Pond

class Fisherman:
    def gofishing(self):
       print '1.Add fish'
       print '2.catch fish'
       choice = input('enter your choice:')
       if choice == 1:
           pond = Pond()
           fish_add = pond.add(fish_name, fish_size, fish_id) 
       elif choice == 2:
           pond = Pond()
           fishing = pond.catch()
    
        

import random

class Fish:
    

     def __init__(self, fish_name, fish_size):
        self.fish_name = fish_name
        self.fish_size = fish_size

Pike = Fish('Pike', 5)
Boss = Fish('Boss', 8)
SunFish = Fish('SunFish', 6)
Star = Fish('Star', 7)
GoldFish = Fish('GoldFish', 7)
Angler = Fish('Angler', 7)


class Pond:

    fish_list = []
    def add_fish(self,fish):
        #self.fish_list = []
        self.fish_list.append(fish)
        #return self.fish_list
    
    def catch(self):
        fish = random.choice(self.fish_list)
        self.fish_list.remove(fish)
        return fish

    def  display_fish(self):
         #print len(self.fish_list)
         for Fish in range(len(self.fish_list)):
              fish = self.fish_list[Fish]
              print fish.fish_name, fish.fish_size

lotus = Pond()
lotus.add_fish(Pike)
lotus.add_fish(Boss)
lotus.add_fish(SunFish)
lotus.add_fish(Star)
lotus.add_fish(GoldFish)
lotus.add_fish(Angler)
nile = Pond()
nile.add_fish(Pike)
nile.display_fish()
'''nile.add_fish(Boss)
nile.add_fish(SunFish)
nile.add_fish(Star)
nile.add_fish(GoldFish)
nile.add_fish(Angler)'''


class Fisher:

    fisher_list=[]
    def add_fish(self, fish):
          self.fisher_list.append(fish)
          return self.fisher_list

    def display_gotfish(self):   
         for Fish in range(len(self.fisher_list)):
              fish = self.fisher_list[Fish]
              print fish.fish_name, fish.fish_size
    
    def go_fishing(self):
        size = input('enter the size of fish: ')
        catch_fish  = lotus.catch()
        if catch_fish.fish_size >= size:
             self.add_fish(catch_fish)
             self.display_gotfish()
             #return catch_fish
        else:
             lotus.add_fish(catch_fish)           


    def go(self):
         for fishing in range(5):
              self.go_fishing()








              
    
    


















rehan = Fisher()
rehan.go()





    

     

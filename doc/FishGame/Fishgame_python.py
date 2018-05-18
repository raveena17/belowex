import random

class Fish:
    def __init__(self,fish_name, fish_size):
        self.fish_name = fish_name
        self.fish_size = fish_size



Pike = Fish('Pike', 5)
Sushi = Fish('Sushi', 2)
Bubbles = Fish('Bubbles', 4)
Casper = Fish('Casper', 6)
Shadow = Fish('Shadow',8 )
Comet = Fish('Comet', 3)
Charlie = Fish('Charlie', 7)
Goldie = Fish('Goldie',1 )
Nemo = Fish('Nemo',2 )
Pumpkin = Fish('Pumpkin', 5)


class Pond:
    
    pond_name= raw_input("Enter the pond name:")
    pond_size=raw_input("Enter the pond size:")
    fish_type=raw_input("How many types of fishes in that pond:")
    display=raw_input("display/not:")

    list=[]
    def __add__(self,fish):
        self.list.append(fish)
        #return list

    def catch(self):
        fish = random.choice(self.list)
        self.list.remove(fish)
        return fish
        
    def  display(self):
        print len(self.list)
        for Fish in range(len(self.list)):
            fish = self.list[Fish]
            print fish.fish_name, fish.fish_size

              
        

              
pond = Pond()
pond.__add__(Pike)
pond.__add__(Sushi)
pond.__add__(Bubbles)
pond.__add__(Casper)
pond.__add__(Shadow)
pond.__add__(Comet)
pond.__add__(Charlie)
pond.__add__(Goldie)
pond.__add__(Nemo)
pond.__add__(Pumpkin)

nile = Pond()
nile.__add__(Pike)
nile.display()

'''nile.__add__(Pike)
nile.__add__(Sushi)
nile.__add__(Bubbles)
nile.__add__(Casper)
nile.__add__(Shadow)
nile.__add__(Comet)
nile.__add__(Charlie)
nile.__add__(Goldie)
nile.__add__(Nemo)
nile.__add__(Pumpkin)'''



class Fisher:

    fisher_list=[]
    def __add__(self, fish):
          self.fisher_list.append(fish)
          return self.fisher_list

    def display_gotfish(self):   
         for Fish in range(len(self.fisher_list)):
              fish = self.fisher_list[Fish]
              print fish.fish_name, fish.fish_size
    
    def go_fishing(self):
        size = input('enter the size of fish: ')
        catch_fish  = pond.catch()
        if catch_fish.fish_size >= size:
             self.__add__(catch_fish)
             self.display_gotfish()
             #return catch_fish
        else:
             pond.__add__(catch_fish)           


    def go(self):
         for fishing in range(5):
              self.go_fishing()



fisher = Fisher()
fisher.go()


#OUTPUT:

##Enter the pond name:"lotus pond"
##Enter the pond size:2500 "square cm"
##How many types of fishes in that pond:10
##display/not:"display"
##
##11                            #len(fish)
##Pike 5
##Sushi 2
##Bubbles 4
##Casper 6
##Shadow 8
##Comet 3
##Charlie 7
##Goldie 1
##Nemo 2
##Pumpkin 5
##Pike 5  ----->                     #add(another fish)
##
##Enter the size of fish: 5
##Casper 6
##Enter the size of fish: 6
##Enter the size of fish: 4
##Casper 6
##Pike 5
##Enter the size of fish: 3
##Casper 6
##Pike 5
##Pumpkin 5
##Enter the size of fish: 2
##Casper 6
##Pike 5
##Pumpkin 5
##Charlie 7
##
##
##
##

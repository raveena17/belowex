import random

class Fish:
    def __init__(self, fish_name, fish_size):
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
nile.__add__(Sushi)
nile.display()



class Fisher:

    Fishermen_name=raw_input("Enter the fishermen name:")
    Fisher_list=[]
    def __add__(self, Fish):
        self.Fisher_list.append(Fish)
        return self.Fisher_list

    def display_gotFish(self):
        y=len(self.Fisher_list)
        for fish in range(y):
            Fish = self.Fisher_list[fish]
            print Fish.Fish_name, Fish.Fish_size

    def go_Fishing(self, pond_name, size):
        catch_Fish= self.pond_name.catch()
        if catch_Fish.Fish_size >= self.size:
            self.__add__(catch_Fish)
            self.display_gotFish()

        else:
            pond_name.__add__(catch_fish)


    def go(self, pond_name, size):
        self.pond_name = pond_name
        self.size = size
       # Fishermen_name=raw_input("Enter the fishermen name:")
        for Fishing in range(6):
            self.go_Fishing(pond_name, size)


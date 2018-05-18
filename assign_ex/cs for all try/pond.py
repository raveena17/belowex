from fish import Fish
import random
class Pond:

    fish_list = []
    def add_fish(self,fish):
        self.fish_list.append(fish)
        return self.fish_list

    def catch(self):
        #fish = Fish()
        #self.fish = fish.create_fish()
        self.fish_list = self.fish_list()
        self.fish_catch = random.choice(self.fish_list)
        self.remove_fish = self.fish_catch.remove(self.fish_catch)
        return self.fish_catch
        

import pdb
pdb.set_trace()
pond = Pond()
fish=Fish('Pike', 5, 1)
pond.add_fish(fish)
r', 7, 4)
pond.catch('Goldfish', 5, 5)
pond.catch('Angler', 5, 6)'''

'''Pike.create_fish('Pike', 5, 1)
Pike.create_fish('Sunfish', 6, 2)
Pike.create_fish('Bass', 5, 3)
Pike.create_fish('Star', 7, 4)
Pike.create_fish('Goldfish', 5, 5)
Pike.create_fish('Angler', 5, 6)'''
            

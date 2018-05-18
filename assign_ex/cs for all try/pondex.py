
import random

class Fish:
    def set_species(self):
        self.species = ['Pike', 'Bass', 'SunFish','Pike','Bass']
        return self.species

    def select_species(self):
        self.select_fish = self.set_species()
        self.fish = random.choice(self.select_fish)
        return self.fish

    def id_declare(self):
        self.fish = self.select_species()
        self.list_fish = self.set_species()
        self.fish_id = self.list_fish.index(self.fish)
        return self.fish_id

    def size_declare(self):
        self.size = [5,6,7,5,5]
        self.id = self.id_declare()
        self.size_fish = self.size[self.id]
        return self.size_fish
    


class Pond(Fish):
    def set_capacity_pond(self):
        self.capacity_pond = 10
        return self.capacity_pond

    def add(self):
        self.fish_add = raw_input('which fish you want add into pond: ')
        self.add_fish = Fish.set_species()
        self.length_list = len(self.add_fish)
        self.capacity = self.set_capacity_pond()
        if self.length_list < self.capacity_pond:
            self.fish_added = self.add_fish.append(self.fish_add)
            #self.fish_in_pond = print('successfully fish added')
            return self.fish_added
        else:
            print('pond capacity exceed')
    def catch(self,fish):
        #self.fish_remove = select_species()
        #self.remove_fish = Fish.set_species()
        #self.length_list = len(self.add_fish)
        if self.length_list > 0 :
            self.fish_catch = self.remove_fish.remove(self.fish)
            #self.fish_in_pond = print('successfully fish added')
            return self.fish_catch
        else:
            print('pond have no fish')

class Fisher_class(Pond):   
    def goFishing(self):
        fish_weight = input('size of fish')
        fish_catch = Fish.size_declare()
        fishes =[]
        counter = 0
        while counter<5:
         counter = counter+1
         if fish-catch == fish_weight:
            fish = select_species()
            fishes_in_fisherman = fish.append(fishes)
            fish_in_pond = Pond.catch(fish)
            return fishes_in_fisherman
         if counter==4:
            print('your turn finished')
            break
            
    
    


Rehan = Pond()

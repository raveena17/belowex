import random

class Pond():
    
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

    def set_capacity_pond(self):
        self.capacity_pond = 10
        return self.capacity_pond

    def add(self):
        self.fish_add = input('how many fish you want add into pond: ')
        self.add_fish = self.set_species()
        self.length_list = len(self.add_fish)
        self.capacity = self.set_capacity_pond()
        if self.length_list < self.capacity:
          for fish in range(self.fish_add):
            self.fish_add = raw_input('which fish you want add into pond: ')
            #self.fish_size = input('size of fish')
            self.add_fish.append(self.fish_add)
          print('successfully fish added')
          return self.add_fish
        else:
            print('Pond capacity exceed')


    def catch(self):
        self.fish_remove = input('how many fish you want catch:')
        self.remove_fish = self.set_species()
        self.length_list = len(self.remove_fish)
        if self.length_list > 0:
           for fish_catch in range(self.fish_remove):
            self.catch_fish = self.select_speciec()
            self.remove_fish.remove(self.catch_fish)
           return self.remove_fish

    
    
        
c1=pond()

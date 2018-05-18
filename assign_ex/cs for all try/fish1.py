
class Fish:
       name = ''
       def create_fish(self,fish,size):
           self.name = fish
           self.size = size
           print self.name + '' + 'created successfully'
           #pond = Pond()
           self.get_fish()
           #return fish

       def get_fish(self):
           fish = Fish()
           print fish.name 
    


class Pond:
    def get_fish(self):
        fish = Fish()
        print fish.name

fish = Fish()
fish.create_fish('fike', '20')

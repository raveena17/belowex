
class Fisher():

    Fishermen = raw_input("Enter the Fishermen Name:")
    Fishermen_list=[]
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
        for Fishing in range(10):
            self.go_Fishing(pond_name, size)


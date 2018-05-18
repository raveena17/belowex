class Arithmetic:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __add__(self):
         print("Addition = {0}+{1}".format(self.a,self.b))
         x = self.a+self.b
         return x

    def __sub__(self):
        print("Subtraction = {0}-{1}".format(self.a,self.b))
        x = self.a-self.b
        return x


    def __mul__(self):
        print("Multiplication = {0}*{1}".format(self.a,self.b))
        x = self.a*self.b
        return x


    def __div__(self):
        print("Divition = {0}/{1}".format(self.a,self.b))
        x = self.a/self.b
        return x

    def getStats(self):
        return "__add__:    %s\n__sub__:  %s\n__mul__:   %s\n__div__:   %s" % (self.__add__(), self.__sub__(), self.__mul__(), self.__div__())

def main():
    print "Arithmetic Operation:"
    m= Arithmetic(5,7)
    print "__add__:   %s" % m.__add__()
    print "__sub__:   %s" % m.__sub__()
    print "__mul__:   %s" % m.__mul__()
    print "__div__:   %s" % m.__div__()
    print m.getStats()
    print ""



#OUTPUT:

>>> main()
Arithmetic Operation:
Addition = 5+7
__add__:   12
Subtraction = 5-7
__sub__:   -2
Multiplication = 5*7
__mul__:   35
Divition = 5/7
__div__:   0
Addition = 5+7
Subtraction = 5-7
Multiplication = 5*7
Divition = 5/7
__add__:    12
__sub__:  -2
__mul__:   35
__div__:   0


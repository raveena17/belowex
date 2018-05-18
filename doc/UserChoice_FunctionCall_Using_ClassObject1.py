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


        
c1 = Arithmetic(4,5)


#OUTPUT:

>>> c1.__add__()
Addition = 4+5
9
>>> c1.__sub__()
Subtraction = 4-5
-1
>>> c1.__mul__()
Multiplication = 4*5
20
>>> c1.__div__()
Divition = 4/5
0
>>> 
